# web/routes/iris_routes.py

from flask import Blueprint
from sklearn.datasets import load_iris

from web_app.iris_classifier import load_model

iris_routes = Blueprint("iris_routes", __name__)

@iris_routes.route("/stats/iris")
def iris():
    X, y = load_iris(return_X_y=True)
    clf = load_model()
    return str(clf.predict(X[:2, :]))