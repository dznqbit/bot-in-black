from peewee import *
import os
import psycopg2 as _psycopg2

env = os.environ

db = PostgresqlDatabase(
    env['BIB_DB_NAME'],
    user=env['BIB_DB_USER'],
    password=env['BIB_DB_PASSWORD'],
    host=env['BIB_DB_HOST'],
    port=env['BIB_DB_PORT']
)

class BaseModel(Model):
    class Meta:
        database = db

class RedditPost(BaseModel):
    reddit_id = CharField(unique=True)

MODELS = [RedditPost]
db.bind(MODELS, bind_refs=False, bind_backrefs=False)
db.connect()
db.create_tables(MODELS)
