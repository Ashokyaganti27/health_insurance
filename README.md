# 🏥 Health Insurance Cross Sell Prediction

## 📌 project Overview--

This project aims to build a machine learning pipeline to predict whether a customer is likely to purchase vehicle insurance based on various features like age, driving license status, vehicle age, and more.These is Binary classification Problem

## ✅ Current Progress

## Data ingestion Pipeline completed

- Connected securely to Kaggle API for dataset access.
- Automated the data download and storage process using a Python script.
- Implemented basic exception handling and logging for traceability.
- Stored the raw dataset under a dedicated versioned path: `artifacts/data/raw/`.

## Data validation Pipeline completed

## Key Checks Performed

- Validated column names match the expected schema.

- Ensured column order is consistent with training schema.

- Verified data types of each column (e.g., int64, object, etc.).

- Checked both train and test datasets.

- Gives True if Success Otherwise False.

## Data Transformation Pipeline Completed

- Encoded categorical variables like Gender, Vehicle_Damage, Vehicle_Age.

- Applied StandardScaler to numeric features for better model behavior.

- Maintained original feature structure after transformation.

- Saved clean, processed train and test datasets under artifacts/data/processed/.

## Mdodel Training Pipeline Completed

- Trained  decision Tree classifier model on Train data

- Dumped model into artifacts/model_trainer/model.joblib using joblib

## 📂 Data Source

- [Kaggle: Health Insurance Cross Sell Prediction](https://www.kaggle.com/competitions/health-insurance-cross-sell-prediction)

---

## 👤 Author

**Ashok**  
Aspiring Data Scientist working on real-world, end-to-end projects with an  curiosity on building production-grade ML systems from scratch.

---
