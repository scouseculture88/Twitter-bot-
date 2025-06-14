
import sqlite3

def init_db():
    conn = sqlite3.connect('bot.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS scheduled (content TEXT, time TEXT)''')
    conn.commit()
    conn.close()

def add_scheduled_tweet(content, time):
    conn = sqlite3.connect('bot.db')
    c = conn.cursor()
    c.execute("INSERT INTO scheduled (content, time) VALUES (?, ?)", (content, time))
    conn.commit()
    conn.close()

def get_scheduled_tweets():
    conn = sqlite3.connect('bot.db')
    c = conn.cursor()
    c.execute("SELECT content, time FROM scheduled")
    tweets = c.fetchall()
    conn.close()
    return tweets
