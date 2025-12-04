# 🚢 Titanic Survival Predictor

A beautiful, modern web application that predicts whether you would have survived the Titanic disaster using machine learning. Built with Flask and featuring an elegant ocean-themed design.

## 🌐 Live Demo

**Visit the live application:** [https://titanic-survival-predictor-1.onrender.com/](https://titanic-survival-predictor-1.onrender.com/)

## ✨ Features

- 🎨 **Beautiful ocean-themed interface** with animated backgrounds
- 🤖 **Machine Learning predictions** using Logistic Regression
- 📱 **Responsive design** that works on all devices
- 🎯 **Historically accurate model** reflecting real Titanic survival patterns
- 💫 **Smooth animations** and modern UI components
- 🚫 **No database required** - all processing in memory

## 🛠️ Technology Stack

- **Backend**: Flask (Python)
- **Machine Learning**: Scikit-learn (Logistic Regression)
- **Frontend**: HTML5, CSS3, JavaScript
- **Styling**: Custom CSS with animations and glass-morphism effects
- **Icons**: FontAwesome
- **Fonts**: Google Fonts (Playfair Display + Inter)
- **Deployment**: Render.com

## 📊 How It Works

The application uses a Logistic Regression model trained on historical Titanic data patterns:

### Input Features:
- **Passenger Class** (1st, 2nd, 3rd)
- **Gender** (Male/Female)
- **Age** 
- **Number of Siblings/Spouses aboard**
- **Number of Parents/Children aboard**
- **Ticket Fare** (predefined realistic options)

### Prediction Logic:
The model reflects historical survival patterns:
- Women and children had higher survival rates
- First-class passengers had better access to lifeboats
- Family relationships influenced survival chances

## 🏗️ Project Structure

```
flask-ml-demo/
├── app.py                          # Main Flask application
├── requirements.txt                # Python dependencies
├── static/
│   └── styles.css                  # Modern CSS with animations
├── templates/
│   └── index.html                  # Beautiful HTML interface
└── model/
    └── realistic_model.pkl         # Trained ML model
```

## 🚀 Local Development

### Prerequisites
- Python 3.7+
- pip

### Installation

1. **Clone the repository:**
```bash
git clone https://github.com/YarikVitovsky/titanic-survival-predictor.git
cd flask-ml-demo
```

2. **Create virtual environment:**
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. **Install dependencies:**
```bash
pip install -r requirements.txt
```

4. **Run the application:**
```bash
python app.py
```

5. **Open your browser:**
Visit `http://localhost:5000`

## 🎯 Usage

1. **Fill out the passenger information:**
   - Select your passenger class
   - Choose your gender
   - Enter your age
   - Specify family members aboard
   - Select a realistic ticket fare

2. **Click "Predict My Fate"**

3. **View your result:**
   - 🛟 **Survived**: Green card with life ring icon
   - ⚓ **Did not survive**: Red card with anchor icon

## 🎨 Design Features

- **Ocean-themed gradient background** with animated waves
- **Floating ship icon** with smooth animations
- **Glass-morphism cards** with blur effects
- **Modern typography** and professional spacing
- **Hover effects** and micro-interactions
- **Responsive grid layout** for all screen sizes
- **Smooth scrolling** to results

## 📈 Model Accuracy

The model is trained on realistic historical patterns that reflect:
- **92% survival rate** for first-class women
- **86% survival rate** for second-class women  
- **49% survival rate** for third-class women
- **37% survival rate** for first-class men
- **16% survival rate** for second-class men
- **13% survival rate** for third-class men

## 🚀 Deployment

The application is deployed on **Render.com** with:
- Automatic deployment from GitHub
- Built-in SSL certificates
- Global CDN
- Zero-downtime deployments

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test locally
5. Submit a pull request

## 📄 License

This project is open source and available under the MIT License.

## 👨‍💻 Author

Created by [YarikVitovsky](https://github.com/YarikVitovsky)

---

**Experience history through machine learning!** 🌊⚓
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