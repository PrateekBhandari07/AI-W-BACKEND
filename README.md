# BlindSpot: Ethical AI Marketing Platform – Backend

The **BlindSpot Backend** powers the Ethical AI Marketing Platform, enabling organizations to analyze marketing datasets ethically and transparently. It validates, cleans, and processes uploaded datasets, generates lead scores using explainable AI (SHAP), and runs fairness checks to identify and mitigate biases in your campaigns.

Built with **FastAPI**, this backend ensures your marketing decisions remain ethical, compliant, and data-driven, while seamlessly integrating with the BlindSpot frontend for a complete ethical marketing workflow.

---

## 🧠 Features

✅ FastAPI-based REST APIs  
✅ CSV/JSON data upload and validation  
✅ SHAP explainability for models  
✅ Anomaly and bias detection  
✅ Fairness checks using Fairlearn  
✅ Lead scoring and insights generation  
✅ Seamless integration with the BlindSpot frontend

---

## ⚙️ Tech Stack

- **Python 3.9+**
- **FastAPI**, **Uvicorn**
- **Pandas**, **Scikit-learn**, **XGBoost**
- **SHAP**, **Fairlearn**
- **Pydantic** for validation

---

## 🚀 Getting Started
```bash
### 1 Clone the repository
git clone https://github.com/PrateekBhandari07/HWI-BACKEND.git
cd AI-W-BACKEND


2. Create virtual environment
python3 -m venv .venv
source .venv/bin/activate

3. Install dependencies
pip install -r requirements.txt

4. Start FastAPI server
uvicorn main:app --reload
Backend runs on: http://localhost:8000
```
##🚀 Deployment
This backend is deployed on Render for scalable, production-grade API hosting, ensuring fast, reliable, and secure integration with your frontend workflows.

To deploy on Render:

1️⃣ Create a new Web Service in Render.
2️⃣ Connect your GitHub repository (HWI-BACKEND).
3️⃣ Set the Start Command:

uvicorn main:app --host 0.0.0.0 --port $PORT


---


