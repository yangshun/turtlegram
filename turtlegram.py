from flask import Flask, render_template

app = Flask(__name__)
app.config['PROPAGATE_EXCEPTIONS'] = True

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

@app.route('/view/<post_id>')
def view(post_id):
    return render_template('view.html', post_id=post_id)

if __name__ == '__main__':
    app.run()