from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import cross_val_score

X = [[1], [2], [3], [4], [5], [6]]
y = [0, 0, 1, 2, 3, 4]

model = LogisticRegression()

model.fit(X, y)

y_pred = model.predict(X)

accuracy = accuracy_score(y, y_pred)
scores = cross_val_score(model, X, y, cv=3)


print("Accuracy:", accuracy)
print("Scores:", scores)