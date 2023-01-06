from tkinter import *
from tkinter import filedialog
from moviepy import *

# functions
def select_path():
    # allows user to select path
    path = filedialog.askdirectory()
    path_label.config(text=path)

screen = Tk()
title = screen.title('Youtube Download')
canvas = Canvas(screen, width=500, height=500)
canvas.pack()

#image logo
logo_img = PhotoImage(file='youtube_downloader\yt.png')
#resize
logo_img = logo_img.subsample(2, 2)
canvas.create_image(250, 80, image=logo_img)

#link field
link_field = Entry(screen, width=40, font=('Arial', 15) )
link_label = Label(screen, text="Enter Download Link: ", font=('Arial', 15))

# select path
path_label = Label(screen, text="Select Path For Download", font=('Arial', 15))
select_btn =  Button(screen, text="select", command=select_path, font=('Arial', 15))

#Add to window
canvas.create_window(250, 280, window=path_label)
canvas.create_window(250, 330, window=select_btn)

#Add widgets to window 
canvas.create_window(250, 170, window=link_label)
canvas.create_window(250, 220, window=link_field)

#Download btns
download_btn = Button(screen, text="Download File", font=('Arial', 15))
#add to canvas
canvas.create_window(250, 390, window=download_btn)

screen.mainloop()