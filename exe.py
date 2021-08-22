from tkinter import *
from tkinter import filedialog, ttk
from mainProgram import *

class Exe:
    def start(self):
        root = Tk()
        #프로그램 title
        root.title("Launcher")
        #프로그램 size
        root.geometry("600x155+600+200")
        #레이블
        docxLabel = Label(root, text="문서 위치",font=(15))
        docxLabel.place(x=15,y=20)
        saveLabel = Label(root, text="txt 위치",font=(15))
        saveLabel.place(x=15,y=60)
        #버튼
        docxButton = Button(root,text="문서 위치 설정",font=(15),width=12,command=self.add_docxPath)
        docxButton.place(x=460,y=15)
        saveButton = Button(root,text="txt 위치 설정",font=(15),width=12,command=self.add_savePath)
        saveButton.place(x=460,y=55)
        convertButton = Button(root, text="결과물 출력", font=(15),width=12,height=2,command=self.startProgram)
        convertButton.place(x=460,y=95)
        #프로그레스 바(진행 바)
        p_bar = DoubleVar()
        progressbar = ttk.Progressbar(root, maximum=39, length=430, variable=p_bar)
        progressbar.place(x=15,y=110)
        #한 줄 입력 박스
        self.docxEntry = Entry(root,width=50)
        self.docxEntry.place(x=100, y=20)
        self.saveEntry = Entry(root,width=50)
        self.saveEntry.place(x=100,y=60)

        root.mainloop()

    def startProgram(self):
        if self.docxEntry.get() == "" or self.saveEntry.get() == "":
            print('경로 입력이 잘못 되었습니다.')
        else:
            main(self.docxEntry.get()+'/',self.saveEntry.get()+'/',exe)

    def add_docxPath(self):
        path = filedialog.askdirectory()
        if path is None:
            return
        self.docxEntry.delete(0,END)
        self.docxEntry.insert(0,path)
    
    def add_savePath(self):
        path = filedialog.askdirectory()
        if path is None:
            return
        self.saveEntry.delete(0,END)
        self.saveEntry.insert(0,path)

if __name__ == "__main__":
    exe = Exe()
    exe.start()