from tkinter import *
from tkinter import filedialog
from PIL import ImageTk,Image
from PIL import Image
import skimage as sm
from skimage.color import rgb2gray
from skimage import io
from filters.blur import guassian_blur
from filters.sharp import sharpen
from  filters.border import border_20px
from filters.intensity import intensity_2bit
from filters.posterize import posterize_3bit
from filters.sketch import sketching_function
from filters.equalize import equalization_function

def open():
    global selected_image
    window.filename = filedialog.askopenfilename(initialdir="/", title="Select file",filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))
    selected_image = ImageTk.PhotoImage(Image.open(window.filename).resize((640, 400), Image.ANTIALIAS))
    image = Label(window,image=selected_image).grid(row=7, column=0, columnspan=3)


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

#the following function will save a duplicate file and we will work with that file in the future
def save_image():

    # creating a image object (main image)
    im1 = io.imread(window.filename)
    im1 = rgb2gray(im1)
    im1=sm.img_as_int(im1)

    # save a image using extension
    io.imsave(new_path(),im1)

    global selected_image
    selected_image = ImageTk.PhotoImage(Image.open(new_path()).resize((640, 400), Image.ANTIALIAS))
    image = Label(window,image=selected_image).grid(row=7, column=0, columnspan=3)

def original():
    global selected_image
    selected_image = ImageTk.PhotoImage(Image.open(window.filename).resize((640, 400), Image.ANTIALIAS))
    image = Label(window,image=selected_image).grid(row=7, column=0, columnspan=3)

def blur():
    guassian_blur(window.filename, new_path())

    global selected_image
    selected_image = ImageTk.PhotoImage(Image.open(new_path()).resize((640, 400), Image.ANTIALIAS))
    image = Label(window,image=selected_image).grid(row=7, column=0, columnspan=3)

def sharp():
    sharpen(window.filename, new_path())

    global selected_image
    selected_image = ImageTk.PhotoImage(Image.open(new_path()).resize((640, 400), Image.ANTIALIAS))
    image = Label(window,image=selected_image).grid(row=7, column=0, columnspan=3)

def border():
    border_20px(window.filename, new_path())
    global selected_image
    selected_image = ImageTk.PhotoImage(Image.open(new_path()).resize((640, 400), Image.ANTIALIAS))
    image = Label(window,image=selected_image).grid(row=7, column=0, columnspan=3)

def intensity():
    intensity_2bit(window.filename, new_path())
    global selected_image
    selected_image = ImageTk.PhotoImage(Image.open(new_path()).resize((640, 400), Image.ANTIALIAS))
    image = Label(window,image=selected_image).grid(row=7, column=0, columnspan=3)

def posterize():
    posterize_3bit(window.filename, new_path())
    global selected_image
    selected_image = ImageTk.PhotoImage(Image.open(new_path()).resize((640, 400), Image.ANTIALIAS))
    image = Label(window,image=selected_image).grid(row=7, column=0, columnspan=3)

def sketch():
    sketching_function(window.filename, new_path())
    global selected_image
    selected_image = ImageTk.PhotoImage(Image.open(new_path()).resize((640, 400), Image.ANTIALIAS))
    image = Label(window,image=selected_image).grid(row=7, column=0, columnspan=3)

def equalize():
    equalization_function(window.filename, new_path())
    global selected_image
    selected_image = ImageTk.PhotoImage(Image.open(new_path()).resize((640, 400), Image.ANTIALIAS))
    image = Label(window,image=selected_image).grid(row=7, column=0, columnspan=3)

window = Tk()
window.configure(bg='#2eabbf')
window.geometry('720x1080')
window.title('DP Filter App')


title = Label(window,text='  DP Filter App', font=['Times New Roman', 38,'bold']).grid(row=0, column=1,columnspan=2)
browse_button = Button(window,text='Upload image',bg='#fa90a4',fg='white', command=open,font= ['Times New Roman', 16]).grid(row=1, column=1, columnspan=2)

blur_button = Button(window,text='Blur',command=blur,bg='#33c4ff', font= ['Anonymous', 12],width=10).grid(row=2, column=1)
sharp_button = Button(window,text='Sharp',command=sharp, font= ['Anonymous', 12],width=10).grid(row=3, column=1)
sketch_button = Button(window,command=sketch,text='Sketch',bg='#33c4ff', font= ['Anonymous', 12],width=10).grid(row=4, column=1)
posterize_button = Button(window,text='Posterize', command=posterize, font= ['Anonymous', 12],width=10).grid(row=5, column=1)
intensity_button = Button(window,command=intensity, text='Intensity',bg='#33c4ff', font= ['Anonymous', 12],width=10).grid(row=2, column=2)
border_button = Button(window, command=border, text='Border', font= ['Anonymous', 12],width=10).grid(row=3, column=2)
equalize_button = Button(window, command=equalize, text='Equalize',bg='#33c4ff', font= ['Anonymous', 12],width=10).grid(row=4, column=2)
gray_scale = Button(window,text='Gray Scale',command=save_image, font= ['Anonymous', 12],width=10).grid(row=5, column=2)

original_button = Button(window,text='Original',command= original,bg='#ffdde2',fg='black', font= ['Anonymous', 12],width=10).grid(row=6, column=1)
exit_button = Button(window,text='Exit',bg='black',fg='white',command=finish, font= ['Anonymous', 12],width=10).grid(row=6, column=2)


window.mainloop()