from threading import Thread
from tkinter.filedialog import askdirectory
from tkinter.messagebox import showinfo
from tkinter.ttk import *
from pytube import YouTube
from tkinter import filedialog
from tkinter import *

#                               https://www.youtube.com/watch?v=RQ0FzwaqLow
# download
size = 0


def down(link):
    global size
    folder = askdirectory()
    if folder is None:
        return

    try:
        yt = YouTube(link)
        st = yt.streams.first()
        size = st.filesize
        st.download(output_path=folder)
        showinfo("Message", yt.title, "Download Finished")
    except EXCEPTION as e:
        print(e)
        print("something went wrong")


# #button
def btnClicked():
    try:
        btn['text'] = "Waiting..."
        btn['state'] = 'disabled'
        link = ip.get()
        if link == '':
            showinfo("Error", "Unknown YouTube URL")
            root.title('Simple Youtube downloader  (Please Enter a valid URL)')
#            btn['text'] = "Download"
#            btn['state'] = 'active'
            return
        print(link)
        thread = Thread(target=down, args=(link,))
        thread.start()

    except Exception as e:
        print(e)


# gui
font = ('Georgia', 20)
root = Tk()
root.geometry("500x400")
root.title("Simple Youtube downloader")
# #Icon
root.iconbitmap(r"C:\Users\R4V3N\PycharmProjects\YouTube Downloader\venv\img\icon.ico")
# #Thubnail
#file = PhotoImage(file=r"C:\Users\R4V3N\PycharmProjects\YouTube Downloader\venv\img\icon.png")
#label = Label(image=file)
# headingIcon = Label(root, image=file)
# headingIcon.pack(side=TOP, pady=3)
#label.pack()
# #Input
ip = Entry(root, font=font, justify=LEFT)
ip.pack(side=TOP, fill=X, padx=10)
ip.focus()
btn = Button(root, text="Download", font=font, relief='ridge', command=btnClicked)
btn.pack(side=TOP, pady=10)
root.mainloop()

# down("https://www.youtube.com/watch?v=dNOqW8IxmGY")
