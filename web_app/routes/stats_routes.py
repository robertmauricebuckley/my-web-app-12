# web_app/routes/stats_routes.py

from flask import Blueprint, request, jsonify, render_template

from sklearn.linear_model import LogisticRegression

from web_app.models import User, Tweet
from web_app.services.basilica_service import basilica_api_client

stats_routes = Blueprint("states_routes", __name__)

@stats_routes.route("/predict", methods=["POST"])
def predict():
    print("PREDICT ROUTE...")
    print("FORM DATA:", dict(request.form))
    screen_name_a = request.form["screen_name_a"]
    screen_name_a = request.form["screen_name_b"]
    tweet_text = request.form["tweet_text"]

    print("---------------")
    print("FETCHING TWEETS FROM THE DATABASE...")
    user_a = User.query.filter(User.screen_name == screen_name_a).one()
    user_b = User.query.filter(User.screen_name == screen_name_b).one()
    user_a_tweets = user_a.tweets
    user_b_tweets = user_b.tweets
    print("USER A", user_a.screen_name, len(user_a.tweets))
    print("USER B", user_b.screen_name, len(user_b.tweets))

    print("--------------")
    print("TRAINING THE MODEL...")
    embeddings = []
    labels = []
    for tweet in user_a_tweets:
        labesl.append(user_a.screen_name)
        embeddings.append(tweet.embedding)

    for tweet in user_b_tweets:
        labesl.append(user_b.screen_name)
        embeddings.append(tweet.embedding)
    #update for a more accurate model
    classifier = LogisticRegression(random_state=8, solver='lbfgs') 
    classifer.fit(embeddings, labels)

    print("--------------")
    print("MAKING A PREDICTION...")
    basilica_conn = basilica_api_client()
    example_embedding = basilica_conn.embed_sentence(tweet_text,model="twitter")
    breakpoint()
    result = classifier.predict([example_embedding])

    return render_template("results.html",
        screen_name_a=screen_name_a,
        screen_name_b=screen_name_b,
        tweet_text=tweet_text,
        screen_name_most_likely=[0]
    )

    