from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
from utils.shap_explainer import SHAPExplainer
from utils.data_utils import parse_uploaded_file
from utils.explainability import explain_model
from utils.fairness import check_bias
from utils.compliance import run_compliance_scan
from utils.ethics import suggest_ethics
from utils.lead_scoring import score_leads

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

data_store = {"df": None}

explainer = SHAPExplainer()
trained_features = None


@app.get("/")
def read_root():
    return {"message": "Hello, EPSILON FastAPI running!"}

# @app.post("/upload")
# async def upload_data(file: UploadFile = File(...)):
#     contents = await file.read()
#     df = parse_uploaded_file(contents, file.filename)
#     if df is None or df.empty:
#         return {"error": "Invalid or empty file"}
#     data_store["df"] = df
#     return {
#         "message": "File processed",
#         "rows": len(df),
#         "columns": list(df.columns),
#         "sample": df.head().to_dict(orient="records")
#     }

# @app.post("/upload")
# async def upload_data(file: UploadFile = File(...)):
#     contents = await file.read()
#     df = parse_uploaded_file(contents, file.filename)
#     if df is None or df.empty:
#         return {"error": "Invalid or empty file"}
#     data_store["df"] = df
#     return {
#         "message": "File processed",
#         "rows": len(df),
#         "columns": list(df.columns),
#         "sample": df.head().to_dict(orient="records")
#     }


@app.post("/upload")
async def upload_data(file: UploadFile = File(...)):
    contents = await file.read()
    df = parse_uploaded_file(contents, file.filename)
    if df is None or df.empty:
        return {"error": "Invalid or empty file"}
    data_store["df"] = df
    return {
    "message": "File processed",
    "rows": len(df),
    "columns": list(df.columns),
    "sample": df.head().to_dict(orient="records"),
    "fullData": df.to_dict(orient="records")  # Add this
}



@app.post("/train-model")
def train_model():
    df = data_store["df"]
    if df is None:
        return {"error": "No data uploaded"}
    global trained_features
    trained_features = explainer.train(df, target="target")  # Make sure target column is named 'target'
    return {"message": "Model trained"}


# ✅ SHAP Explanation Route
@app.get("/shap")
def get_shap_values():
    if trained_features is None:
        return {"error": "Model not trained"}

    shap_data = explainer.explain(trained_features)

    # Check if returned as list of SHAP values
    if isinstance(shap_data, list) and len(shap_data) > 0:
        # Assume mean SHAP across rows
        shap_values_mean = np.mean(np.abs(shap_data), axis=0)

        # Get feature names
        if hasattr(trained_features, 'columns'):
            feature_names = trained_features.columns
        else:
            feature_names = [f"Feature {i}" for i in range(len(shap_values_mean))]

        shap_summary = dict(zip(feature_names, shap_values_mean))
        sorted_summary = dict(sorted(shap_summary.items(), key=lambda x: -abs(x[1]))[:8])

        return {"explanations": sorted_summary}
    else:
        return {"error": "SHAP explanation failed or returned empty."}



@app.get("/lead-scores")
def get_lead_scores():
    df = data_store["df"]
    if df is None:
        return {"error": "No data uploaded"}
    return score_leads(df)

@app.get("/explain")
def get_explanations():
    df = data_store["df"]
    if df is None:
        return {"error": "No data uploaded"}
    return explain_model(df)

@app.get("/bias")
def get_bias_report():
    df = data_store["df"]
    if df is None:
        return {"error": "No data uploaded"}
    return check_bias(df)

@app.get("/compliance")
def get_compliance_report():
    df = data_store["df"]
    if df is None:
        return {"error": "No data uploaded"}
    return run_compliance_scan(df)

@app.get("/ethics")
def get_ethical_suggestions():
    df = data_store["df"]
    if df is None:
        return {"error": "No data uploaded"}
    return suggest_ethics(df)
