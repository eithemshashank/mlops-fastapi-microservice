import joblib
import pandas as pd
from pydantic import BaseModel
from src.core.config import settings


class PredictionInput(BaseModel):
    features: dict


class PredictionService:
    def __init__(self):
        self.model = joblib.load(settings.MODEL_PATH)

    def predict(self, input_data: PredictionInput):
        # Get the feature order used when the model was trained
        expected_features = list(self.model.feature_names_in_)

        # Build the DataFrame using the model's expected feature order
        df = pd.DataFrame([input_data.features])
        df = df.reindex(columns=expected_features)

        return self.model.predict(df)
