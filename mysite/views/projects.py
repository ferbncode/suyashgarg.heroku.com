from flask import Blueprint, render_template

projects = Blueprint('projects', __name__)

@projects.route('/')
def index():
	return "This is the projects main page"

