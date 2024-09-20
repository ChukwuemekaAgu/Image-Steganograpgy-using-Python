# Python program implementing Image Steganography 
from tkinter import *
from tkinter import filedialog
import tkinter as tk
# PIL module is used to extract pixels of image and modify it 
from PIL import Image, ImageTk 
import os

##==================================Open_btn Function=====================================================================#
def openFile():
 global path
 path = filedialog.askopenfilename(filetypes=[("Image File",'png')])
 im = Image.open(path)
 tkimage = ImageTk.PhotoImage(im)
 myvar=Label(UpFrame2,image = tkimage)
 myvar.image = tkimage
 myvar.pack()
 showTxt["text"] = str(path) if path else showTxt
# Convert encoding data into 8-bit binary 
# form using ASCII value of characters 
def genData(data): 	
		# list of binary codes 
		# of given data 
		newd = []
		for i in data: 
			newd.append(format(ord(i), '08b')) 
		return newd 	
# Pixels are modified according to the 
# 8-bit binary data and finally returned 
def modPix(pix, data): 
	datalist = genData(data) 
	lendata = len(datalist) 
	imdata = iter(pix) 
	for i in range(lendata): 
		# Extracting 3 pixels at a time 
		pix = [value for value in imdata.__next__()[:3] + imdata.__next__()[:3] + imdata.__next__()[:3]] 						
		# Pixel value should be made 
		# odd for 1 and even for 0 
		for j in range(0, 8): 
			if (datalist[i][j]=='0') and (pix[j]% 2 != 0): 
				if (pix[j]% 2 != 0): 
					pix[j] -= 1
			elif (datalist[i][j] == '1') and (pix[j] % 2 == 0): 
				pix[j] -= 1
		# Eighth pixel of every set tells 
		# whether to stop ot read further. 
		# 0 means keep reading; 1 means the 
		# message is over. 
		if (i == lendata - 1): 
			if (pix[-1] % 2 == 0): 
				pix[-1] -= 1
		else: 
			if (pix[-1] % 2 != 0): 
				pix[-1] -= 1
		pix = tuple(pix) 
		yield pix[0:3] 
		yield pix[3:6] 
		yield pix[6:9] 
def encode_enc(newimg, data): 
	w = newimg.size[0] 
	(x, y) = (0, 0) 
	for pixel in modPix(newimg.getdata(), data): 
		# Putting modified pixels in the new image 
		newimg.putpixel((x, y), pixel) 
		if (x == w - 1): 
			x = 0
			y += 1
		else: 
			x += 1
# Encode data into image 
def encode(): 
	img = os.path.basename(path) 
	image = Image.open(img, 'r') 
	data = showTxt_1.get()
	if (len(data) == 0): 
		raise ValueError('Data is empty') 
	newimg = image.copy() 
	encode_enc(newimg, data) 
	new_img_name = showTxt_10.get()
	newimg.save(new_img_name, str(new_img_name.split(".")[1].upper())) 
# Decode the data in the image 
def decode():
	img = os.path.basename(path)
	image = Image.open(img, 'r') 
	data = '' 
	imgdata = iter(image.getdata()) 
	while (True): 
		pixels = [value for value in imgdata.__next__()[:3] +
								imgdata.__next__()[:3] +
								imgdata.__next__()[:3]] 
		# string of binary data 
		binstr = '' 
		for i in pixels[:8]: 
			if (i % 2 == 0): 
				binstr += '0'
			else: 
				binstr += '1'
				
		data += chr(int(binstr, 2))
		showTxt_2["text"] = str(data) if data else showTxt_2
		if (pixels[-1] % 2 != 0):
			return data
##____________________________________________________________________________________________________________#############
root = tk.Tk()
root.title("Image Steganography")
root.geometry('580x700+0+0')
root.configure(background='black')
UpFrame = Frame(root, width=580, height=700)
UpFrame.pack()

UpFrame1 = Frame(UpFrame)
UpFrame1.pack(side=TOP)
UpFrame2 = Frame(UpFrame, width=580, height=350, bg="ghostwhite")
UpFrame2.pack(side=TOP)
UpFrame3 = Frame(UpFrame, width=580, height=350)
UpFrame3.pack(side=TOP)

# ===================================UpFrame1=================================================================================================#
labelTitle = Label(UpFrame1, text="EMEKA'S SECURE SHELL", width=23, fg="#000000", bg="#33B5E5", font=('Algerian', 29, 'bold'))
labelTitle.pack()

# ===================================UpFrame2=================================================================================================#



# ===================================UpFrame3=================================================================================================#
Open_btn = Button(UpFrame3, text='Upload Image',fg="#000000", bg="#33B5E5",font=('Garamond', 10, 'bold'), 
   command = openFile)
Open_btn.pack()
showTxt = Label(UpFrame3,fg="#011011",bg="#ffffff",width=40, font=('Garamond', 12, 'bold'))
showTxt.pack()

##==============================================================================================================================================#
labelMsg_100 = Label(UpFrame3, font=('Garamond', 10, 'bold'))
labelMsg_100.pack()

##==============================Enter Message==================================================================================================#
labelMsg_1 = Label(UpFrame3, font=('Garamond', 10, 'bold'), text="Input Message")
labelMsg_1.pack()
showTxt_1 = tk.Entry(UpFrame3,width=60)
showTxt_1.pack()

##==============================Enter Stego/New Image Name================================================================================================#
labelMsg_10 = Label(UpFrame3, font=('Garamond', 10, 'bold'), text="Input Stego-Image Name(.png)")
labelMsg_10.pack()
showTxt_10 = tk.Entry(UpFrame3,width=60)
showTxt_10.pack()

##==============================View Decoded Message==================================================================================================#
labelMsg_2 = Label(UpFrame3, font=('Garamond', 10, 'bold'), text="View Decoded Message")
labelMsg_2.pack()
showTxt_2 = Label(UpFrame3,fg="#011011",bg="#ffffff",width=40, font=('Garamond', 12, 'bold'))
showTxt_2.pack()

##============================================================================================================================================#
labelMsg_101 = Label(UpFrame3, font=('Garamond', 10, 'bold'))
labelMsg_101.pack()

##==============================Encode Button==================================================================================================#
Encode_btn = Button(UpFrame3, text='Encode',  fg="#011011", bg="#33b5e5",
 font=('Times New Roman', 12, 'bold'), command = encode)
Encode_btn.pack(side=LEFT)

##==============================Decode Button==================================================================================================#
Decode_btn = Button(UpFrame3, text='Decode',  fg="#011011", bg="#00C853",
 font=('Times New Roman', 12, 'bold'),  command = decode)
Decode_btn.pack(side=RIGHT)


root.mainloop()
