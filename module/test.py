import tkinter as tk
import PIL.Image
import PIL.ImageTk


root=tk.Tk()
root.title('test')
canvas=tk.Canvas(root,width=600,height=600)
canvas.create_image(300,150,image=tk.PhotoImage(file='Asset/shop/Button.png'),anchor='center')

im = PIL.Image.open("Asset/shop/Button.png")
photo = PIL.ImageTk.PhotoImage(im)

label = tk.Label(root, image=photo)
label.image = photo  # keep a reference!
label.place(x=300,y=150,anchor='center')



canvas.create_text(300,50,text='Museum',font=('Impact Regular',30,'bold'),fill='black')
canvas.pack()   
root.mainloop()