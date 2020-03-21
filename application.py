import praw
import os 

reddit = praw.Reddit(client_id=os.environ['REDDIT_API_KEY'],
                     client_secret=os.environ['REDDIT_API_SECRET'],
                     user_agent='bot-in-black')

submissions = reddit.subreddit('westworld').hot(limit=10) 

for submission in submissions:
    # print(f"For submission {submission.id}")

    for comment in submission.comments:
        if comment.author is None:
            comment_author_name = "(Deleted)"
        else:
            comment_author_name = comment.author.name

        # print(f'{comment_author_name}: {comment.body}')
        if "Man in Black" in comment.body:
            print(f"Do something with {comment.id}")
