def explain_model(df):
    if df is None:
        return {"error": "No data provided for explanation"}

    # For hackathon/demo, generate a simple explanation:
    # Count unique values per column as a "pseudo-explanation".
    explanation = {}
    for col in df.columns:
        explanation[col] = {
            "unique_values": df[col].nunique(),
            "sample_values": df[col].dropna().unique()[:5].tolist()
        }

    return {
        "message": "Explanation generated successfully",
        "explanation": explanation
    }
