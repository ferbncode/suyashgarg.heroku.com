from flask import Blueprint, render_template

career = Blueprint('career', __name__)

@career.route('/')
def index():
	return render_template('career/index.html')



