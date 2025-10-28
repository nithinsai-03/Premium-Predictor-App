import streamlit as st

# -----------------------------------------------------------
# Page Config
# -----------------------------------------------------------
st.set_page_config(page_title="SmartHealth Project Details", page_icon="📘", layout="wide")

# -----------------------------------------------------------
# Deep Black Futuristic Theme
# -----------------------------------------------------------
st.markdown("""
<style>
.stApp {
    background: radial-gradient(circle at 20% 20%, #000000, #030712 90%);
    color: #e0e0e0;
}

/* Title */
.title {
    font-size: 3rem;
    text-align: center;
    color: #00ffff;
    font-weight: 900;
    text-shadow: 0 0 30px #00ffff;
    letter-spacing: 1px;
    margin-bottom: 1rem;
}

/* Hero Section */
.hero {
    background: linear-gradient(145deg, rgba(0,255,255,0.1), rgba(0,0,0,0.8));
    border-radius: 25px;
    padding: 3rem 2rem;
    margin-bottom: 3rem;
    box-shadow: 0 0 40px rgba(0,255,255,0.15);
    text-align: center;
    backdrop-filter: blur(10px);
}
.hero h1 {
    font-size: 2.5rem;
    color: #00ffff;
    text-shadow: 0 0 25px #00ffff;
}
.hero p {
    color: #9ca3af;
    font-size: 1.2rem;
    margin-top: 0.5rem;
}

/* Stats Cards */
.stats-container {
    display: flex;
    justify-content: center;
    flex-wrap: wrap;
    gap: 1.8rem;
    margin-top: 2rem;
}
.stat-card {
    background: rgba(10, 10, 10, 0.85);
    border: 1px solid rgba(0,255,255,0.3);
    border-radius: 20px;
    padding: 1rem 2rem;
    text-align: center;
    box-shadow: 0 0 25px rgba(0,255,255,0.1);
    min-width: 180px;
    transition: 0.4s ease;
}
.stat-card:hover {
    transform: translateY(-6px);
    box-shadow: 0 0 25px rgba(0,255,255,0.5);
}
.stat-card h2 {
    color: #00ffff;
    margin-bottom: 0.4rem;
    font-size: 1.8rem;
}
.stat-card p {
    color: #d1d5db;
}

/* Section Box */
.section {
    background: rgba(10, 10, 10, 0.85);
    border-radius: 22px;
    padding: 2rem;
    margin-bottom: 2.5rem;
    border: 1px solid rgba(0,255,255,0.2);
    box-shadow: 0 0 35px rgba(0,255,255,0.1);
    backdrop-filter: blur(8px);
}
.section:hover {
    box-shadow: 0 0 45px rgba(0,255,255,0.25);
}
.section h3 {
    color: #00ffff;
    text-shadow: 0 0 12px #00ffff;
    margin-bottom: 0.8rem;
}
.section p, .section li {
    color: #d1d5db;
    font-size: 1rem;
    line-height: 1.7;
}

/* Horizontal Rule */
hr {
    border: none;
    border-top: 1px solid rgba(0,255,255,0.2);
    margin: 3rem 0;
}

/* Footer */
.footer {
    text-align: center;
    color: #9ca3af;
    font-size: 0.95rem;
    margin-top: 3rem;
}
.footer b {
    color: #00ffff;
}
</style>
""", unsafe_allow_html=True)

# -----------------------------------------------------------
# Hero Section
# -----------------------------------------------------------
st.markdown("""
<div class="hero">
    <h1>📘 SmartHealth Premium Predictor</h1>
    <p>AI-powered system predicting accurate health insurance premiums using real-world data.</p>
    <div class="stats-container">
        <div class="stat-card">
            <h2>98.2%</h2>
            <p>Accuracy (Young Group - Ridge)</p>
        </div>
        <div class="stat-card">
            <h2>96.4%</h2>
            <p>Accuracy (Rest Group - XGBoost)</p>
        </div>
        <div class="stat-card">
            <h2>50K+</h2>
            <p>Insurance Records</p>
        </div>
        <div class="stat-card">
            <h2>2</h2>
            <p>Trained ML Models</p>
        </div>
        <div class="stat-card">
            <h2>Real-Time</h2>
            <p>Interactive Prediction</p>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# -----------------------------------------------------------
# Project Overview
# -----------------------------------------------------------
st.markdown("""
<div class="section">
<h3>🧠 Project Overview</h3>
<p>
<b>SmartHealth Premium Predictor</b> leverages Machine Learning to estimate health insurance premiums based on 
user profiles. Trained on a dataset of 50,000+ individuals, it combines demographic, lifestyle, and medical 
factors to generate accurate predictions. 
The project aims to empower insurers and users alike with fast, data-driven premium estimation.
</p>
</div>
""", unsafe_allow_html=True)

# -----------------------------------------------------------
# Methodology
# -----------------------------------------------------------
st.markdown("""
<div class="section">
<h3>⚙️ Methodology</h3>
<p>The dataset underwent robust preprocessing including:</p>
<ul>
<li>Missing value imputation.</li>
<li>Outlier detection via IQR method.</li>
<li>Feature normalization and encoding.</li>
</ul>

<p>After cleaning, data was segmented into two age-based groups for optimized modeling:</p>
<ul>
<li><b>Young Group (&lt;30 years):</b> Ridge Regression model – accuracy <b>98.2%</b></li>
<li><b>Rest Group (≥30 years):</b> XGBoost model – accuracy <b>96.4%</b></li>
</ul>

<p>
Both models were trained using Scikit-learn and XGBoost, serialized with Joblib, and integrated 
into a Streamlit interface for real-time user predictions.
</p>
</div>
""", unsafe_allow_html=True)

# -----------------------------------------------------------
# Dataset
# -----------------------------------------------------------
st.markdown("""
<div class="section">
<h3>📊 Dataset Information</h3>
<ul>
<li>📁 <b>Records:</b> 50,000+</li>
<li>📋 <b>Features:</b> Age, Gender, BMI, Income, Region, Dependents, Smoking Status, etc.</li>
<li>🎯 <b>Target Variable:</b> Insurance Premium (₹)</li>
<li>🧹 <b>Cleaning:</b> Missing value handling, IQR-based outlier removal, scaling.</li>
</ul>
</div>
""", unsafe_allow_html=True)

# -----------------------------------------------------------
# Tech Stack
# -----------------------------------------------------------
st.markdown("""
<div class="section">
<h3>🧩 Tech Stack</h3>
<ul>
<li>💻 <b>Language:</b> Python</li>
<li>📚 <b>Libraries:</b> Pandas, NumPy, Scikit-learn, XGBoost, Joblib, Matplotlib</li>
<li>⚙️ <b>Framework:</b> Streamlit (real-time deployment)</li>
<li>🧠 <b>ML Models:</b> Ridge Regression, XGBoost Regressor</li>
</ul>
</div>
""", unsafe_allow_html=True)

# -----------------------------------------------------------
# Future Scope
# -----------------------------------------------------------
st.markdown("""
<div class="section">
<h3>🚀 Future Enhancements</h3>
<ul>
<li>Integrate wearable health data (Fitbit, Apple Health) for real-time premium adjustment.</li>
<li>Visualize model interpretability using SHAP & LIME for transparency.</li>
<li>Implement policy comparison dashboard across income groups.</li>
<li>Deploy globally using Streamlit Cloud / AWS EC2.</li>
<li>Introduce secure login and premium history analytics.</li>
</ul>
</div>
""", unsafe_allow_html=True)

# -----------------------------------------------------------
# Footer
# -----------------------------------------------------------
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<p class='footer'>💡 Designed & Developed by <b>Nithin Sai</b></p>", unsafe_allow_html=True)
