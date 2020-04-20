from flask import render_template, flash, redirect, url_for
from werkzeug.utils import secure_filename
from app import app
from app.forms import LoginForm

@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = LoginForm()
    if form.validate_on_submit():
        filenames = []
        for files in form.folder.data:
            filenames.append(files)
        print(filenames)
        return redirect(url_for('index'))
    return render_template('index.html', title='String Matcher - 13518030', form=form)

@app.route('/about')
def about():
    return render_template('about.html', title="About Me")