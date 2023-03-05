from sqlalchemy import types
import datetime
import os
import json
import pandas as pd
import constants 
class DataSchema:
    def __init__(self) -> None:
        None 

    def players_table_schema(self):
        players_table_sql_types =  {'player_name' : types.VARCHAR,
                    'team_name':types.VARCHAR,
                    'date_of_birth':types.Date,
                    'batting_style':types.VARCHAR,
                    'bowling_style':types.VARCHAR,
                    'player_role':types.VARCHAR,
                    'player_type':types.VARCHAR}
        
        return players_table_sql_types
    
    def teams_table_schema(self):
        teams_table_sql_types =  {'team_name' : types.VARCHAR,
                    'team_short_name':types.VARCHAR,
                    'team_logo_url':types.VARCHAR,
                    'team_captain':types.Integer,
                    'team_coach':types.VARCHAR}
        return teams_table_sql_types
    

if __name__=="__main__":
    ds = DataSchema()
