from src.customer_churn import logging
from src.customer_churn.pipelines.pipe_01_data_ingestion import DataIngestionPipeline
from src.customer_churn.pipelines.pipe_02_data_validation import DataValidationPipeline

ELEMENT_01_NAME = "DATA INGESTION ELEMENT"
try:
    logging.info(f"## =================== {ELEMENT_01_NAME} Started! ========================##")
    data_ingestion_pipeline = DataIngestionPipeline()
    data_ingestion_pipeline.run()
    logging.info(f"## =============== {ELEMENT_01_NAME} Terminated Successfully!=================\n\nx************************x")
except Exception as e:
    logging.exception(e)
    raise e

ELEMENT_02_NAME = "DATA VALIDATION ELEMENT"
try:
    logging.info(f"## =================== {ELEMENT_02_NAME} Started! ========================##")
    data_validation_pipeline = DataValidationPipeline()
    data_validation_pipeline.run()
    logging.info(f"## =============== {ELEMENT_02_NAME} Terminated Successfully!=================\n\nx************************x")
except Exception as e:
    logging.exception(e)
    raise e