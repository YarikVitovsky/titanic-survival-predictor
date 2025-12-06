"""
Create a working Titanic survival prediction model based on historical patterns
"""
import pickle
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
import pandas as pd

# Create synthetic training data based on known Titanic survival patterns
np.random.seed(42)

# Generate synthetic data that reflects historical survival patterns
n_samples = 1000

# Features: [pclass, age, sibsp, parch, fare, sex_male]
# Historical patterns:
# - Women had ~74% survival rate
# - Men had ~19% survival rate  
# - 1st class: 63% survival
# - 2nd class: 47% survival
# - 3rd class: 24% survival
# - Children had higher survival rates

data = []
labels = []

for i in range(n_samples):
    # Generate passenger class (1, 2, or 3)
    pclass = np.random.choice([1, 2, 3], p=[0.3, 0.25, 0.45])
    
    # Generate gender (0=female, 1=male)
    sex_male = np.random.choice([0, 1], p=[0.35, 0.65])
    
    # Generate age (children more likely to survive)
    if np.random.random() < 0.15:  # 15% children
        age = np.random.uniform(1, 16)
    else:
        age = np.random.uniform(17, 80)
    
    # Generate family size
    sibsp = np.random.choice([0, 1, 2, 3, 4], p=[0.6, 0.2, 0.1, 0.05, 0.05])
    parch = np.random.choice([0, 1, 2, 3, 4], p=[0.7, 0.15, 0.1, 0.03, 0.02])
    
    # Generate fare based on class
    if pclass == 1:
        fare = np.random.uniform(80, 250)
    elif pclass == 2:
        fare = np.random.uniform(20, 80)
    else:
        fare = np.random.uniform(5, 30)
    
    # Determine survival based on historical patterns
    survival_prob = 0.1  # base survival rate
    
    # Gender effect (strongest predictor)
    if sex_male == 0:  # female
        survival_prob += 0.6
    else:  # male
        survival_prob += 0.1
    
    # Class effect
    if pclass == 1:
        survival_prob += 0.3
    elif pclass == 2:
        survival_prob += 0.15
    
    # Age effect (children and young adults)
    if age < 16:
        survival_prob += 0.2
    elif age < 30:
        survival_prob += 0.1
    elif age > 60:
        survival_prob -= 0.1
    
    # Family size effect (small families had better chances)
    family_size = sibsp + parch
    if family_size == 0:
        survival_prob -= 0.05  # traveling alone
    elif 1 <= family_size <= 3:
        survival_prob += 0.05  # small family
    else:
        survival_prob -= 0.1   # large family
    
    # Ensure probability is in valid range
    survival_prob = max(0.05, min(0.95, survival_prob))
    
    # Generate survival label
    survived = 1 if np.random.random() < survival_prob else 0
    
    data.append([pclass, age, sibsp, parch, fare, sex_male])
    labels.append(survived)

# Convert to numpy arrays
X = np.array(data)
y = np.array(labels)

print(f"Generated {n_samples} training samples")
print(f"Overall survival rate: {np.mean(y):.2%}")
print(f"Female survival rate: {np.mean(y[X[:, 5] == 0]):.2%}")
print(f"Male survival rate: {np.mean(y[X[:, 5] == 1]):.2%}")

# Create and train the model
model = LogisticRegression(random_state=42, max_iter=1000)
model.fit(X, y)

# Test the model with our example cases
test_case_1 = np.array([[1.0, 44.0, 0.0, 0.0, 100.0, 1.0]])  # Male, 1st class
test_case_2 = np.array([[2.0, 50.0, 0.0, 3.0, 50.0, 0.0]])   # Female, 2nd class

pred1 = model.predict(test_case_1)
pred2 = model.predict(test_case_2)
prob1 = model.predict_proba(test_case_1)
prob2 = model.predict_proba(test_case_2)

print("\nModel Test Results:")
print(f"Case 1 (Male, 1st class): Prediction={pred1[0]}, Survival Prob={prob1[0][1]:.2%}")
print(f"Case 2 (Female, 2nd class): Prediction={pred2[0]}, Survival Prob={prob2[0][1]:.2%}")

# Save the model
with open('model/titanic_model.pkl', 'wb') as f:
    pickle.dump(model, f)

print(f"\nModel saved as 'model/titanic_model.pkl'")