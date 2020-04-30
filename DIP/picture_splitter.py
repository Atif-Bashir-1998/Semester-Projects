from tkinter import *
from tkinter import filedialog
from PIL import ImageTk,Image
from image_to_blocks import split_image


def open():
    global selected_image
    window.filename = filedialog.askopenfilename(initialdir="/", title="Select file",filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))
    selected_image = ImageTk.PhotoImage(Image.open(window.filename).resize((640, 400), Image.ANTIALIAS))
    image = Label(window,image=selected_image).grid(row=4, column=0, columnspan=3)


def finish():
    window.quit()

def new_path():
    path = window.filename  #get the path
    path = path.split('/')  #split the string of path
    name = path[-1]         #isolaate the name
    name = name.split('.')  #split the name
    saved = str(name[0]) + '_filtered'      #change the name
    renamed = str(saved) + '.' + str(name[-1])
    path[-1] = renamed
    path = '/'.join(path)
    return path

def original():
    global selected_image
    selected_image = ImageTk.PhotoImage(Image.open(window.filename).resize((640, 400), Image.ANTIALIAS))
    image = Label(window,image=selected_image).grid(row=4, column=0, columnspan=3)

def split():
    split_image(window.filename, new_path())
    global selected_image
    selected_image = ImageTk.PhotoImage(Image.open(window.filename).resize((640, 400), Image.ANTIALIAS))
    image = Label(window,image=selected_image).grid(row=4, column=0, columnspan=3)

window = Tk()
window.configure(bg='#2eabbf')
window.geometry('1080x720')
window.title('Photo Splitting App')


title = Label(window,text='Photo Splitter', font= ['Anonymous', 28]).grid(row=0, column=0,columnspan=3)
browse_button = Button(window,text='Upload image',bg='yellow',fg='blue', command=open,font= ['Times New Roman', 16]).grid(row=1, column=1)

split_button = Button(window, command=split, text='Split',bg='red', font= ['Anonymous', 12],width=10).grid(row=2, column=0)
combine_button = Button(window,text='Combine',bg='green', font= ['Anonymous', 12],width=10).grid(row=2, column=2)

original_button = Button(window,text='Original',bg='green',fg='white', font= ['Anonymous', 12],width=10).grid(row=3, column=0)
exit_button = Button(window,text='Exit',bg='red',fg='white',command=finish, font= ['Anonymous', 12],width=10).grid(row=3, column=2)


window.mainloop()