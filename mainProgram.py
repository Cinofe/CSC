from tqdm import tqdm
import Extracting_docx as dc
import Analysis_API as api
import os, shutil, time

#폴더 생성 함수 중복 폴더 제거
def create_forlder(path):
    if os.path.exists(path):
        shutil.rmtree(path)
    os.mkdir(path)
#워드에서 텍스트를 추출해서 한 문장씩 불리해 저장하는 함수
def Extracting_docx(Dfilepath, Tfilepath):
    #해당 경로의 모든 파일이름을 리스트 형식으로 반환하는 함수
    Dfiles = os.listdir(Dfilepath)
    #문자 개수 측정 변수
    charCount = 0
    #한 문장이 들어가는 변수
    sen_text = ''
    #파일 이름 변수 (번호)
    file_no = 1
    #페이지 수 폴더 이름
    page_no = 1
    #문서 이름 번호
    doc_no = 1

    os.system('cls')
    print("텍스트 추출중...")
    for f in tqdm(range(len(Dfiles))):
        #한 파일의 모든 문자 추출하는 함수
        DTexts = dc.getText(Dfilepath+Dfiles[f])
        #추출된 문자들 중 필요없는 부분 제거하는 전처리 함수
        DTexts = dc.data_Preprocessing(DTexts)
        #문서 폴더 생성 기존 폴더 제거  
        create_forlder(Tfilepath+'Document'+str(doc_no))

        if page_no == 1:
            #페이지 폴더 생성 기존 폴더 제거
            create_forlder(Tfilepath+'Document'+str(doc_no)+'/'+str(page_no)+' page')
        
        for i in range(len(DTexts)):
            if DTexts[i] != '\n':
                #enter로 문장 구분
                sen_text += DTexts[i]
                charCount += 1
            else :
                if len(sen_text) > 20:
                #한페이지당 전체 문서 입력
                    with open(Tfilepath+'Document'+str(doc_no)+'/'+str(page_no)+' page/all text.txt','a',encoding='utf-8') as tf:
                        tf.write(sen_text)
                        tf.write('\n')
                    #문장 길이가 30이하라면 입력 안함    
                    Tfilename = Tfilepath+'Document'+str(doc_no)+'/'+str(page_no)+' page/'+str(file_no)+'.txt'
                    #같은 파일이름이 있을 경우 해당 파일 제거
                    if os.path.isfile(Tfilename):
                        os.remove(Tfilename)
                    with open(Tfilename,"w",encoding='utf-8') as tf:
                        tf.write(sen_text)
                    sen_text = ''
                    file_no += 1
                else :
                    sen_text = ''
            #총 글자수가 700자 이상이면 한페이지로 정의 하고 문자 카운트 초기화
            if charCount >= 850:
                charCount = 0
                page_no += 1
                create_forlder(Tfilepath+'Document'+str(doc_no)+'/'+str(page_no)+' page')
        doc_no += 1
        page_no = 1
#각 문장마다 감정 분석을 통해 나쁨이 나온 문장 분류
def Analysis_text(Tfilepath,exe):
    #페이지 폴더 이름
    page_no = 1
    #문서 폴더 이름
    doc_no = 1
    #0감정 문장들의 파일 이름 저장하는 리스트
    bed_text = []
    scores = {}

    Dfiles = os.listdir(Tfilepath)
    os.system('cls')
    print('분석중...')
    for f in tqdm(range(len(Dfiles))):
        Pfiles = os.listdir(Tfilepath+Dfiles[f]+'/')
        print('분석중..')
        for P in tqdm(range(len(Pfiles))):
            if exe != None:
                exe.p_bar.set((P/(len(Pfiles)-1))*100)
            #각 페이지 폴더 전체 경로
            PagePath = Tfilepath+'Document'+str(doc_no)+'/'+str(
                page_no)+' page/'
            #경로안의 파일이름을 리스트 형식으로 반환
            Texts = os.listdir(PagePath)
            print('분석중.')
            for i in tqdm(range(len(Texts))):
                if exe != None:
                    exe.p_bar2.set((i/(len(Texts)-1))*100)
                #alltext안나오게 해야함
                if Texts[i].find('all') == -1:
                    try:
                        score = float(api.Analysis_Text(PagePath+Texts[i]))
                    except:
                        if exe != None:
                            exe.alert()
                    if score <= -0.9:
                        bed_text.append(Texts[i])
                        scores.setdefault(Texts[i],score)
                    time.sleep(0.05)
                if exe != None:
                    exe.progressbar2.update()
            page_no += 1
            if exe != None:
                exe.progressbar.update()
            os.system('cls')
        doc_no += 1
        page_no = 1
    
    findpages = find_folder(bed_text,Tfilepath)
    combi_text(findpages)

#bed_texts에 들어있는 문장들이 포함된 페이지 폴더 찾기
def find_folder(bed_text,path):
    #찾은 폴더 경로 저장
    find = []
    folders = os.listdir(path)

    for i in range(len(folders)):
        pagepath = path+folders[i]+'/'
        pages = os.listdir(pagepath)

        for p in range(len(pages)):
            #페이지 내부 경로(ex: ~~~/Documuent1/page[p]/)
            inPagePath = pagepath+pages[p]+'/'
            #페이지 폴더 내부에 있는 파일들의 이름을 리스트 형식으로 반환
            texts = os.listdir(inPagePath)
            for j in range(len(bed_text)):
                #bed_text의 j번째(ex: 1.txt)가 texts 에 포함되어 있다면 true 반환
                if bed_text[j] in texts:
                    #찾은 폴더의 경로가 이미 저장되어있다면 true 반환 이 경우는 없을때 경로를 저장해야 함으로 앞에 not을 붙여서
                    #false가 나왔을 경우 즉 저장된 경로가 없을경우 새로운 경로 추가
                    if not((p, str(inPagePath)) in find):
                        find.append((p,str(inPagePath)))

    return find
    
#페이지 폴더 안에 있는 문장들을 하나로 합치는 함수
def combi_text(paths):
    #합쳐질 문자를 담을 변수
    appendText = ''
    for path in paths:
        i = path[0]
        Texts = os.listdir(path[1])
        with open(path[1]+Texts[-1],'r',encoding='utf-8') as f:
            #path에는 (해당 페이지, txt까지 경로)가 튜플 형태를 들어있다.
            if path[0] == i:
                appendText += f'\t\t\t------------{path[0]}page------------\n'
                i +=1
            appendText += f.read()
            appendText += '\n\n'
    #합쳐진 txt를 저장할 경로
    new_path = r'D:\seungwan\Desktop\Study\Python\AI_Study\Projects\CSC\webapp\flaskapp\files\Result\Text'
    create_forlder(new_path)
    new_path = new_path + '/result.txt'
    #이미 같은 파일이 있다면 제거후 입력
    if os.path.isfile(new_path):
        os.remove(new_path)
    with open(new_path,'a',encoding='utf-8') as nf:
        nf.write(appendText)

#웹서버로 실행시 경로가 지정되어 있지만 exe 로 실행시 지정된 경로로 이동
def main(Dpath=None,Tpath=None,exe=None):
    #여기에 자신의 파일 밑 폴더 경로 입력 
    if Dpath == None:
        Dfilepath = r"D:\seungwan\Desktop\Study\Python\AI_Study\Projects\CSC\webapp\flaskapp\files\DocxFiles"+'/'
        Tfilepath = r"D:\seungwan\Desktop\Study\Python\AI_Study\Projects\CSC\webapp\flaskapp\files\textfiles"+'/'
    else:
        Dfilepath = Dpath
        Tfilepath = Tpath
    #텍스트 추출 작업
    Extracting_docx(Dfilepath,Tfilepath)
    #감정 점수 분석 후 분류작업
    Analysis_text(Tfilepath,exe)

    #docx 폴더 청소(한번 실행이 끝나면 모든 파일을 삭제)
    forders = os.listdir(Dfilepath)
    for f in forders:
        fpath = Dfilepath+f
        os.remove(fpath)
    
    #txt 폴더 청소(한번 실행이 끝나면 모든 파일을 삭제)
    forders = os.listdir(Tfilepath)
    for f in forders:
        fpath = Tfilepath+f
        shutil.rmtree(fpath)

    if exe != None:
        exe.open_file()