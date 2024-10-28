from sklearn.model_selection import StratifiedKFold
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import f1_score
import joblib
import os
from src.customer_churn import logging
from src.customer_churn.entity.config_entity import ModelTrainerConfig

# mlflow
import dagshub
import mlflow 

dagshub.init(repo_owner='Sanju-Shrestha', repo_name='Customer-Churn-Prediction', mlflow=True)
mlflow.set_tracking_uri('https://dagshub.com/Sanju-Shrestha/Customer-Churn-Prediction.mlflow')

    
class ModelTrainer:
    def __init__(self, config: ModelTrainerConfig):
        self.config = config

    def initiate_model_trainer(self, X_train_transformed, X_val_transformed, y_train, y_val):
        # Start an MLflow run
        with mlflow.start_run(run_name="LogisticRegression_Training"):  # Set a run name for clarity

            # Initialize the Stratified K-Fold cross-validator
            skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)

            # Perform Stratified K-Fold Cross-Validation
            fold_f1_scores = []
            for fold, (train_index, val_index) in enumerate (skf.split(X_train_transformed, y_train)):
                X_train_fold, X_val_fold = X_train_transformed[train_index], X_train_transformed[val_index]
                y_train_fold, y_val_fold = y_train.iloc[train_index], y_train.iloc[val_index]

                # Train the model on the training fold
                lr_model = LogisticRegression(
                    solver=self.config.solver,
                    penalty=self.config.penalty,
                    C=self.config.C,
                    max_iter=self.config.max_iter,
                    verbose=0,
                )
                lr_model.fit(X_train_fold, y_train_fold)

                # Validate the model on the validation fold
                y_val_pred = lr_model.predict(X_val_fold)

                # Evaluate the model
                fold_f1 = f1_score(y_val_fold, y_val_pred, average='macro')
                fold_f1_scores.append(fold_f1)
                print(f"Fold Validation Macro F1-Score: {fold_f1}")

                # Log fold-specific metrics in MLflow
                mlflow.log_metric("fold_f1_score", fold_f1, step=fold)

            # Print average Macro F1-Score across all folds
            avg_f1 = sum(fold_f1_scores) / len(fold_f1_scores)
            print(f"Average Cross-Validation Macro F1-Score: {avg_f1}")

            # Log average F1 in MLflow
            mlflow.log_metric("avg_f1_score", avg_f1)

            # Final training on full training set
            lr_model.fit(X_train_transformed, y_train)

            # Log model hyperparameters
            mlflow.log_param("solver", self.config.solver)
            mlflow.log_param("penalty", self.config.penalty)
            mlflow.log_param("C", self.config.C)
            mlflow.log_param("max_iter", self.config.max_iter)

            # Save the model
            model_path = os.path.join(self.config.root_dir, self.config.model_name)
            joblib.dump(lr_model, model_path)

            # Log model artifact in MLflow
            mlflow.log_artifact(model_path)

            # Register the model in MLflow
            mlflow.sklearn.log_model(lr_model, "model", input_example=X_train_transformed[:5])
            mlflow.register_model(
                "runs:/" + mlflow.active_run().info.run_id + "/model", "MyLogisticRegressionModel" 
            )
            mlflow.set_tag("model_version", "v0.0.2")

        # End the MLflow run from the training 
        mlflow.end_run()

        # Logging info 
        logging.info(f"[Completed]: Model Trainer completed: Saved to {model_path}")
