# Importing the libraries

from datetime import datetime
from pathlib import Path
import os

print(datetime.now())

package_name = 'customer_churn'

files_list = [
    Path('.github') / 'workflows' / '.gitkeep',
    f'src/__init__.py'
    f'src/{package_name}/__init__.py',
    f'src/{package_name}/elements/__init__.py',
    f'src/{package_name}/elements/e_01_data_ingestion.py',
    f'src/{package_name}/elements/e_02_data_validation.py',
    f'src/{package_name}/elements/e_03_data_transformation.py',
    f'src/{package_name}/elements/e_04_model_trainer.py',
    f'src/{package_name}/elements/e_05_model_evaluation.py',
    f'src/{package_name}/elements/e_06_model_validation.py',
    f'src/{package_name}/utils/__init__.py',
    f'src/{package_name}/utils/commons.py',
    f'src/{package_name}/config/__init__.py',
    f'src/{package_name}/config/configuration.py',
    f'src/{package_name}/pipelines/__init__.py',
    f'src/{package_name}/pipelines/pipe_01_data_ingestion.py',
    f'src/{package_name}/pipelines/pipe_02_data_validation.py',
    f'src/{package_name}/pipelines/pipe_03_data_transformation.py',
    f'src/{package_name}/pipelines/pipe_04_model_trainer.py',
    f'src/{package_name}/pipelines/pipe_05_model_evaluation.py',
    f'src/{package_name}/pipelines/pipe_06_model_validation.py',
    f'src/{package_name}/pipelines/pipe_07_model_prediction_pipeline.py',
    f'src/{package_name}/entity/__init__.py',
    f'src/{package_name}/entity/config_entity.py',
    f'src/{package_name}/constants/__init__.py',
    f'src/{package_name}/exception.py',
    f'src/{package_name}/logger.py',
    'config/config.yaml',
    'metrics_threshold.yaml',
    'params.yaml',
    'schema.yaml',
    'main.py',
    'app.py',
    'setup.py',
    'app_streamlit.py',
    'Dockerfile',
    'requirements.txt',
    'requirements_dev.txt',
    'trials/trial_01_data_ingestion.py',
    'trials/trial_02_data_validation.py',
    'trials/trial_03_data_transformation.py',
    'trials/trial_04_model_trainer.py',
    'trials/trial_05_model_evaluation.py',
    'trials/trial_06_model_validation.py',
    'templates/home.html',
    'templates/index.html',
    'templates/prediction.html',
    'templates/train.html',
    'static/styles.css'

]

# Traversing through each file from the list
for filepath in files_list:
    filepath = Path(filepath)

    # Splitting the filename and directory from the filepath
    filedir, filename = os.path.split(filepath)

    # Creating new folders if not present
    if filedir != '':
        os.makedirs(filedir,exist_ok=True)

    # Creating empty file if not present or empty
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, 'w') as f:
            pass

