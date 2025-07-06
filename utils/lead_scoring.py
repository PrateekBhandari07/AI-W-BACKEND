def score_leads(df):
    if df is None:
        return {"error": "No data provided for lead scoring"}

    # Dummy scoring: assign score = 50 for all rows
    df['lead_score'] = 50

    return {
        "message": "Lead scoring completed",
        "rows_scored": len(df),
        "sample_scores": df[['lead_score']].head().to_dict(orient="records")
    }
