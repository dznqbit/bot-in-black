from random import sample
import psycopg2
import praw
import yaml
import os

env = os.environ

try:
    connection = psycopg2.connect(user = env['BIB_DB_USER'],
            password = env['BIB_DB_PASSWORD'],
            host = env['BIB_DB_HOST'],
            port = env['BIB_DB_PORT'],
            database = env['BIB_DB_NAME'])

    cursor = connection.cursor()
    # Print PostgreSQL Connection properties
    print ( connection.get_dsn_parameters(),"\n")

    # Print PostgreSQL version
    cursor.execute("SELECT version();")
    record = cursor.fetchone()
    print("You are connected to - ", record,"\n")

except (Exception, psycopg2.Error) as error :
    print ("Error while connecting to PostgreSQL", error)
finally:
    #closing database connection.
        if(connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

with open(r'quotes.yaml') as file:
    quotes = yaml.load(file, Loader=yaml.FullLoader)

reddit = praw.Reddit(client_id=env['REDDIT_API_KEY'],
        client_secret=env['REDDIT_API_SECRET'],
        user_agent='bot-in-black')

submissions = reddit.subreddit('westworld').hot(limit=10)
comments = [c for s in submissions for c in s.comments]

def summarize_comment(comment):
    author_name = "(Deleted)" if comment.author is None else comment.author.name
    print(f'{author_name}: {comment.body[0:64]}')

def add_comment(comment):
    print(f"Do sometihng with {comment.id}")
    print(sample(quotes, 1)[0])

for comment in comments:
    # summarize_comment(comment)

    if "Rehoboam" in comment.body:
        add_comment(comment)

# RAW t1_fl2qtzp
# DZNQBIT POST ID fl2qtzp
