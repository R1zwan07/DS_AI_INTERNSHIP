import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score

df = pd.read_csv("Day-14/car_data.csv")

X = df[["Experience"]]
y = df["PurchaseAmount"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

linear_model = LinearRegression()
linear_model.fit(X_train, y_train)
pred_linear = linear_model.predict(X_test)
r2_linear = r2_score(y_test, pred_linear)

poly = PolynomialFeatures(degree=2)
X_poly_train = poly.fit_transform(X_train)
X_poly_test = poly.transform(X_test)

poly_model = LinearRegression()
poly_model.fit(X_poly_train, y_train)
pred_poly = poly_model.predict(X_poly_test)
r2_poly = r2_score(y_test, pred_poly)

print(f"Linear Model R2 Score: {r2_linear:.3f}")
print(f"Polynomial Model R2 Score: {r2_poly:.3f}")

print("\nConclusion:")
if r2_poly > r2_linear:
    print("Polynomial features improved model performance (captures curve relationship).")
else:
    print("No improvement detected.")
