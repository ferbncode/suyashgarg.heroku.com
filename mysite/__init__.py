from flask import Flask, render_template, request, redirect
from .views.blog import blog
from .views.projects import projects
from .views.career import career

app = Flask(__name__)
app.secret_key = "sdadfafgaga"
app.debug = True
# registering blueprints

app.register_blueprint(blog, url_prefix='/blog')
app.register_blueprint(career, url_prefix='/career')
app.register_blueprint(projects, url_prefix='/projects')


@app.route('/')
def index():
	return render_template("index.html") 

@app.route('/contactme')
def contact():
	return "This is the contacts page"

@app.route('/know_more')
def know_more():
	return "This is the know me more page"

@app.route('/code')
def work():
	return redirect("https://github.com/ferbncode")

@app.route('/resume')
def resume():
	return "Here goes your resume"




