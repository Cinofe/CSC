from flask import Flask, render_template, request, flash, send_file, Response
from mainProgram import *
import ssl

app = Flask(__name__)

#처음 들어오면 보이는 화면을 만들어줌
@app.route('/')
def mainView():
    return render_template('mainView.html')

#파일 업로드 버튼을 클릭했을시 이동되는 웹 경로와 해당 경로에서 처리하는 일
@app.route('/fileupload', methods = ['GET','POST'])
def upload_file():
    #반환된 request 값이 POST 라면 작업 시작
    if request.method == 'POST':
        #입력된 파일 없다면 경고창 출력
        f = request.files['file']
        if f.filename == "":
            flash('파일을 선택하세요.')
            return render_template('mainView.html')
        else:
            #입력된 파일이 워드 형식이 아니라면 경고창 출력
            if ('.docx' in f.filename) or ('.doc' in f.filename):
                #워드 형식 파일이라면 처리중 화면을 보여줌
                f.save(r'D:\seungwan\Desktop\Study\Python\AI_Study\Projects\CSC\webapp\flaskapp\files\DocxFiles'+'/'+f.filename)
                return render_template('wait.html')
            else:
                flash("docx 형식 워드 파일만 선택 가능합니다.")
                return render_template('mainView.html')
#처리중 화면에서 해당 경로 호출
@app.route('/complete', methods = ['GET'])
def complete():
    #호출되면 메인코드가 실행되고
    try:
        main()
    except:
        flash('error')
        return render_template('mainView.html')
    #메인 코드가 끝나면 완료된 화면을 보여줌
    return render_template('upload.html')

#완료된 화면에서 다운로드를 클릭할시 실행됨
@app.route('/download_file')
def download_file():
    #다운로드할 파일 경로
    filepath = r"D:\seungwan\Desktop\Study\Python\AI_Study\Projects\CSC\webapp\flaskapp\files\textfiles" + "/result.txt"
    #파일을 다운로드 시켜줌
    return send_file(filepath, mimetype='text/txt',download_name='result.txt', as_attachment=True)

if __name__ == "__main__":

    context = ssl.SSLContext(ssl.PROTOCOL_TLS)
    context.load_cert_chain(certfile='ssl/certificate.crt',keyfile='ssl/private.key', password='OMG')
    app.secret_key = 'qwer1234!@#$'

    app.run(host='0.0.0.0', port='443', ssl_context=context)