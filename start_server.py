from flask import Flask, render_template, request
from mainProgram import *

app = Flask(__name__)

@app.route('/')
def rendering():
    return render_template('mainView.html')

@app.route('/fileupload', methods = ['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        f.save(r'D:\seungwan\Desktop\AI_Study\Projects\CSC\DocxFiles'+'/'+f.filename)
        return render_template('upload.html')


app.run(host = '0.0.0.0', port=80)
#http://test.terms.kro.kr