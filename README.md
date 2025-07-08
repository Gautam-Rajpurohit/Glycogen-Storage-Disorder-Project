# Glycogen Storage Disorder (GSD) Prediction Model

A Machine Learning-based predictive model for early diagnosis of **Glycogen Storage Disease Type I (Von Gierke Disease)** using clinical parameters such as Blood Sugar, Uric Acid, Triglycerides, Cholesterol, Lactic Acid, and Liver Enzymes. This tool aims to support healthcare professionals in non-invasive, data-driven decision-making for early GSD detection.

---

## Introduction

Glycogen Storage Disease Type I (GSD I) is a **rare genetic disorder** that disrupts glucose metabolism due to enzyme deficiencies. It often leads to:

- Hepatomegaly (enlarged liver)
- Hypoglycemia
- Hyperlipidemia
- Hyperuricemia
- Growth retardation
- Neutrophil dysfunction (especially in GSD Ib)

### Motivation

Currently, diagnosis involves **invasive genetic testing or liver biopsies**, which are costly, complex, and often inaccessible. This project presents a **non-invasive ML-based approach** using key biochemical features to predict the presence of GSD.

---

## Problem Statement

To develop a Machine Learning model capable of accurately diagnosing **Glycogen Storage Disorder Type I** based on clinical test results, thereby aiding in early screening and treatment planning.

---

## Project Aim

- To build a reliable ML model for early detection of GSD Type I.
- To improve diagnostic accuracy via **SVM** with hyperparameter tuning.
- To compare ML results against known clinical patterns.

---

## Objectives

- Develop a robust classifier using biochemical test data.
- Perform feature scaling and model optimization.
- Evaluate and improve accuracy, precision, and generalization.
- Compare ML predictions with clinical benchmarks.

---

## Features Explained

- **Bilirubin** – Marker of liver dysfunction.
- **ALT / AST / ALP** – Liver enzymes; elevated in liver stress or inflammation.
- **Triglycerides & Cholesterol** – Elevated due to impaired glucose metabolism.
- **Uric Acid** – Increased in hyperuricemia caused by metabolic imbalance.
- **Lactic Acid** – High levels due to anaerobic metabolism in GSD I.

---

## Techniques & Methodology

1. **Dataset Creation**  
   • Manual dataset creation using lab test values.

2. **Data Preprocessing**  
   • Handling of noise, missing values.

3. **Feature Scaling**  
   • Z-score normalization for feature scaling.

4. **Model Training**  
   • Algorithm: Support Vector Machine (SVM)  
   • Hyperparameter Tuning: Kernel type, Regularization (C), Gamma  
   • Train-Test Split for performance evaluation.

---

## Why SVM?

Support Vector Machine (SVM) excels in:
- Handling small datasets.
- Managing non-linear boundaries via kernel tricks.
- Maximizing the decision boundary margin.
- Reducing overfitting with regularization.

---
