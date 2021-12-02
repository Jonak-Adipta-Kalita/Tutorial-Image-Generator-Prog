from tkinter import *
from tkinter import colorchooser, filedialog
from PIL import Image

root = Tk()
root.title("JAK Image Generator Prog")
root.geometry("712x508+300+100")
root.resizable(False, False)
root.iconbitmap("icon.ico")
root.configure(bg="green yellow")


##### Labels
color_label = Label(
    root, text="Color :", font=("arial", 20, "bold"), bg="green yellow"
).place(x=50, y=10)

extension_label = Label(
    root, text="Extension :", font=("arial", 20, "bold"), bg="green yellow"
).place(x=50, y=80)

width_label = Label(
    root, text="Width :", font=("arial", 20, "bold"), bg="green yellow"
).place(x=50, y=150)

height_label = Label(
    root, text="Height :", font=("arial", 20, "bold"), bg="green yellow"
).place(x=50, y=220)

number_label = Label(
    root, text="Images No. :", font=("arial", 20, "bold"), bg="green yellow"
).place(x=50, y=290)

image_name_label = Label(
    root, text="Name :", font=("arial", 20, "bold"), bg="green yellow"
).place(x=50, y=360)

convert_status_label = Label(
    root, text="", font=("arial", 20, "bold"), bg="green yellow"
).place(x=50, y=465)

##### Functions
def choose_color():
    color_code = colorchooser.askcolor()
    color_entry_box.delete(0, END)
    color_entry_box.insert(
        END,
        "{},{},{}".format(
            int(color_code[0][0]), int(color_code[0][1]), int(color_code[0][2])
        ),
    )


def create_image():
    color = color_entry_box.get()
    extension = extension_entry_box.get()
    name = image_name_entry_box.get()
    imagenumber = image_number_entry_box.get()
    width = int(width_entry_box.get())
    height = int(height_entry_box.get())
    url = filedialog.askdirectory()
    convert_single_btn.configure(
        text=f"{imagenumber} Creating Images"
    )
    col = color.split(",")
    colorname = []
    try:
        for i in col:
            colorname.append(int(i))
        colorname = tuple(colorname)
    except:
        colorname = col[0]
    for i in range(int(imagenumber)):
        path = url + "/{} {}{}".format(name, i + 1, extension)
        im = Image.new("RGB", (width, height), color=colorname)
        im.save(path)
    convert_single_btn.configure(
        text=f"{imagenumber} Images Created Sucessfully"
    )

##### Entry Boxes
color_entry_box = Entry(
    root,
    font=("arial", 14, "italic bold"),
    bg="blue",
    bd=5,
    justify="center",
    relief="ridge",
    foreground="yellow",
    selectbackground="white",
    selectforeground="black",
)
color_entry_box.insert(END, "255, 0, 0")
color_entry_box.place(x=230, y=10, height=45, width=350)

extension_entry_box = Entry(
    root,
    font=("arial", 20, "italic bold"),
    width=30,
    bg="blue",
    relief=RIDGE,
    bd=5,
    justify="center",
    selectbackground="white",
    selectforeground="black",
    fg="yellow",
)
extension_entry_box.insert(END, ".png")
extension_entry_box.place(x=230, y=80)

width_entry_box = Entry(
    root,
    font=("arial", 14, "italic bold"),
    bg="blue",
    relief=RIDGE,
    bd=5,
    justify="center",
    selectbackground="white",
    selectforeground="black",
    fg="yellow",
)
width_entry_box.insert(END, "800")
width_entry_box.place(x=230, y=150, height=45, width=460)

height_entry_box = Entry(
    root,
    font=("arial", 14, "italic bold"),
    bg="blue",
    relief=RIDGE,
    bd=5,
    justify="center",
    selectbackground="white",
    selectforeground="black",
    fg="yellow",
)
height_entry_box.insert(END, "800")
height_entry_box.place(x=230, y=220, height=45, width=460)

image_number_entry_box = Entry(
    root,
    font=("arial", 14, "italic bold"),
    bg="blue",
    relief=RIDGE,
    bd=5,
    justify="center",
    selectbackground="white",
    selectforeground="black",
    fg="yellow",
)
image_number_entry_box.insert(END, "5")
image_number_entry_box.place(x=230, y=290, height=45, width=460)

image_name_entry_box = Entry(
    root,
    font=("arial", 14, "italic bold"),
    bg="blue",
    relief=RIDGE,
    bd=5,
    justify="center",
    selectbackground="white",
    selectforeground="black",
    fg="yellow",
)
image_name_entry_box.insert(END, "Awesome Image")
image_name_entry_box.place(x=230, y=360, height=45, width=460)

##### Buttons
button = Button(
    root,
    text="Select Color",
    font=("arial", 10, " bold"),
    width=52,
    bd=5,
    relief=RIDGE,
    bg="red",
    activebackground="blue",
    activeforeground="white",
    command=choose_color,
)
button.place(x=590, y=10, height=45, width=100)

convert_single_btn = Button(
    root,
    text="Create Coloured Images",
    font=("arial", 15, " bold"),
    width=52,
    bd=5,
    relief=RIDGE,
    bg="red",
    activebackground="blue",
    activeforeground="white",
    command=create_image,
)
convert_single_btn.place(x=50, y=410, height=45)

root.mainloop()
