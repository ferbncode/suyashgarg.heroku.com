from flask import Blueprint, render_template
from  ..models import *
blog = Blueprint('blog', __name__)

@blog.route('/')
def index():
	blog_summary = []
	#not feeling like adding generator...the below is slow and less memory-efficient
	for blog in query_db("select * from projects"):
		blog_summary.append(blog)
	return render_template('blog/index.html', blog_summary=blog_summary)
@blog.route('/<blogname>')
def projectread(blogname):
	blog_detail = query_db("select * from projects where subject=?", [blogname])
	blog_detail = project_detail[0]
	if blog_detail == []:
		return "Its a 404 buddy",404
	return render_template("blog/blogdet.html", blog_detail = blog_detail)

