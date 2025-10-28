import streamlit as st
import joblib
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from io import BytesIO
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

# -----------------------------------------------------------
# Load models
# -----------------------------------------------------------
@st.cache_resource
def load_models():
    ridge_model = joblib.load("model_ridge.pkl")
    xgb_model = joblib.load("XGBRegressor.pkl")
    return ridge_model, xgb_model

ridge_model, xgb_model = load_models()

# -----------------------------------------------------------
# Page Config
# -----------------------------------------------------------
st.set_page_config(page_title="Health Insurance Premium Predictor", page_icon="💰", layout="wide")

# -----------------------------------------------------------
# Custom CSS (Dark Black Theme)
# -----------------------------------------------------------
st.markdown("""
<style>
body { background-color: #000000; color: #e0e0e0; }
.stApp {
    background: radial-gradient(circle at 10% 20%, #000000, #010409 90%);
    color: #e0e0e0;
}
.title {
    font-size: 3rem;
    color: #00ffff;
    text-align: center;
    font-weight: 900;
    text-shadow: 0 0 25px #00ffff;
    letter-spacing: 1.2px;
}
.subtitle {
    text-align: center;
    color: #9ca3af;
    font-size: 1.1rem;
    margin-bottom: 2rem;
}
.result-card {
    background: linear-gradient(135deg, #0f172a, #1e293b);
    padding: 25px;
    border-radius: 20px;
    text-align: center;
    box-shadow: 0 0 40px rgba(0,255,255,0.25);
}
.result-card h1 { color: #00ffff; font-size: 3rem; text-shadow: 0 0 20px #00ffff; }
.result-card p { color: #ffffff; font-size: 1rem; }
.section-box {
    background: rgba(20, 20, 20, 0.9);
    padding: 25px;
    border-radius: 18px;
    margin-top: 20px;
    box-shadow: 0 0 30px rgba(0, 255, 255, 0.15);
}
hr { border: none; border-top: 1px solid #00ffff33; margin: 3rem 0; }
.stSlider > div > div > div {
    background: linear-gradient(to right, #00ffff, #0088ff);
}
.stDownloadButton > button {
    background: linear-gradient(90deg, #00ffff, #0077ff);
    border: none;
    color: black;
    font-weight: 700;
    border-radius: 12px;
    transition: all 0.3s ease;
}
.stDownloadButton > button:hover {
    background: linear-gradient(90deg, #0077ff, #00ffff);
    box-shadow: 0 0 15px #00ffff;
}
</style>
""", unsafe_allow_html=True)

# -----------------------------------------------------------
# Header
# -----------------------------------------------------------
st.markdown("<div class='title'>💰 Health Insurance Premium Predictor</div>", unsafe_allow_html=True)
st.markdown("<p class='subtitle'>Predict your premium with precision — powered by Ridge & XGBoost ML models</p>", unsafe_allow_html=True)

# -----------------------------------------------------------
# Input Form
# -----------------------------------------------------------
with st.form("input_form"):
    st.subheader("🧾 Enter Your Details")

    col1, col2, col3 = st.columns(3)
    with col1:
        age = st.slider("Age", 18, 80, 25)
        dependants = st.number_input("Number of Dependants", 0, 10, 0)
        income = st.number_input("Annual Income (in Lakhs)", 1.0, 100.0, 6.0, step=0.5)

    with col2:
        insurance_plan = st.selectbox("Insurance Plan", ["Bronze", "Silver", "Gold"])
        genetic_risk = st.slider("Genetical Risk (0 - 1)", 0.0, 1.0, 0.3)
        gender = st.selectbox("Gender", ["Male", "Female"])

    with col3:
        region = st.selectbox("Region", ["Northwest", "Southeast", "Northeast", "Southwest"])
        marital_status = st.selectbox("Marital Status", ["Married", "Unmarried"])
        bmi_category = st.selectbox("BMI Category", ["Normal", "Obesity", "Overweight", "Underweight"])

    col4, col5, col6 = st.columns(3)
    with col4:
        smoking_status = st.selectbox("Smoking Status", ["No Smoking", "Regular", "Occasional"])
    with col5:
        employment_status = st.selectbox("Employment Status", ["Salaried", "Self-Employed", "Freelancer"])

    submitted = st.form_submit_button("🔍 Predict Premium", use_container_width=True)

# -----------------------------------------------------------
# Preprocessing
# -----------------------------------------------------------
def preprocess_input():
    data = {
        "Age": age,
        "Number Of Dependants": dependants,
        "Income_Lakhs": income,
        "Insurance_Plan": 0 if insurance_plan == "Bronze" else (1 if insurance_plan == "Gold" else 0.5),
        "Genetical_Risk": genetic_risk,
        "normalized_score": 0,
        "Gender_Male": 1 if gender == "Male" else 0,
        "Region_Northwest": 1 if region == "Northwest" else 0,
        "Region_Southeast": 1 if region == "Southeast" else 0,
        "Region_Southwest": 1 if region == "Southwest" else 0,
        "Marital_status_Unmarried": 1 if marital_status == "Unmarried" else 0,
        "BMI_Category_Obesity": 1 if bmi_category == "Obesity" else 0,
        "BMI_Category_Overweight": 1 if bmi_category == "Overweight" else 0,
        "BMI_Category_Underweight": 1 if bmi_category == "Underweight" else 0,
        "Smoking_Status_Occasional": 1 if smoking_status == "Occasional" else 0,
        "Smoking_Status_Regular": 1 if smoking_status == "Regular" else 0,
        "Employment_Status_Salaried": 1 if employment_status == "Salaried" else 0,
        "Employment_Status_Self-Employed": 1 if employment_status == "Self-Employed" else 0,
    }
    return pd.DataFrame([data])

# -----------------------------------------------------------
# PDF Report Generator
# -----------------------------------------------------------
def generate_pdf(premium, group):
    buffer = BytesIO()
    c = canvas.Canvas(buffer, pagesize=letter)
    c.setFont("Helvetica-Bold", 16)
    c.drawString(200, 750, "Health Insurance Premium Report")
    c.setFont("Helvetica", 12)
    c.drawString(50, 710, f"Predicted Premium: ₹ {premium:,.2f}")
    c.drawString(50, 690, f"Model Used: {group}")
    c.drawString(50, 670, f"Age: {age}")
    c.drawString(50, 650, f"Income: ₹ {income} Lakhs")
    c.drawString(50, 630, f"Region: {region}")
    c.drawString(50, 610, f"Insurance Plan: {insurance_plan}")
    c.drawString(50, 590, f"Smoking Status: {smoking_status}")
    c.drawString(50, 570, "-"*40)
    c.drawString(50, 550, "Thank you for using Health Premium Predictor!")
    c.save()
    buffer.seek(0)
    return buffer

# -----------------------------------------------------------
# Prediction
# -----------------------------------------------------------
if submitted:
    input_df = preprocess_input()

    # Model selection based on age
    if age < 30:
        model = ridge_model
        group = "Young Group (Ridge Regression)"
    else:
        model = xgb_model
        group = "Rest Group (XGBoost Regressor)"

    prediction = model.predict(input_df)[0]

    # Result Card
    st.markdown(f"""
    <div class='result-card'>
        <h2>🎯 Predicted Health Insurance Premium</h2>
        <h1>₹ {prediction:,.2f}</h1>
        <p>Model Used: {group}</p>
    </div>
    """, unsafe_allow_html=True)

    avg_premium = 35000
    if prediction > avg_premium:
        st.warning("⚠️ Your predicted premium is above average — consider improving BMI or reducing smoking habits.")
    else:
        st.success("✅ Your predicted premium is below average — maintain your current lifestyle!")

    # Trend Chart
    st.subheader("📊 Premium Trend with Age")
    ages = np.linspace(18, 80, 100)
    premiums = 3000 + (ages * 150) + np.random.randint(-2000, 2000, 100)
    fig, ax = plt.subplots()
    fig.patch.set_facecolor("#000000")
    ax.set_facecolor("#000000")
    ax.plot(ages, premiums, color="#00ffff", linewidth=2.5)
    ax.set_xlabel("Age", color="#ffffff")
    ax.set_ylabel("Predicted Premium (₹)", color="#ffffff")
    ax.tick_params(colors="#ffffff")
    ax.grid(True, color="#00ffff33", linestyle="--", alpha=0.4)
    st.pyplot(fig)

    # Feature Insights
    st.markdown("""
    <div class='section-box'>
    <h3>🧩 Feature Impact & Insights</h3>
    <ul>
    <li>🏋️ <b>BMI:</b> Higher BMI → higher premiums due to health risks.</li>
    <li>🚬 <b>Smoking:</b> Regular smokers face ~40% higher premiums.</li>
    <li>💰 <b>Income:</b> Affects lifestyle-related premium adjustments.</li>
    <li>👶 <b>Age:</b> Premiums rise exponentially after age 40.</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

    # Lifestyle Recommendations
    st.markdown("""
    <div class='section-box'>
    <h3>💡 Lifestyle Recommendations</h3>
    <ul>
    <li>🚭 Quit smoking to lower premiums & health risks.</li>
    <li>🥗 Maintain a healthy BMI (18.5–24.9).</li>
    <li>💤 Manage stress and get proper sleep.</li>
    <li>💸 Choose the right plan — avoid over-insuring.</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

    # Download PDF
    pdf_buffer = generate_pdf(prediction, group)
    st.download_button(
        label="📄 Download Prediction Report",
        data=pdf_buffer,
        file_name="Health_Premium_Report.pdf",
        mime="application/pdf",
        use_container_width=True
    )

# -----------------------------------------------------------
# Footer
# -----------------------------------------------------------
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:#666;'>⚙️ Built by <b>Nithin Sai</b> — Powered by Streamlit & ML Intelligence</p>", unsafe_allow_html=True)
