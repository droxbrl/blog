from flask import Blueprint, render_template, request, redirect, url_for
from app import db, app
from models import Post, Tag
from .forms import PostFrom

posts = Blueprint(name='posts', import_name=__name__, template_folder='templates')


@posts.route('/create', methods=['POST', 'GET'])
def create_post():
    if request.method == 'POST':
        title = request.form.get('title', '')
        body = request.form.get('body', '')
        # tags = request.form.get('tags', '')
        # if tags:
        #    for tag in tags.split(','):
        #        new_tag = Tag(name=tag)
        #        db_save(data=new_tag)
        if title and body:
            post = Post(title=title, body=body)
            db_save(data=post)

            return redirect(url_for('posts.index'))

    form = PostFrom()
    return render_template('posts/create_post.html', form=form)


@posts.route('/<slug>/edit/', methods=['POST', 'GET'])
def edit_post(slug):
    post = Post.query.filter(Post.slug == slug).first()
    if request.method == 'POST':
        form = PostFrom(formdata=request.form, obj=post)
        form.populate_obj(post)
        db_commit()
        return redirect(url_for('posts.post_detail', slug=post.slug))

    form = PostFrom(obj=post)
    return render_template('posts/edit_post.html', post=post, form=form)


@posts.route('/')
def index():
    q = request.args.get('q')
    page = request.args.get('page')
    if page and page.isdigit():
        page = int(page)
    else:
        page = 1
    if q:
        posts = Post.query.filter(Post.title.contains(q) | Post.body.contains(q))
    else:
        posts = Post.query.order_by(Post.created.desc())

    pages = posts.paginate(page=page, per_page=5)

    return render_template('posts/index.html', posts=posts, pages=pages)


@posts.route('/<slug>')
def post_detail(slug):
    post = Post.query.filter(Post.slug == slug).first()
    tags = post.tags.all()
    return render_template('posts/post_detail.html', post=post, tags=tags)


@posts.route('/tag/<slug>')
def tag_detail(slug):
    tag = Tag.query.filter(Tag.slug == slug).first()
    posts = tag.posts
    return render_template('posts/tag_detail.html', posts=posts, tag=tag)


def db_save(data):
    if data:
        try:
            with app.app_context():
                db.session.add(data)
                db.session.commit()
        except:
            pass
            # TODO: ???????????????????? ????????????????????


def db_commit():
    db.session.commit()
