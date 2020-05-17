import pyautogui # pip install pyautogui
from PIL import Image, ImageGrab # pip install pillow
import time

def isCollide(data):
	for i in range(760,800):
		for j in range(275,330):
			if data[i,j] < 100:
				hit('up')
				return

	for i in range(760,800):
		for j in range(200,276):
			if data[i,j]<100:
				hit('down')
				return
	return

def hit(key):
    pyautogui.keyDown(key)
    return

if __name__ == "__main__":
	time.sleep(5)
	hit("space")
	while True:
		image = ImageGrab.grab().convert('L')
		data=image.load()
		isCollide(data)
		#print(image)
		#for i in range(760,800):
		#	for j in range(200,270):
		#		data[i,j]=25
		#break
		

	image.show()