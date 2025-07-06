def check_bias(df):
    if df is None:
        return {"error": "No data provided for bias check"}

    # Dummy bias check: just return column distributions
    bias_report = {}
    for col in df.columns:
        bias_report[col] = df[col].value_counts(normalize=True).head(5).to_dict()

    return {
        "message": "Bias check completed",
        "bias_report": bias_report
    }
