# OptiSupply-AI
### Predictive Inventory & Demand Forecasting using Machine Learning

OptiSupply AI is a predictive analytics tool designed to help businesses optimize their inventory levels. By leveraging historical sales data and identifying patterns like seasonality (weekends vs. weekdays) and yearly trends, the system predicts the quantity of stock required for any given day of the year.

---

## 🚀 Features
* **Automated Data Generation:** Custom script to simulate realistic retail sales patterns.
* **Machine Learning Pipeline:** Utilizes a **Random Forest Regressor** to learn complex demand patterns.
* **Real-time Dashboard:** Interactive UI built with **Streamlit** for instant stock predictions.
* **Model Persistence:** Uses `joblib` for efficient model saving and loading.

---

## 🛠️ Tech Stack
* **Language:** Python 3.12+
* **ML Libraries:** Scikit-Learn, Pandas, NumPy
* **Interface:** Streamlit
* **Serialization:** Joblib

---

## 📂 Project Structure
```text
.
├── data_gen.py        # Generates synthetic sales data (CSV)
├── model_trainer.py   # Processes data and trains the RandomForest model
├── app.py             # Streamlit web application interface
├── requirements.txt   # Project dependencies
└── demand_model.pkl   # Pre-trained model (generated after training)
⚙️ Installation & Usage
1. Clone the repository

Bash
git clone [https://github.com/neetamaan20-cloud/OptiSupply-AI.git](https://github.com/neetamaan20-cloud/OptiSupply-AI.git)
cd OptiSupply-AI
2. Set up a Virtual Environment (macOS)

Bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
3. Run the Pipeline

First, generate the data and train the model:

Bash
python3 data_gen.py
python3 model_trainer.py
Then, launch the interactive dashboard:

Bash
streamlit run app.py
📊 How it Works
Feature Engineering: The model extracts the day_of_year and day_of_week from the raw date.

Training: A Random Forest model is trained to recognize that demand spikes significantly on weekends and shows a steady growth trend over time.

Inference: The user selects a date via the slider, and the model provides a quantitative estimate of units needed.
