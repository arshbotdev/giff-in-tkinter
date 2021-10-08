import tkinter as tk
from PIL import Image

root =tk.Tk()
file='animation.gif'


info =Image.open(file)
frames=info.n_frames
print(frames)

im=[tk.PhotoImage(file=file,format=f'gif -index {i}') for i in range(frames)]


count=0
def animation(count):
    im2=im[count]
    gif_label.configure(image=im2)


    count+=1
    if count == frames:
        count=0

    root.after(20,lambda:animation(count))



gif_label=tk.Label(image='')
gif_label.pack()

animation(count)
root.mainloop()

