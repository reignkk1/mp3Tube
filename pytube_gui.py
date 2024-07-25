from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from pytubefix import YouTube


# 리팩토링 진행

root = Tk()
root.title('mp3Tube v0.1')

# 창 크기
width = '650'
height = '550'

root.geometry('{}x{}'.format(width,height))
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



# 저장할곳 찾기 버튼 클릭
def save_directory_button_click():
    output_path_entry_text_remover()
    save_directory = filedialog.askdirectory()
    output_path_entry_text_insert(save_directory)
    

# 저장할 주소 Text 지우기
def output_path_entry_text_remover():
    output_path_entry.configure(state='normal')
    output_path_entry.delete(0,'end')
    output_path_entry.configure(state='readonly')

# 저장할 주소 insert
def output_path_entry_text_insert(text:str):
    output_path_entry.configure(state='normal')
    output_path_entry.insert(0,text)
    output_path_entry.configure(state='readonly')
    

output_path_label = Button(root,text='저장할 곳',command=save_directory_button_click)
output_path_label.pack(pady=10)
output_path_entry = Entry(root,width=60,state='readonly')
output_path_entry.pack()


# 링크, 파일이름 Entry 비우기
def link_filename_entry_remove():
    link_entry.delete(0,'end')
    file_name_entry.delete(0,'end')
    link_entry.focus()


# 다운로드 완료
def on_complete(_,output_path):
    messagebox.showinfo(title='알림',message='다운로드 완료! \n {}'.format(output_path))
    link_filename_entry_remove()

# 에러 메세지 띄우기
def show_warning_message(message):
    messagebox.showwarning(title='에러',message=message)


# 다운로드 버튼 클릭
def convert_button_click():
    try:
        link = link_entry.get()
        file_name = file_name_entry.get()
        save_directory = output_path_entry.get()

        if(link == ''):
            return show_warning_message('링크를 입력해주세요.')
        elif(file_name == ''):
            return show_warning_message('파일 이름을 입력해주세요.')
        elif(save_directory == ''):
            return show_warning_message('저장할 곳을 선택해주세요.')

        yt = YouTube(link,on_complete_callback=on_complete)
        yt.streams.filter(only_audio=True).first().download(mp3=True,filename=file_name,output_path=save_directory)
    except:
        show_warning_message('다운로드 실패!')
            

convert_button = Button(root,text='다운로드',width=10,command=convert_button_click)
convert_button.pack(side='bottom',pady=10)

root.mainloop()
