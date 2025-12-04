# Flask Machine Learning Demo

This project is a Flask web application that serves a trained Logistic Regression model for predicting outcomes based on user input. The model is trained on the Titanic dataset and allows users to interact with the model through a web interface.

## Project Structure

```
flask-ml-demo
├── app
│   ├── __init__.py
│   ├── routes.py
│   ├── static
│   │   └── styles.css
│   └── templates
│       └── index.html
├── model
│   └── logistic_regression_model.pkl
├── data
│   ├── X_train.csv
│   ├── X_val.csv
│   ├── y_train.csv
│   └── y_val.csv
├── requirements.txt
├── app.py
└── README.md
```

## Setup Instructions

1. **Clone the repository**:
   ```
   git clone <repository-url>
   cd flask-ml-demo
   ```

2. **Create a virtual environment** (optional but recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required packages**:
   ```
   pip install -r requirements.txt
   ```

4. **Run the application**:
   ```
   python app.py
   ```

5. **Access the web application**:
   Open your web browser and go to `http://127.0.0.1:5000`.

## Usage

- The main page will allow you to input the features required by the model.
- After submitting the form, the application will display the prediction results based on the trained model.

## Dependencies

- Flask
- scikit-learn
- pandas
- joblib

## License

This project is licensed under the MIT License.