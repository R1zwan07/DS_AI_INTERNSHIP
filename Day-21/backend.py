# Step 1: Import Libraries
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# Step 2: Load Dataset
df = pd.read_csv("E:\DS_AI_Internship\Day-21\Iris.csv")

# Step 3: Basic Info
print("First 5 Rows:\n", df.head())
print("\nDataset Info:\n")
print(df.info())

# Step 4: Drop Unnecessary Column (Id)
df = df.drop("Id", axis=1)

# Step 5: Separate Features (X) and Target (y)
X = df.drop("Species", axis=1)
y = df["Species"]

# Step 6: Encode Target Labels (Convert text to numbers)
le = LabelEncoder()
y = le.fit_transform(y)

# Step 7: Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Step 8: Train Model
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# Step 9: Make Predictions
y_pred = model.predict(X_test)

# Step 10: Evaluate Model
print("\nAccuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))
print("\nConfusion Matrix:\n", confusion_matrix(y_test, y_pred))