from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import FileField
from flask_wtf.csrf import CSRFProtect
import os
import secrets
import subprocess

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'upload'
app.config['ALLOWED_EXTENSIONS'] = {'csv', 'xls', 'xlsx'}
csrf = CSRFProtect(app)

# Generate a random secret key
app.secret_key = secrets.token_hex(16)

class UploadForm(FlaskForm):
    file = FileField('Upload Packet Data (CSV)')

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    form = UploadForm()
    if request.method == 'POST' and form.validate_on_submit():
        file = form.file.data
        if file and allowed_file(file.filename):
            filename = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(filename)

            visualization_script = 'visualization.py'
            cmd = f'python {visualization_script} --data_file {filename}'
            subprocess.run(cmd, shell=True)

            return render_template('visualizations.html')

    return render_template('upload.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
