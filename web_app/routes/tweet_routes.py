# web_app/routes/tweet_routes.py

# from flask import Blueprint, render_template, request, redirect

# from web_app.models import db, Twitter, parse_records

# tweet_routes = Blueprint("tweet_routes", __name__)

# @tweet_routes.route("/tweets")
# def tweets():
#     print("REQUESTED THE TWEETS PAGE")
#     tweet_records = Twitter.query.all()
#     return render_template("tweets.html", tweets = tweet_records)

# @tweet_routes.route("/tweets/new")
# def new_tweet():
#     return render_template("new_tweet.html")

# @tweet_routes.route("/tweets/create", methods=["POST"])
# def create_tweet():
#     print("FROM DATA:", dict(request.form))
#     new_tweet = Twitter(tweet=request.form["tweet"], user=request.form["user_name"])
#     print(new_tweet)
#     db.session.add(new_tweet)
#     db.session.commit()
#     return redirect("/tweets")
