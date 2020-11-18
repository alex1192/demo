import keyboard
import time
import pyautogui
import win32gui

def rgb(x, y):
		hdc = win32gui.GetWindowDC(win32gui.GetDesktopWindow())
		c = int(win32gui.GetPixel(hdc, x, y))
		return (c & 0xff), ((c >> 8) & 0xff), ((c >> 16), 0xff)

pyautogui.click(1046,602)
keyboard.send('space')
mv = 'right'
def move():
	keyboard.send(f'{mv}')
	time.sleep(0.12)

count = 0
while True:
	x,y = pyautogui.position()
	res = rgb(x,y)
	count+=1
	print(res)	

	if res[0] == 161 and res[1] == 116 and x == 1046 and y >= 602 or res[0] == 172 and res[1] == 165 and x == 1046 and y >= 602 or res[0] == 175 and res[1] == 221 and x == 1046 and y >= 602:
		keyboard.send('left')
		print('ушел налево')
		mv = 'left'
		pyautogui.click(873,602)	
	if res[0] == 161 and res[1] == 116 and x == 873 and y >= 602 or res[0] == 172 and res[1] == 165 and x == 873 and y >= 602 or res[0] == 175 and res[1] == 221 and x == 873 and y >= 602:
		keyboard.send('right')
		print('ушел направо')
		mv = 'right'
		pyautogui.click(1046,602)
	move()
	if count == 500:
		break
