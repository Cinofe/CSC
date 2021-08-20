from flask import Flask, render_template, request, flash, redirect, send_file
from mainProgram import *
import time

app = Flask(__name__)
app.secret_key = 'abcd1234!@#$'

@app.route('/')
def mainView():
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
                return render_template('upload.html',result=main())
            else:
                flash("docx 형식 워드 파일만 선택 가능합니다.")
                return render_template('mainView.html')


@app.route('/download_file')
def download_file():
    filepath = r"D:\seungwan\Desktop\AI_Study\Projects\CSC\webapp\flaskapp\files\Result\Text"+'/result.txt'
    return send_file(filepath, mimetype='text/txt',attachment_filename='result.txt',as_attachment=True)

app.run(host = '0.0.0.0', port=80)
#http://www.terms.kro.kr