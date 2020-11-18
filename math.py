import cv2, pytesseract, os, time, pyautogui,keyboard
from PIL import Image
import pyscreenshot as ImageGrab
import matplotlib.pyplot as plt


def image():
	im=ImageGrab.grab(bbox=(530,400,710,460))
	im_res=ImageGrab.grab(bbox=(530,460,710,510))
	im.save('1.png')
	im_res.save('2.png')

def char(x):
	for i in arr[0]:
		if i == 'x' or i == '-' or i == '/' or i == '+':
			s = arr[0].split(i)
			s.append(i)
			res = arr[1].replace('=','')
			s.append(res)
	s[1],s[2] = s[2],s[1]
	print(s)
	if s[1] == '+':
		res = int(s[0])+int(s[2])
		itog = int(s[3])
		print(res,'==', itog)
		if res == itog:
			print('верно')
		else:
			print('неверно')
	if s[1] == '-':
		res = int(s[0])-int(s[2])
		itog = int(s[3])
		print(res,'==', itog)
		if res == itog:
			print('верно')
		else:
			print('неверно')
	if s[1] == 'x':
		res = int(s[0])*int(s[2])
		itog = int(s[3])
		print(res,'==', itog)
		if res == itog:
			print('верно')
		else:
			print('неверно')
	if s[1] == '/':
		res = int(s[0])/int(s[2])
		itog = int(s[3])
		print(res,'==', itog)
		if res == itog:
			print('верно')
		else:
			print('неверно')
	if int(res) == itog:
		keyboard.send('left')
	else:
		keyboard.send('right') 
pyautogui.click(400,900)
keyboard.send('space')
while True:
	image()
	arr =[]
	string=''
	preprocess = "thresh"
	pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
	i = 1
	while i < 3:
		img = cv2.imread(f'{i}.png')
		img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

		config = r'--oem 3 -c tessedit_char_whitelist=0123456789+-/x  --psm 10'
		img = pytesseract.image_to_string(img, config=config)
		arr.append(img)
		i+=1
	arr = [line.rstrip() for line in arr]
	char(arr[0])