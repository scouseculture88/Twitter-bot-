
from flask import Flask, render_template, request, redirect
from twitter_service import post_tweet
from scheduler_service import schedule_tweet
from database import init_db, get_scheduled_tweets

app = Flask(__name__)
init_db()

@app.route('/')
def dashboard():
    tweets = get_scheduled_tweets()
    return render_template('dashboard.html', tweets=tweets)

@app.route('/tweet', methods=['POST'])
def tweet():
    content = request.form['content']
    post_tweet(content)
    return redirect('/')

@app.route('/schedule', methods=['POST'])
def schedule():
    content = request.form['content']
    time = request.form['time']
    schedule_tweet(content, time)
    return redirect('/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
