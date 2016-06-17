from flask import Blueprint, render_template

career = Blueprint('career', __name__)

@career.route('/')
def index():
	return "This is career main page"



