import cv2
from PIL import Image
from pytesseract import image_to_string
import pyttsx as speak
from time import sleep


IMAGE_FILE = 'imageToRead.tif'

flag = 0

def say(tosay):
    speaker = speak.init()
    speaker.setProperty('rate',120)
    speaker.setProperty('voice', 'english-us')
    speaker.say(tosay)
    a = speaker.runAndWait()

# loop forever

say("Blind Reader Started")
print("Blind Reader Started")

while True:

    flag = flag + 1


    cam2 = cv2.VideoCapture(0)
    img1 = cam2.read()[1]
    cam2.release()

    cv2.imwrite(IMAGE_FILE, img1)

    img1 = Image.open(IMAGE_FILE)
    img2 = img1.convert('L')
    img2.save('grey.tif')

    print "::::::::::::::::::::::::::::::" + str(flag) + "::::::::::::::::::::::::::::::"
    words = None
    words = image_to_string(img1).strip()
    if words:
        print words
        say(words)

    sleep(2)
