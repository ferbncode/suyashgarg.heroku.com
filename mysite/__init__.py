from flask import Flask, render_template, request
from .views.blog import blog
from .views.projects import projects
from .views.career import career

app = Flask(__name__)
app.secret_key = "sdadfafgaga"

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

@app.route('/work')
def work():
	return "This is the work page"

@app.route('/resume')
def resume():
	return "Here goes your resume"

if __name__ == '__main__':
	app.run(debug=True)




