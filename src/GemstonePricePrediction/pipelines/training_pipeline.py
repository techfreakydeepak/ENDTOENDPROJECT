import sys
sys.path.insert(0, 'C:\ENDTOENDPROJECT')
from src.GemstonePricePrediction import logger


from src.GemstonePricePrediction.components.data_ingestion import DataIngestion

import os
import sys
from src.GemstonePricePrediction.logger import logging
from src.GemstonePricePrediction.exception import GemstoneException
import pandas as pd


obj=DataIngestion()
obj.initiate_data_ingestion()