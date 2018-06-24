import cv2
from cv2 import imshow
from time import sleep
import _thread
from datetime import datetime as dt

from tkinter import *

camera = cv2.VideoCapture(0)
import pickle

global value
value = 127
global save_image
save_image = False

def on_the_side(a):
	while False:
		pickle.dump(value,open("value.pkl","wb"))

	root = Tk()
	root.title("example")
	root.configure(bg="maroon")
	root.geometry("360x480")

	promptForSlider = Label(root, text="Slide to change value of thershold : ", bg = '#1976d2', fg = '#212121', font=("arial", 16, 'bold'), height = '2')
	promptForSlider.pack(fill=X,padx='1',pady='3')

	def send_value(sld_value):
		global value
		value = sld_value

	slider = Scale(root, from_=0, to=254, orient=HORIZONTAL, command=send_value)
	slider.pack(fill=X,padx='1',pady='3')

	def save_image():
		global save_image
		save_image = True

	btn = Button(root, text=" Enter ", bg = '#ff9800', command=save_image, font=("arial", 16, 'bold'), height = '2')
	btn.config(activebackground = '#ff7800')
	btn.pack(fill=X,padx='1',pady='3')
	root.mainloop()

_thread.start_new_thread(on_the_side,(1,))

while(True):

	image = camera.read()[1]
	#value = pickle.load(open("value.pkl","rb"))


	image_gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
	_, art_image = cv2.threshold(image_gray,int(value),255,cv2.THRESH_BINARY)

	if save_image == True:
		file_with_date = str(dt.now())[:19] + ".jpeg"
		cv2.imwrite(file_with_date,art_image)
		save_image = False

	cv2.imshow("Video",art_image)
	if cv2.waitKey(10) == ord('q'):
		break
	sleep(0.03)


"""
cv.ADAPTIVE_THRESH_MEAN_C

cv.ADAPTIVE_THRESH_GAUSSIAN_C


"""
