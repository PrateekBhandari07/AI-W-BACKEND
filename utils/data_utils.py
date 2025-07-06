import pandas as pd
import io
import json

def parse_uploaded_file(contents: bytes, filename: str) -> pd.DataFrame:
    if filename.endswith(".csv"):
        return pd.read_csv(io.BytesIO(contents))
    elif filename.endswith(".json"):
        json_data = json.loads(contents.decode("utf-8"))
        return pd.DataFrame(json_data)
    else:
        raise ValueError("Unsupported file type")
