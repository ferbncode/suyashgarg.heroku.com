from flask import Blueprint, render_template

blog = Blueprint('blog', __name__)

@blog.route('/')
def index():
	return "This is blog main page"


