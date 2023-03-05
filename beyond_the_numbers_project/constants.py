import os.path, sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))
os.environ['PATH']+=os.getcwd()
POSTGRES_HOST = "ec2-100-25-135-202.compute-1.amazonaws.com"
POSTGRES_USER = "postgres"
POSTGRES_PASSWORD = "postgres"  
AWS_CREDNTIALS_FILE="/Users/nyzy/.aws/credentials"
JSON_FILE_DIR = "/Users/nyzy/data/india_male_json"
S3_FILE_DIR= "s3://sports-analysis-project/raw_files/india_male_json/"