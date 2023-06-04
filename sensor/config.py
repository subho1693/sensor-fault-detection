import pymongo
# import pandas as pd 
import json
import os 


class EnvironmentVariable:
    mongo_db_url:str = os.getenv('MONGO_DB_URL')

env_var = EnvironmentVariable()
MONGODB_DB_URL = env_var.mongo_db_url
