import shap
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

class SHAPExplainer:
    def __init__(self):
        self.model = None
        self.explainer = None

    def train(self, df: pd.DataFrame, target: str):
        X = df.drop(columns=[target])
        y = df[target]
        self.model = RandomForestClassifier(n_estimators=100, random_state=42)
        self.model.fit(X, y)
        self.explainer = shap.TreeExplainer(self.model)
        return X

    def explain(self, X: pd.DataFrame):
        if self.explainer is None:
            raise Exception("Model not trained yet")

        shap_values = self.explainer.shap_values(X)[1]  # Assuming binary classification
        explanations = []

        for i in range(min(5, len(X))):  # Just explain first 5 rows
            row = {}
            for j, col in enumerate(X.columns):
                row[col] = shap_values[i][j]
            explanations.append(row)

        return explanations
