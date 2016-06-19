from flask import Blueprint, render_template

blog = Blueprint('blog', __name__)

@blog.route('/')
def index():
	return render_template('blog/index.html')


