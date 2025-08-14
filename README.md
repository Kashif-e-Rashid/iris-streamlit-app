🌸 Iris Flower Prediction App

A simple Streamlit web application that predicts the species of an Iris flower (Setosa, Versicolor, or Virginica) based on sepal and petal measurements.

📌 Features

User-friendly sliders for entering flower measurements

Instant prediction using a trained Random Forest Classifier

Pre-trained model based on the classic Iris dataset

Works locally or can be deployed for free on Streamlit Cloud

🛠 Installation & Local Run

Clone the repository

git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name


Install dependencies

pip install -r requirements.txt


Run the app

streamlit run app.py


View in browser
Streamlit will open a tab automatically at

http://localhost:8501

🚀 Deployment on Streamlit Cloud

Push your project to a GitHub repository.

Go to Streamlit Cloud and sign in with GitHub.

Click New App → select your repo and branch.

Set the main file to app.py.

Click Deploy — your app will be live in seconds!

📂 Project Structure
.
├── app.py                  # Streamlit frontend & backend
├── iris_model.joblib        # Trained Random Forest model
├── train_model.py           # Script to train and save model
├── requirements.txt         # Python dependencies
└── README.md                # Project documentation

📊 Model Details

Algorithm: Random Forest Classifier

Dataset: Iris dataset from scikit-learn

Accuracy: ~100% on test data

📜 License

This project is open-source and available under the MIT License.
