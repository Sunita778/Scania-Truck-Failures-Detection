import pymongo
import pandas as pd
import json
from dataclasses import dataclass

#Provide the mongodb localhost url to connect python to mongodb
import os
@dataclass
class EnviromentVAriable():
    mongo_db_url:str = os.getenv("MONGO_DB_URL")

env_var = EnviromentVAriable()

mongo_client = pymongo.MongoClient(env_car.mongo_db_url)


