-- migrate:up
create table reddit_posts(
  id integer,
  reddit_id varchar(32)
);

-- migrate:down
drop table reddit_posts;
