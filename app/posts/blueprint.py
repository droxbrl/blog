from flask import Blueprint, render_template

posts = Blueprint(name='posts', import_name=__name__, template_folder='templates')


@posts.route('/')
def index():
    return render_template('posts/index.html')
