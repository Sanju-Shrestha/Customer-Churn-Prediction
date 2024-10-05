from src.customer_churn import logging
from src.customer_churn.pipelines.pipe_01_data_ingestion import DataIngestionPipeline
from src.customer_churn.pipelines.pipe_02_data_validation import DataValidationPipeline
from src.customer_churn.pipelines.pipe_03_data_transformation import DataTransformationPipeline
from src.customer_churn.pipelines.pipe_04_model_trainer import ModelTrainerPipeline
from src.customer_churn.pipelines.pipe_05_model_evaluation import ModelEvaluationPipeline
from src.customer_churn.pipelines.pipe_06_model_validation import ModelValidationPipeline

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

ELEMENT_03_NAME = "DATA TRANSFORMATION ELEMENT"
try:
    logging.info(f"## =================== {ELEMENT_03_NAME} Started! ========================##")
    data_transformation_pipeline = DataTransformationPipeline()
    data_transformation_pipeline.run()
    logging.info(f"## =============== {ELEMENT_03_NAME} Terminated Successfully!=================\n\nx************************x")
except Exception as e:
    logging.exception(e)
    raise e

ELEMENT_04_NAME = "MODEL TRAINER ELEMENT"
try:
    logging.info(f"## =================== {ELEMENT_04_NAME} Started! ========================##")
    model_trainer_pipeline = ModelTrainerPipeline()
    model_trainer_pipeline.run()
    logging.info(f"## =============== {ELEMENT_04_NAME} Terminated Successfully!=================\n\nx************************x")
except Exception as e:
    logging.exception(e)
    raise e

ELEMENT_05_NAME = "MODEL EVALUATION ELEMENT"
try:
    logging.info(f"## =================== {ELEMENT_05_NAME} Started! ========================##")
    model_evaluation_pipeline = ModelEvaluationPipeline()
    model_evaluation_pipeline.run()
    logging.info(f"## =============== {ELEMENT_05_NAME} Terminated Successfully!=================\n\nx************************x")
except Exception as e:
    logging.exception(e)
    raise e

ELEMENT_06_NAME = "MODEL VALIDATION ELEMENT"
try:
    logging.info(f"## =================== {ELEMENT_06_NAME} Started! ========================##")
    model_validation_pipeline = ModelValidationPipeline()
    model_validation_pipeline.run()
    logging.info(f"## =============== {ELEMENT_06_NAME} Terminated Successfully!=================\n\nx************************x")
except Exception as e:
    logging.exception(e)
    raise e