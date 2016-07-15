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
@projects.route('/<projectname>')
def projectread(projectname):
	project_detail = query_db("select * from projects where subject=?", [projectname])
	project_detail = project_detail[0]
	if project_detail == []:
		return "Its a 404 buddy",404
	return render_template("projects/projdet.html", project_detail = project_detail)
@projects.route('/test')
def pr():
	return render_template('projects/detailTest.html')
