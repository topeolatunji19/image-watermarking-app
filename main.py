from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageFont, ImageDraw


def watermark_image():
    # Reads the image to be copied with the line below
    image_path = file_path_entry.get()
    im = Image.open(image_path)

    # Shows detail about the image to be watermarked. It is optional
    # print(im.format, im.size, im.mode)

    # Opens the image to be copied. It is optional
    # im.show()

    watermark_type = watermark_type_entry.get().upper()
    if watermark_type == "T":
        # Watermarking a Text
        watermarked_image = im.copy()

        draw = ImageDraw.Draw(watermarked_image)

        # You can specify a different font type or font size below
        font_type = ImageFont.truetype("/Library/fonts/Arial.ttf", 60)

        watermark_text = watermark_text_entry.get()
        # You can change the color type using rbg in the fill variable below
        draw.text(xy=(300, 200), text=watermark_text, fill=(0, 0, 0), font=font_type)
        watermarked_image.show()

        # Saves the watermarked image in the directory below using the name "watermarked-image" as shown below.
        # User can specify another directory or filename here.
        watermarked_image.save("watermarked-images/watermarked-image.png")

    elif watermark_type == "L":
        # Watermarking a logo or image
        size = (500, 500)
        img_to_watermark = image_to_watermark_entry.get()
        crop_image = Image.open(img_to_watermark)
        crop_image.thumbnail(size)

        # add watermark
        watermarked_image = im.copy()
        watermarked_image.paste(crop_image, (500, 200))
        watermarked_image.show()

        # Saves the watermarked image in the directory below using the name "watermarked-image" as shown below.
        # User can specify another directory or filename here.
        watermarked_image.save("watermarked-images/watermarked-image.png")

    else:
        print("You have entered and invalid option")
        # watermark_image()


# Open a file and get the file name using dialog box
def open_file():
    filename = filedialog.askopenfilename(initialdir='/', title="Select a file", filetypes=[('Image Files',
                                                                                             '*jpeg *jpg *png')])
    file_path = filename
    get_file_name(file_path=file_path)


def select_watermark_image():
    filename = filedialog.askopenfilename(initialdir='/', title="Select a file", filetypes=[('Image Files',
                                                                                             '*jpeg *jpg *png')])
    get_watermark_image_path(filename=filename)


def get_watermark_image_path(filename):
    image_to_watermark_entry.delete(0, END)
    image_to_watermark_entry.insert(0, filename)
    return filename


# Get the file name that would be passed to the image processor
def get_file_name(file_path):
    file_path_entry.delete(0, END)
    file_path_entry.insert(0, file_path)
    return file_path


window = Tk()
window.title("Image Watermarking Application")
window.minsize(width=300, height=400)
window.config(padx=50, pady=50)

label_file_explorer = Label(window,
                            text="This is a desktop application to watermark an image either with text or another image",
                            width=60)
label_file_explorer.grid(column=1, row=1)

button_explore = Button(window,
                        text="Select File",
                        command=open_file)
button_explore.grid(column=1, row=2)

button_exit = Button(window,
                     text="Exit",
                     command=exit)
button_exit.grid(column=1, row=3)

file_path_label = Label(window, text="File Path")
file_path_label.grid(row=3, column=0)

file_path_entry = Entry(width=60)
file_path_entry.grid(row=3, column=1, columnspan=2)

watermark_type_label = Label(window, text="Enter watermark type. 'T' for Text and 'L' for Logo or Image: ")
watermark_type_label.grid(row=4, column=0)

watermark_type_entry = Entry(width=60)
watermark_type_entry.grid(row=4, column=1, columnspan=2)

watermark_text_label = Label(window, text="Enter the text you want watermarked: ")
watermark_text_label.grid(row=5, column=0)

watermark_text_entry = Entry(width=60)
watermark_text_entry.grid(row=5, column=1, columnspan=2)

image_to_watermark_label = Label(window, text="Select Image you want to use as watermark", width=50)
image_to_watermark_label.grid(column=0, row=6)

image_to_watermark_button = Button(window, text="Select File", command=select_watermark_image, width=12)
image_to_watermark_button.grid(column=1, row=6)

image_to_watermark_entry = Entry(width=60)
image_to_watermark_entry.grid(row=7, column=1)

watermark_action_button = Button(window, text="Add Watermark", command=watermark_image)
watermark_action_button.grid(row=8, column=1)

window.mainloop()

