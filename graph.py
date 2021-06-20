
import cv2
import numpy as np
import tkinter as tk
from tkinter import *
import os
import imutils
from tkinter import filedialog

window = Tk()
window.title("Welcome to shape detection")
window.geometry('800x500')
lbl = Label(window, text="Choose \nan image",bg = 'green',font = ('arial bond',50))
lbl.grid(column=0, row=0)

# Let's load a simple image with 3 black squares
def clicked():
    print("Choose an image")
    cv2.waitKey(0)
    root=tk.Tk()
    root.withdraw()
    imag=filedialog.askopenfilenames()#opening a dialog box
    imge=os.path.normpath(''.join(imag)) #converting
    image1=cv2.imread(imge)
    cv2.waitKey(0)
    r = 450.0 / image1.shape[1]
    dim = (450, int(image1.shape[0] * r))
    image = cv2.resize(image1, dim, interpolation=cv2.INTER_AREA)

    # Grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Find Canny edges
    edged = cv2.Canny(gray, 30, 200)
    cv2.waitKey(0)

    # Finding Contours
    # Use a copy of the image e.g. edged.copy()
    # since findContours alters the image
    contours, hierarchy = cv2.findContours(edged,
        cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    cv2.imshow('Canny Edges After Contouring', edged)
    cv2.waitKey(0)

    print("Number of Contours found = " + str(len(contours)))

    # Draw all contours
    # -1 signifies drawing all contours

    font=cv2.FONT_HERSHEY_TRIPLEX

    for cnt in contours:
        approx=cv2.approxPolyDP(cnt,0.05*cv2.arcLength(cnt,True),True)
        cv2.drawContours(image, [approx], 0, (0, 255, 0),2)
        print(len(approx))
        x=approx.ravel()[0]
        y = approx.ravel()[1]
        if len(approx) == 3:
            cv2.putText(image,"Triangle",(x,y),font,0.6,(255,0,255))
        elif len(approx) == 4:
            cv2.putText(image,"Rectangle",(x,y),font,0.6,(255,0,255))
        elif len(approx) == 5:
            cv2.putText(image,"Pentagon",(x,y),font,0.6,(255,0,255))
        elif len(approx) <10:
            cv2.putText(image,"Oval",(x,y),font,0.6,(255,0,255))
        else:
            cv2.putText(image,"Circle",(x,y),font,0.6,(255,0,255))


    cv2.imshow('Contours', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
btn = Button(window, text="Start", command=clicked,bg = 'yellow',font = ('arial bond',30))
btn.grid(column=5, row=5)

window.mainloop()
# import the necessary packages
import pyimagesearch
import imutils
import cv2
# load the image and resize it to a smaller factor so that
# the shapes can be approximated better
'''image = cv2.imread("C://Users\Maansi\PycharmProjects\shape_detect\shapes.png")
resized = imutils.resize(image, width=300)
ratio = image.shape[0] / float(resized.shape[0])

# convert the resized image to grayscale, blur it slightly,
# and threshold it
gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (5, 5), 0)
thresh = cv2.threshold(blurred, 60, 255, cv2.THRESH_BINARY)[1]

# find contours in the thresholded image and initialize the
# shape detector
cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
                        cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
sd = pyimagesearch.ShapeDetector()
# loop over the contours
for c in cnts:
    # compute the center of the contour, then detect the name of the
    # shape using only the contour
    M = cv2.moments(c)
    cX = int((M["m10"] / M["m00"]) * ratio)
    cY = int((M["m01"] / M["m00"]) * ratio)
    shape = pyimagesearch.ShapeDetector.detect(c)

    # multiply the contour (x, y)-coordinates by the resize ratio,
    # then draw the contours and the name of the shape on the image
    c = c.astype("float")
    c *= ratio
    c = c.astype("int")
    cv2.drawContours(image, [c], -1, (0, 255, 0), 2)
    cv2.putText(image, shape, (cX, cY), cv2.FONT_HERSHEY_SIMPLEX,
                0.5, (255, 255, 255), 2)

    # show the output image
    cv2.imshow("Image", image)
    cv2.waitKey(0)'''

