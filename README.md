# Project_Fastapi
Smart Text Classifier (FastAPI + Machine Learning)

A Machine Learning–powered Text Classification API that classifies business-related text queries into one of the following categories:
Technical
Billing
General
The project uses TF-IDF + Logistic Regression for text classification and exposes predictions through a FastAPI REST API.

Project Overview
Businesses often receive large volumes of user queries such as:
Payment issues
Login or technical problems
General information requests
This project automatically classifies such text queries so they can be:
Routed to the correct support team
Analyzed for trends
Integrated into chatbots or ticketing systems

Tech Stack
Python
Scikit-learn – Machine Learning
Pandas – Data handling
FastAPI – API framework
Uvicorn – ASGI server
Joblib – Model serialization

Project Structure
Smart_Text_Classifier/
│
├── dataset.csv           # Training dataset

├── train_model.py        # Model training & evaluation

├── model.pkl             # Saved trained model

├── api.py                # FastAPI application

├── requirements.txt      # Dependencies

└── README.md             # Project documentation

Model Training
train_model.py
This script:
Loads the dataset
Splits data into train/test
Applies TF-IDF vectorization
Trains Logistic Regression model
Evaluates accuracy and metrics
Saves the trained model as model.pkl

Run Training
python train_model.py

FastAPI Application
📄 api.py
The API exposes a /predict endpoint that:
Accepts input text
Returns the predicted category

Start the server
python -m unicorn api:app --reload

Server will run at:
http://127.0.0.1:8000

