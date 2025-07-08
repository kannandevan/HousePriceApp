# House Price Prediction AI 🏠💸

This is a simple and fun machine learning project that predicts house prices based on various features. It's a great starting point for anyone new to AI, machine learning, and web development!

The app uses a Linear Regression model trained on the USA Housing dataset to make predictions. The user can input house details through a simple web interface and get an instant price prediction.

### ✨ Features

* **AI-Powered Predictions:** Uses a real machine learning model to predict house prices.
* **Interactive Web Interface:** A user-friendly web form built with Flask to input data.
* **Data Visualization:** Displays a graph showing the relationship between area income and house price.
* **Easy to Understand:** The code is well-commented and structured for beginners.

### 🛠️ Tech Stack

* **Backend:** Python, Flask
* **Machine Learning:** Scikit-learn
* **Data Handling:** Pandas
* **Plotting:** Matplotlib & Seaborn
* **Frontend:** Basic HTML & CSS

### ⚙️ How It Works

The project is divided into two main parts:

1.  **Model Training (`train_model.py`):**
    * The script loads the `USA_Housing.csv` dataset.
    * It separates the data into features (like income, house age, number of rooms) and the target (the price).
    * A Linear Regression model is trained on this data.
    * The trained model is saved as `house_price_model.pkl`.
    * A graph visualizing the data is created and saved as an image.

2.  **Web Application (`app.py`):**
    * The Flask app loads the pre-trained `house_price_model.pkl`.
    * It displays an HTML page (`index.html`) with a form for the user.
    * When the user submits the form, the app takes the input, feeds it to the model, and gets a prediction.
    * The predicted price is then displayed back to the user on the web page.

### 🚀 Setup and Installation

To run this project on your local machine, follow these steps:

**1. Clone the Repository (or download the files):**
```bash
git clone [https://github.com/kannandevan/HousePriceApp.git](https://github.com/kannandevan/HousePriceApp.git)
cd HousePriceApp
```

**2. Create a Virtual Environment (Recommended):**
```bash
# For Windows
python -m venv venv
venv\Scripts\activate

# For macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

**3. Install the Required Libraries:**
All the necessary libraries are listed in the `requirements.txt` file. You can install them all with one command.
```bash
pip install -r requirements.txt
```
*(Note: If you don't have a `requirements.txt` file, you can install the libraries manually: `pip install pandas scikit-learn Flask matplotlib seaborn`)*

### ▶️ How to Run the App

**Step 1: Train the Model**
First, you need to run the training script to generate the model file (`.pkl`) and the graph.
```bash
python train_model.py
```
This will create `house_price_model.pkl` and `static/income_vs_price.png`.

**Step 2: Run the Flask Web App**
Now, start the web server.
```bash
python app.py
```

**Step 3: View the App in Your Browser**
Open your web browser and go to the following address:
```
[http://127.0.0.1:5000](http://127.0.0.1:5000)
```
You should now see the application running! Fill in the form to get your first house price prediction.

### 📂 Project Folder Structure

```
HousePriceApp/
├── static/
│   └── income_vs_price.png
├── templates/
│   └── index.html
├── app.py
├── train_model.py
├── house_price_model.pkl
├── USA_Housing.csv
└── README.md