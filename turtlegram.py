from flask import Flask, render_template, send_from_directory
import os
import urllib2
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/gallery')
def gallery():
    return render_template('gallery.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/create')
def create():
    return render_template('create.html')

@app.route('/view/')
@app.route('/view/<post_id>')
def view(post_id):
	url = 'https://turtlegram.firebaseio.com/posts/' + post_id + '.json'
	data = json.load(urllib2.urlopen(url))
	print data
	return render_template('view.html', post_id=post_id, post_data=data)

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'img/favicon.ico', mimetype='image/vnd.microsoft.icon')

if __name__ == '__main__':
    app.run()