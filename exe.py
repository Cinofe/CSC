from tkinter import *
from tkinter import filedialog, ttk, messagebox as msg
from mainProgram import *
import os

class Exe:
    def start(self):
        root = Tk()
        #프로그램 title
        root.title("Launcher")
        #프로그램 size
        root.geometry("600x185+600+200")
        root.resizable(width=False, height=False)
        #레이블
        docxLabel = Label(root, text="문서 위치",font=(15))
        docxLabel.place(x=15,y=20)
        saveLabel = Label(root, text="txt 위치",font=(15))
        saveLabel.place(x=15,y=60)
        p_barLabel = Label(root, text="전체", font=(15))
        p_barLabel.place(x=15, y=105)
        p_barLabel2 = Label(root, text="일부", font=(15))
        p_barLabel2.place(x=15, y=145)
        #버튼
        docxButton = Button(root,text="문서 위치 설정",font=(15),width=12,command=self.add_docxPath)
        docxButton.place(x=460,y=15)
        saveButton = Button(root,text="txt 위치 설정",font=(15),width=12,command=self.add_savePath)
        saveButton.place(x=460,y=55)
        convertButton = Button(root, text="결과물 출력", font=(15),width=12,height=4,command=self.startProgram)
        convertButton.place(x=460,y=95)
        #프로그레스 바(진행 바)
        self.p_bar = DoubleVar()
        self.progressbar = ttk.Progressbar(root, maximum=100, length=385, variable=self.p_bar)
        self.progressbar.place(x=60,y=105)
        self.p_bar2 = DoubleVar()
        self.progressbar2 = ttk.Progressbar(root, maximum=100, length=385, variable=self.p_bar2) 
        self.progressbar2.place(x=60,y=145)
        #한 줄 입력 박스
        self.docxEntry = Entry(root,width=50)
        self.docxEntry.place(x=100, y=20)
        self.saveEntry = Entry(root,width=50)
        self.saveEntry.place(x=100,y=60)

        root.mainloop()

    def startProgram(self):
        if self.docxEntry.get() == "" or self.saveEntry.get() == "":
            msg.showinfo('오류','경로 입력이 잘못 되었습니다.')
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

    def open_file(self):
        response = msg.askyesno("완료","결과가 저장된 폴더를 여시겠습니까?")
        if response == True:
            filepath = r"D:\seungwan\Desktop\AI_Study\Projects\CSC\webapp\flaskapp\files\Result\Text"
            os.startfile(filepath)
    
    def alert(self):
        msg.showerror('오류',"api 리소스 할당 오류.\n잠시 후 다시 시도하세요.")
        exit()


if __name__ == "__main__":
    exe = Exe()
    exe.start()