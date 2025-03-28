import os
import joblib
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from mlProject.entity.config_entity import ModelTrainerConfig 


class ModelTrainer:
    def __init__(self, config: ModelTrainerConfig):
        self.config = config

    def train(self):
        #print("🟢 Starting model training...")  # Debugging step

        # Load training & testing data
        train_data = pd.read_csv(self.config.train_data_path)
        test_data = pd.read_csv(self.config.test_data_path)
        #print("✅ Data loaded successfully!")

        # Prepare input and target variables
        train_x = train_data.drop([self.config.target_column], axis=1)
        test_x = test_data.drop([self.config.target_column], axis=1)
        train_y = train_data[[self.config.target_column]]
        test_y = test_data[[self.config.target_column]]
        #print("✅ Data preprocessing completed!")

        # Initialize and train the RandomForest model
        rf = RandomForestRegressor(
            n_estimators=self.config.n_estimators,
            min_samples_split=self.config.min_samples_split,
            min_samples_leaf=self.config.min_samples_leaf,
            max_features=self.config.max_features,
            max_depth=self.config.max_depth,
            bootstrap=self.config.bootstrap,
            random_state=self.config.random_state
        )

        #print("🚀 Training model...")
        rf.fit(train_x, train_y.values.ravel())  # Flatten y for sklearn
        #print("✅ Model training completed!")

        # Ensure the directory exists before saving
        os.makedirs(self.config.root_dir, exist_ok=True)

        # Define model path
        model_path = os.path.join(self.config.root_dir, self.config.model_name + ".joblib")
        #print(f"💾 Saving model at: {model_path}")

        # Save the trained model
        joblib.dump(rf, model_path)

        

  