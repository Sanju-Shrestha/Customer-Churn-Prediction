# Customer Churn Prediction using MLOps

[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/streamlit)](https://pypi.org/project/dagshub/)

Customer churn is a critical challenge for businesses, as it directly impacts revenue and customer retention strategies. The churn rate measures the percentage of customers who stop using a company's products or services over a certain time period. To help businesses proactively reduce churn, we can leverage machine learning models to predict which customers are likely to leave. This prediction is based on a combination of user demographic data, behavior patterns, and transaction history.

In this case, each user is assigned a churn risk score ranging from 1 to 5, where a higher score indicates a greater likelihood of churn. This score is updated daily for users who have made at least one transaction, and it helps businesses focus their retention efforts more effectively.

This repository builds a machine learning model that predicts the churn risk score for each customer based on the provided features. The dataset contains various customer-related information such as demographic details, browsing behavior, transaction history, and membership details. Using this data, the model should be trained to assign a churn score between 1 and 5 for each user, indicating the risk of them leaving the business.

Credits: This dataset is sourced from a machine learning challenge conducted by HackerEarth. You can learn more about the challenge at the official HackerEarth page [here](https://www.hackerearth.com/challenges/competitive/hackerearth-machine-learning-challenge-predict-customer-churn/).

This repository contains an end-to-end MLOps pipeline for predicting customer churn using a machine learning model. The project implements various stages of the MLOps lifecycle, including data ingestion, validation, transformation, model training, evaluation, and validation using tools like MongoDB Atlas, LightGBM, DVC, MLflow, and Dagshub.

## Project Structure

The project is modularized and follows the standard MLOps practices, with the following structure:

```plaintext
customer_churn_prediction/
├── config/
│   └── config.yaml                  # Configuration file for the project
├── data/                            # Directory for datasets (tracked with DVC)
├── notebooks/
│   └── ETL_Customer_Churn.ipynb     # Jupyter notebook for ETL process
├── src/
│   └── customer_churn/
│       ├── config/
│       │   └── configuration.py     # Reads and manages configuration settings
│       ├── elements/
│       │   ├── e_01_Data_Ingestion.py
│       │   ├── e_02_Data_Validation.py
│       │   ├── e_03_Data_Transformation.py
│       │   ├── e_04_Model_Trainer.py
│       │   ├── e_05_Model_Evaluation.py
│       │   └── e_06_Model_Validation.py
│       ├── entity/
│       │   └── config_entity.py      # Defines data structures for configuration
│       └── pipelines/
│           ├── pipe_01_Data_Ingestion.py
│           ├── pipe_02_Data_Validation.py
│           ├── pipe_03_Data_Transformation.py
│           ├── pipe_04_Model_Trainer.py
│           ├── pipe_05_Model_Evaluation.py
│           └── pipe_06_Model_Validation.py
├── Trials/
│   ├── Trial_01_Data_Ingestion.py    # Initial trial for data ingestion
│   ├── Trial_02_Data_Validation.py   # Initial trial for data validation
│   ├── Trial_03_Data_Transformation.py
│   ├── Trial_04_Model_Trainer.py     # Using LightGBM
│   ├── Trial_05_Model_Evaluation.py
│   └── Trial_06_Model_Validation.py
├── dvc.yaml                          # DVC pipeline definition
├── main.py                           # Entry point to trigger the pipeline
├── params.yaml                       
├── README.md                         # Project documentation
└── schema.yaml                       
```

## Key Features

  * MongoDB Atlas: The dataset for this project is stored in MongoDB Atlas. The raw data is stored in the customer_churn.churndb collection, and the transformed data is stored in the customer_churn.transformed_churndb collection.

  * ETL Process: The ETL pipeline is implemented using Jupyter notebooks and MongoDB. The transformed dataset is saved back to MongoDB for further processing.

  * Data Version Control (DVC): DVC is used for tracking datasets and model versions.

  * Machine Learning Model: LightGBM is used as the machine learning model for churn prediction. The training process is modularized into stages such as data ingestion, validation, transformation, training, evaluation, and validation.

  * MLflow & Dagshub: MLflow is used for tracking experiments, and Dagshub is integrated to monitor and collaborate on the project.


## Project Workflow

* Setup Repository and Folders:
	
	- The repository is organized with necessary folders for data, configurations, and modularized code.

* Data Collection:
	
	- The dataset is sourced from Kaggle and uploaded to MongoDB Atlas under the customer_churn database.
        - Raw data is stored in the churndb collection.

* ETL Process:
	
	- Data is cleaned, transformed, and saved in the transformed_churndb collection. The process is documented in notebooks\ETL_Customer_Churn.ipynb.

* Config Management:
	
	- Configurations are managed through config\config.yaml, including MongoDB credentials and paths.

* Pipeline Stages:

	- Data Ingestion: Fetches data from MongoDB (pipe_01_Data_Ingestion.py).
        - Data Validation: Ensures data quality and consistency (pipe_02_Data_Validation.py).
        - Data Transformation: Prepares the dataset for model training (pipe_03_Data_Transformation.py).
        - Model Training: LightGBM is trained on the transformed data (pipe_04_Model_Trainer.py).
        - Model Evaluation: Evaluates the model performance (pipe_05_Model_Evaluation.py).
        - Model Validation: Validates the model on unseen data (pipe_06_Model_Validation.py).

* Modularization:
	- All the steps are broken down into elements (modular Python scripts) and can be executed individually or as part of a pipeline using DVC.

* Experiment Tracking:
	- MLflow is used to track experiments, including model parameters and metrics.
        - Dagshub is used for project collaboration and monitoring.

## Getting Started

### Prerequisites

	* Python 3.8+
	* MongoDB Atlas account
	* DVC
	* MLflow
	* HanckerEarth login access (for dataset)

## Installation

1) Clone the repository:

```bash
git clone https://github.com/Sanju-Shrestha/Customer-Churn-Prediction.git
cd Customer-Churn-Prediction
```

2) Install required dependencies:

```bash
pip install -r requirements.txt
```

3) Setup MongoDB Atlas and update the credentials in config\config.yaml.

4) Initialize DVC:

```bash
dvc init
```


## Running the Project

1) Run ETL Notebook:
	
	- Execute notebooks\ETL_Customer_Churn.ipynb to perform the ETL process and save the transformed data to MongoDB Atlas.

2) Trigger Pipelines:
	
	- To run the entire pipeline:
	
	```bash
	python main.py
	```

3) Track Experiments with MLflow:
	
	- MLflow is already integrated. Track model metrics and parameters by accessing the MLflow UI:

	```bash
	mlflow ui
	```

4) Monitor on Dagshub:
	
	- Access Dagshub to monitor and collaborate on the project.

## Contribution Guidelines

Contributions are welcome! Feel free to submit a pull request or open an issue for any bugs or feature requests.

## License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/Sanju-Shrestha/Customer-Churn-Prediction/blob/95f373eb2f843a974d188240cd468f450a7cb0c9/LICENSE) file for details.