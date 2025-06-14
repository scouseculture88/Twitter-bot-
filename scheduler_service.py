
from apscheduler.schedulers.background import BackgroundScheduler
from twitter_service import post_tweet
from database import add_scheduled_tweet, get_scheduled_tweets

scheduler = BackgroundScheduler()
scheduler.start()

def schedule_tweet(content, time):
    scheduler.add_job(post_tweet, 'date', run_date=time, args=[content])
    add_scheduled_tweet(content, time)
