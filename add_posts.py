import json
from flaskblog import db
from flaskblog.models import User, Post


with open('posts.json') as f:
    data = json.load(f)

for post in data:
    user = User.query.get(post['user_id'])
    if user:
        post = Post(title=post['title'], content=post['content'], user_id=post['user_id'])
        db.session.add(post)
        db.session.commit()
