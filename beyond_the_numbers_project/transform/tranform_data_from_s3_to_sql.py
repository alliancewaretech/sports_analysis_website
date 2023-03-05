from sqlalchemy import types
import datetime
import os
import json
import pandas as pd
import constants
from data_access_layer.flexible_data_read import FlexDataRead
from transform.schemas import DataSchema
import psycopg2
from sqlalchemy import create_engine
class S3ToSQL:
    def __init__(self) -> None:
        self.directory_of_files = constants.JSON_FILE_DIR
        self.fdr = FlexDataRead()
        self.engine = create_engine("postgresql+psycopg2://{0}:{1}@{2}:5432/sports_analysis".format(constants.POSTGRES_USER,constants.POSTGRES_PASSWORD,constants.POSTGRES_HOST))
        self.conn = self.engine.connect()
        self.data_schema = DataSchema()

    def create_players_table(self):
        list_files = os.listdir(self.directory_of_files)
        team_players={}
        for ff in list_files:
            if "json" in ff:
            #print(os.path.join(directory_of_files,ff))
                data = self.fdr.read_json(os.path.join(self.directory_of_files,ff))
                for each in data["info"]["players"]:
                    for xx in data["info"]["players"][each]:
                        if xx not in team_players.keys():
                            team_players[xx]=each
        df = pd.DataFrame(team_players.items(),columns=['player_name','team_name'])
        date_string = "01-01-1980"
        df["date_of_birth"]=datetime.datetime.strptime(date_string,"%m-%d-%Y").date()
        df["batting_style"]="B"
        df["bowling_style"]="B"
        df["player_role"]="B"
        df["player_type"]="B"
        df.to_sql('players', con=self.conn, if_exists='append',schema='raw_tables',index=False,dtype=self.data_schema.players_table_schema)
        return df
    
    def create_teams_table(self):
        list_files = os.listdir(self.directory_of_files)
        list_files =['386532.json','676529.json']
        print(list_files)
        team_list_set=set()
        for ff in list_files:
            if "json" in ff:
                print(os.path.join(self.directory_of_files,ff))

                data = self.fdr.read_json(os.path.join(self.directory_of_files,ff))
                for team_list in data["info"]["teams"]:
                    team_list_set.add(team_list)
                print(team_list_set)
        df= pd.DataFrame(team_list_set,columns = ["team_name"])
        df["team_short_name"]=df["team_name"].apply(lambda x:x[:3])
        df["team_logo_url"]="logo"
        df["team_captain"]=8
        df["team_coach"]=""
        print(df)
        #df.to_sql('teams', con=self.conn, if_exists='append',schema='raw_tables',index=False,dtype=self.data_schema.teams_table_schema())
        print("Table Created with shape",df.shape)
        return df
    
    def create_series_table(self):
        list_files = os.listdir(self.directory_of_files)
        series_dict = {"series_name":[],"series_date":[],"host_country":[],"season":[]}
        for ff in list_files:
            if "json" in ff:
            #print(os.path.join(directory_of_files,ff))
                data = self.fdr.read_json(os.path.join(self.directory_of_files,ff))
                for each in (data["info"]["dates"]):
                    #print(data["info"]["event"])
                    series_dict["series_date"].append(each)
                    try:
                        series_dict["series_name"].append(data["info"]["event"]["name"])
                    except:
                        #print(data["info"])
                        series_dict["series_name"].append( data["info"]["teams"][0]+" tour of "+ data["info"]["teams"][1])
                    series_dict["host_country"].append(data["info"]["teams"][0])
                    series_dict["season"].append(data["info"]["season"]) 

        df = pd.DataFrame(series_dict)

        df["series_date"] = pd.to_datetime(df["series_date"])
        #df["series_start_date"]=df.groupby(["series_name","season"]).agg({"series_date":"min"}).reset_index()["series_date"].tolist()[0]
        #df["series_end_date"]=df.groupby(["series_name","season"]).agg({"series_date":"max"}).reset_index()["series_date"].tolist()[0]
        df = df.groupby(["series_name","season","host_country"])["series_date"].aggregate(['min','max']).reset_index()
        df.columns =["series_name","season","host_country","series_start_date","series_end_date"]
        #pd.DataFrame.from_dict(series_dict,orient='index').transpose()
        df = df.drop_duplicates()
        print(df)
        return df
    

    def create_series_matches_table(self):
        list_files = os.listdir(self.directory_of_files)
        series_dict = {"series_name":[],"match_id":[],"match_number":[],"season":[]}
        for ff in list_files:
            if "json" in ff:
            #print(os.path.join(directory_of_files,ff))
                data = self.fdr.read_json(os.path.join(self.directory_of_files,ff))
                for each in (data["info"]["dates"]):
                    #print(data["info"]["event"])
                    series_dict["series_date"].append(each)
                    try:
                        series_dict["series_name"].append(data["info"]["event"]["name"])
                    except:
                        #print(data["info"])
                        series_dict["series_name"].append( data["info"]["teams"][0]+" tour of "+ data["info"]["teams"][1])
                    series_dict["host_country"].append(data["info"]["teams"][0])
                    series_dict["season"].append(data["info"]["season"]) 

        df = pd.DataFrame(series_dict)

        df["series_date"] = pd.to_datetime(df["series_date"])
        #df["series_start_date"]=df.groupby(["series_name","season"]).agg({"series_date":"min"}).reset_index()["series_date"].tolist()[0]
        #df["series_end_date"]=df.groupby(["series_name","season"]).agg({"series_date":"max"}).reset_index()["series_date"].tolist()[0]
        df = df.groupby(["series_name","season","host_country"])["series_date"].aggregate(['min','max']).reset_index()
        df.columns =["series_name","season","host_country","series_start_date","series_end_date"]
        #pd.DataFrame.from_dict(series_dict,orient='index').transpose()
        df = df.drop_duplicates()
        print(df)
        return df


    
    def start_transformation(self):
        ## read json files in a loop
        return self.create_teams_table()
        #self.create_players_table()
        #return self.create_series_table()



if __name__=="__main__":
    sc = S3ToSQL()
    sc.start_transformation()