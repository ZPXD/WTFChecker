from flask import Flask, render_template, redirect, url_for, flash, request

import flask_wtf
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, BooleanField, SubmitField

from flask_wtf.file import FileField, FileRequired
from werkzeug.utils import secure_filename

import os
import random
import string
import threading

from wtf_checker import WTFChecker


ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'zip', 'tar'} # Code from Flask
app.config['UPLOAD_FOLDER'] = os.getcwd() + '/'
app.config['MAX_UPLOAD_CONTENT_LENGTH'] = 16 * 1000 * 1000
app.config['UPLOAD_SIZE_MAX'] = 16 * 1000 * 1000

app = Flask(__name__)
app.secret_key = 'aefefffafe'



def check_result(check_id):
    WTF = WTFChecker()
    check_folder = os.path.join(app.config['UPLOAD_FOLDER'], check_id)
    #result_file = os.path.join(check_folder, 'so.json')
    result_file = os.path.join(check_folder, 'so.txt')
    result = WTF.read_result_for(result_file)
    return result

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS # Code from Flask

@app.route('/')
def index():
    WTF = WTFChecker()
    form = WTFCheckerForm()
    if form.validate_on_submit():
        #if form.data_info_checkbox.data == True:
        if True:
            url = form.url.data
            code = form.code.data
            file = form.file.data
            check_id = create_id()
            if len(code) > 1:
                what = code
            elif len(url.strip()) > 1:
                what = WTF.get_file_from_url(url) # !!!
            elif file:
                filename = secure_filename(file.filename)
                if allowed_file(filename):
                    folder = os.path.join(app.config['UPLOAD_FOLDER'], check_id)
                    filepath = os.path.join(folder, filename)
                    os.mkdir(folder)
                    file.save(filepath)
                what = filepath
            estimation = WTF.estimate(what)
            return redirect(url_for('chill', check_id=check_id, estimation=estimation, what=what))
    return render_template("index.html")

@app.route('/<check_id>/chill')
def chill(check_id, estimation=None, what=None):
    if not estimation or not what:
        return redirect(url_for('index'))
    checking_wtf = threading.Thread(target=WTF.check_it, args=[what])
    checking_wtf.start()
    form = Next()
    files_to_check = os.path.join(app.config['UPLOAD_FOLDER'], check_id)
    if form.validate_on_submit():
        return redirect(url_for('result', check_id=check_id))
    return render_template("chill.html", form=form, estimation=estimation, files_to_check=files_to_check, check_id=check_id)

@app.route('/<check_id>/result')
def result(check_id):
    result = check_result(check_id)
    os.system('rm {}'.format(result_file))
    os.mkdir(check_folder)
    return render_template("info.html", result=result)

@app.route('/secret_check', methods=['GET', 'POST'])
def secret_check():
    if request.method == 'POST':
        headers = dict(request.headers)
        #user = headers['User']
        #key = headers['Key']
        #password = headers['Password']
        #user = User.query.filter_by(email=user).first()
        if True:
        #if user:
            if True:
            #if user.check_password(password) and user.check_password(key):
                WTF = WTFChecker()
                if headers['what']:
                    WTF.check_it(what)
                elif headers['file']:
                    #unzip
                    #what = request.files['file']
                    #what = headers['file']
                    WTF.check_it(what)
                else:
                    return {"response":"what?"}
                result, results = check_result(check_id)
                return {"code" : "https://github.com/ZPXD/WTFChecker.git", "result" : result, "results" : results }
            return {"code" : "https://github.com/ZPXD/WTFChecker.git", "response" : "what you want?"}
        return  {"code" : "https://github.com/ZPXD/WTFChecker.git", "response" : "what you want?"}


@app.route('/see_the_code', methods=['GET', 'POST'])
def see_the_code():
    if request.method == 'POST':
        response = {'repo' : 'https://github.com/ZPXD/WTFChecker.git'}
    return render_template('see_the_code.html')

def wtf_check_file(what):
    '''
    Copy this function to your program.

    Use this code in whatever program you need.
    '''
    import requests
    import os
    url = 'http://lukasz-pintal.pl/wtf'
    headers = {
        "user" : "",
        "key" : "",
        "msg" : "hi",
    }
    if 'www' in what[:10]:
        headers['what'] = what
    elif len(what) < 200 and os.path.exists(what):
        file = {'file': open(what,'rb')}
    else:
        headers['what'] = what
    
    r = requests.post(url, files=file, headers=headers)
    info = r.json()

    result = info['result']
    results = info['results']
    return result, results
#wtf_check_file(what)



# Erroros.

@app.errorhandler(404)
def handle_404(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def handle_500(e):
    return render_template('500.html'), 500


# Forms.

class WTFCheckerForm(FlaskForm):
    url = StringField()
    code = TextAreaField()
    file = FileField(validators=[FileRequired()])
    data_info_checkbox = BooleanField()
    ok = SubmitButton()

class Next(FlaskForm):
    ok = SubmitButton()


if __name__=="__main__":
	app.run(debug=True)
