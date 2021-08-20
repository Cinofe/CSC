from flask import Flask, render_template, request, flash
from mainProgram import *

app = Flask(__name__)
app.secret_key = 'abcd1234!@#$'

@app.route('/')
def rendering():
    return render_template('mainView.html')

@app.route('/fileupload', methods = ['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        if f.filename == "":
            flash("파일을 선택하세요.")
            return render_template('mainView.html')
        else:
            if ('.docx' in f.filename) or ('.doc' in f.filename):
                f.save(r'D:\seungwan\Desktop\AI_Study\Projects\CSC\webapp\flaskapp\files\DocxFiles'+'/'+f.filename)
                return render_template('upload.html')
            else:
                flash("docx 형식 워드 파일만 입력 가능합니다.")
                return render_template('mainView.html')


app.run(host = '0.0.0.0', port=80)
#http://www.terms.kro.kr