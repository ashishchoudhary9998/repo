import cv2
from PIL import Image
from pytesseract import image_to_string
import pyttsx as speak
from time import sleep


#IMAGE_FILE = 'imageToRead.jpeg'


flag = 0
print "Defining say()"

def say(tosay):
	speaker = speak.init()
	speaker.setProperty('rate',150)
	speaker.setProperty('voice', 'english-us')
	speaker.setProperty('gender', 'female')
	speaker.say(tosay)
	a = speaker.runAndWait()

# loop forever

say("Blind Reader Started")
print("Blind Reader Started")


while True:

	flag = flag + 1

	try:

		camera = cv2.VideoCapture(0)

		for i in xrange(5):
			temp = camera.read()
			sleep(0.05)

		img1 = camera.read()[1]
		cv2.imshow("Video", img1)
		if cv2.waitKey(10) == ord('q'):
			break
			camera.release()
		camera.release()

		#convert image array to bytes image
		img1 = Image.fromarray(img1)
		img2 = img1.convert('L')
		print ":" + str(flag) + ":"
		words = None
		words = image_to_string(img2).strip()
		if words:
			print "Words are : "
			print words
			say(words)

	except KeyboardInterrupt:
		print "^C pressed."
		print "Resources Cleared."
		camera.release()
	except:
		print "Something Else occured."
		print "Resources Cleared."
		camera.release()

	sleep(1)

#anirudhvyas230897@gmail.com

#senacha.mahendra@gmail.com

