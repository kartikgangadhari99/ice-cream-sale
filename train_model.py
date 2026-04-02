import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import pickle

# Load the dataset
data = pd.read_csv('ice-cream.csv')

# Assume X = Temperature, y = IceCreamsSold (Sales)
X = data[['Temperature']]
y = data['IceCreamsSold']

# Split the dataset (80/20)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train LinearRegression model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict on test set
y_pred = model.predict(X_test)

# Print R² score
r2 = r2_score(y_test, y_pred)
print(f"R² Score: {r2:.4f}")

# Save model as model.pkl
with open('model.pkl', 'wb') as f:
    pickle.dump(model, f)

print("Model trained and saved as model.pkl")