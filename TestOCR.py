import time
from tkinter import *
from tkinter import scrolledtext

import PIL.Image
import cv2
import pyautogui
import pytesseract

window = Tk()

window.title("Text Extractor")

window.geometry('500x600')
txt = scrolledtext.ScrolledText(window, width=35, height=25)
txt.grid(column=3, row=4)


def quit():
    exit(0)


def extractext():
    window.wm_state('iconic')
    time.sleep(0.5)
    im1 = pyautogui.screenshot()
    im1.save('Fullsave.png')
    im = cv2.imread('Fullsave.png')
    r = cv2.selectROI(im)
    imCrop = im[int(r[1]):int(r[1] + r[3]), int(r[0]):int(r[0] + r[2])]

    gray = cv2.cvtColor(imCrop, cv2.COLOR_BGR2GRAY)

    cv2.imwrite("croppedImage.png", gray)
    text = pytesseract.image_to_string(PIL.Image.open('croppedImage.png'))

    txt.insert(INSERT, text)
    print(text)
    window.deiconify()


btn = Button(window, text="Extract !", command=extractext)
btn2 = Button(window, text="Quit !", command=quit)

btn2.grid(column=1, row=2)
btn.grid(column=1, row=1)

window.mainloop()
