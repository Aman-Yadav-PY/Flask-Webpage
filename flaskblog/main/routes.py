from flask import Blueprint, render_template, request
from flaskblog.models import Post, User

app = Blueprint('main', __name__)

@app.route('/')
@app.route('/home')
def home():
	page = request.args.get('page', 1, type=int)
	post = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
	return render_template("home.html", posts=post)

@app.route('/about')
def about():
	return render_template("about.html")


