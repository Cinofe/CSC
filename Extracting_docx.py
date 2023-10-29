import docx
import re
import os

def getText(filepath):
    '''
    docx 워드 파일에서 텍스트를 추출해주는 함수
    '''
    doc = docx.Document(filepath)
    fulltext = []

    for para in doc.paragraphs:
        fulltext.append(para.text)
    return '\n'.join(fulltext)

def data_Preprocessing(text):
    '''
    텍스트에서 필요없는 부분을 없애주는 전처리 함수
    '''
    ReturnText = ''

    for i in range(len(text)):
        if text[i-2] != '\n' or text[i] != '\n':
            if text[i-1] !='.' or text[i] != '.':
                if text[i-1] != " " or text[i] != " ":
                    if text[i] != "\t":
                        ReturnText += text[i]
    
    ReturnText = re.sub("[※]","",ReturnText)
    return ReturnText