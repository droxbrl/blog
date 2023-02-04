from flask import Blueprint, render_template
from models import Post

posts = Blueprint(name='posts', import_name=__name__, template_folder='templates')


@posts.route('/')
def index():
    posts = Post.query.all()
    return render_template('posts/index.html', posts=posts)
