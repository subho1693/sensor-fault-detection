from sensor.configuration.mongo_db_connection import MongoDBClient
from sensor.exception import SensorException
import os,sys
from  sensor.logger import logging

def text_exception():
    try:
        logging.info("we are dividing 1 by zero")
        a = 1/0
    except Exception as e:
        raise SensorException(e,sys)




if __name__ == '__main__':
    # print(os.getenv("MONGO_DB_URL"))
    mongodb_client = MongoDBClient()
    print("collections = ",mongodb_client.database.list_collection_names())
    # try:
    #     text_exception()
    # except Exception as e:
    #     raise SensorException(e,sys)