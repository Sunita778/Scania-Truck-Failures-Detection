import pandas as pd
from sensor.logger import logging
from sensor.exception import SensorException
from sensor.config import mongo_client
import sys, os
def get_collection_as_dataframe(database_name:str, collection_name:str)->pd.Dataframe:
    """
    Description: This function return collection as dataframe
    Params: 
    database name: database name
    collection_name: collection name
    ==========================================================
    retun Pandas dataframe  of a collection
    """
    try:
        logging.info("Reading data from database: {} and collection {}")
        df = pd.Dataframe(list(mongo_client[database_name][collection_name].find()))
        logging.info(f"Found columns: {df.columns}")
        if "_id" in df.columns:
            logging.info(f"Droppinggg column: _id ")
            df = df.drop("_id", axis=1)
        logging.info(f"Rows and Columns in df: {df.shape}")
        return df
    except Exception as e:
        raise SensorException(e, sys)