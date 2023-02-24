import psycopg2
import pandas as pd

from sqlalchemy import create_engine
engine = create_engine("postgresql+psycopg2://postgres:postgres@ec2-100-25-135-202.compute-1.amazonaws.com")

conn = engine.connect()

print(conn)

df = pd.read_sql("select * from public.supply_chain", con = engine)

print(df.shape)

