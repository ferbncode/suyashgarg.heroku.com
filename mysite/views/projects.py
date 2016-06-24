from flask import Blueprint, render_template
from  ..models import *
projects = Blueprint('projects', __name__)

@projects.route('/')
def index():
	projects_summary = []
	#not feeling like adding generator...the below is slow and less memory-efficient
	for project in query_db("select * from projects"):
		projects_summary.append(project)
	return render_template('projects/index.html', projects_summary=projects_summary)


