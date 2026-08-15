# 🏭 Industrial Decision Intelligence Platform (IDIP)

An AI-powered industrial predictive maintenance platform designed to analyze machine operating conditions, estimate failure probability, classify operational risk, and provide intelligent maintenance recommendations.

The project combines **Machine Learning, a cloud-hosted REST API, and an interactive web dashboard** to transform machine data into actionable maintenance decisions.

---

## 🌐 Live Demo

The platform is deployed and available online:

### 🔗 Live Website
https://shaikahalajmi.github.io/Industrial-Decision-Intelligence-Platform/

Users can enter machine operating parameters and receive an AI-generated failure probability, risk classification, machine status, and maintenance recommendation.

---

## 🎯 Project Objective

Unexpected equipment failures can lead to:

- Production downtime
- Increased maintenance costs
- Operational disruptions
- Reduced equipment availability

The objective of IDIP is to demonstrate how **Machine Learning and predictive analytics** can support industrial maintenance decisions by identifying potential machine failure risks from operational data.

---

## 🤖 Machine Learning Analysis

The system analyzes several machine operating parameters:

- Machine Type
- Air Temperature (K)
- Process Temperature (K)
- Rotational Speed (rpm)
- Torque (Nm)
- Tool Wear (min)

These parameters are sent to the trained Machine Learning model through the backend API.

The model then estimates the probability of machine failure.

---

## ✨ Key Features

### 🧠 AI Machine Analysis
Users can enter machine operating parameters and run an AI-powered failure analysis.

### 📊 Failure Probability
The system calculates and displays the estimated probability of machine failure.

### ⚠️ Risk Classification
Prediction results are translated into understandable operational risk levels.

### ⚙️ Machine Status
The platform converts model predictions into machine conditions such as:

- NORMAL
- CAUTION
- WARNING

### 🔧 Maintenance Recommendations
The system provides an operational recommendation based on the predicted machine condition.

### 📈 Interactive Dashboard
Prediction results are displayed through an industrial-style monitoring dashboard with dynamic indicators and visualizations.

### 📋 History & Reports
Previous machine analyses can be viewed through the History section.

### 🧠 Machine Intelligence
Operating parameters are presented with additional context to help interpret machine conditions.

### 🚨 Alerts
The platform generates operational alerts when selected machine parameters or risk levels require attention.

---

## ⚙️ How It Works

The platform follows this workflow:

1. The user enters machine operating parameters.
2. The web dashboard collects the input values.
3. JavaScript sends the machine data to the backend through a REST API.
4. The Flask backend receives and processes the request.
5. The trained Machine Learning model analyzes the machine conditions.
6. The model returns the estimated failure probability.
7. The platform classifies the operational risk.
8. The dashboard displays the prediction and maintenance recommendation.

---

## 🏗️ System Architecture

```text
Machine Operating Data
        ↓
Interactive Web Dashboard
        ↓
JavaScript API Request
        ↓
Flask REST API
        ↓
Machine Learning Model
        ↓
Failure Probability
        ↓
Risk Classification
        ↓
Maintenance Recommendation
        ↓
Interactive Decision Dashboard
