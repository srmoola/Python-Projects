from tkinter import *
from tkinter.filedialog import askopenfile
from tkinter import messagebox
from PIL import ImageTk,Image
from Backend import * 
		


	
		
root = Tk()  # create root window
root.title("Dev's Photoshop")  # title of the GUI window
root.maxsize(1200, 720)  # specify the max size the window can expand to
root.config(bg="skyblue")  # specify background color

# Create left and right frames
left_frame = Frame(root, width=200, height=400, bg='grey')
left_frame.grid(row=0, column=0, padx=10, pady=5)

originalWidth = 120
editWidth = 650

image = Image.open("testimage.jpg")
img = ImageTk.PhotoImage(image)
wpercent = (originalWidth/float(image.size[0]))
hsize = int((float(image.size[1])*float(wpercent)))
original_img = image.resize((originalWidth,hsize), Image.Resampling.LANCZOS)


original_image = ImageTk.PhotoImage(original_img)




right_frame = Frame(root, width=650, height=400, bg='grey')
right_frame.grid(row=0, column=1, padx=10, pady=5)

# Create frames and labels in left_frame
Label(left_frame, text="Original Image", image = original_image).grid(row=0, column=0, padx=5, pady=5)

# load image to be "edited"
Label(right_frame, image=img).grid(row=0,column=0, padx=5, pady=5)




# Create tool bar frame
tool_bar = Frame(left_frame, width=180, height=185)
tool_bar.grid(row=2, column=0, padx=5, pady=5)

# Example labels that serve as placeholders for other widgets
Label(tool_bar, text="Tools", relief=RAISED).grid(row=0, column=0, padx=5, pady=3, ipadx=10)  # ipadx is padding inside the Label widget
Label(tool_bar, text="Filters", relief=RAISED).grid(row=0, column=1, padx=5, pady=3, ipadx=10)

# Example labels that could be displayed under the "Tool" menu
Label(tool_bar, text="Select").grid(row=1, column=0, padx=5, pady=5)
Label(tool_bar, text="Crop").grid(row=2, column=0, padx=5, pady=5)
Label(tool_bar, text="Rotate & Flip").grid(row=3, column=0, padx=5, pady=5)
Label(tool_bar, text="Resize").grid(row=4, column=0, padx=5, pady=5)
Label(tool_bar, text="Exposure").grid(row=5, column=0, padx=5, pady=5)
root.mainloop()

