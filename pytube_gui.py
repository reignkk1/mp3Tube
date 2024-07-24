from tkinter import *
from tkinter import messagebox
from pytubefix import YouTube
import os

# 리팩토링 진행
# 저장할 곳 찾기 구현

root = Tk()
root.title('YouTube mp3 Free v0.1')
root.geometry('650x550')
root.resizable(False,False)

banner = PhotoImage(file="./assets/banner.png")
logo = PhotoImage(file='./assets/logo.png')

root.wm_iconphoto(False,logo)

label_1 = Label(root,image=banner,padx=0,pady=0)
label_1.pack()

label_2 = Label(root,height=5,text="다운받을 유튜브 영상 링크를 넣어주세요.",font=('',12,'bold'))
label_2.pack()

link_label = Label(root,text="링크")
link_label.pack()
link_entry = Entry(root,width=60)
link_entry.pack()

file_name_label = Label(root,text="파일 이름")
file_name_label.pack(pady=10)
file_name_entry = Entry(root,width=60)
file_name_entry.pack()


output_path_label = Button(root,text='저장할 곳 찾기')
output_path_label.pack(pady=10)
output_path_entry = Entry(root,width=60)
output_path_entry.pack()

def on_complete(_,output_path):
    messagebox.showinfo(title='알림',message='다운로드 완료! \n {}'.format(output_path))

def convert_button_click():
    link = link_entry.get()
    file_name = file_name_entry.get()
    windows_user_name = os.path.expanduser('~')

    yt = YouTube(link,on_complete_callback=on_complete)
    yt.streams.filter(only_audio=True).first().download(mp3=True,filename=file_name,output_path='{}/Downloads'.format(windows_user_name))

convert_button = Button(root,text='다운로드',width=10,command=convert_button_click)
convert_button.pack(side='bottom',pady=10)


root.mainloop()
