from random import sample
import praw
import yaml
import os 

with open(r'quotes.yaml') as file:
    quotes = yaml.load(file, Loader=yaml.FullLoader)

reddit = praw.Reddit(client_id=os.environ['REDDIT_API_KEY'],
                     client_secret=os.environ['REDDIT_API_SECRET'],
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
