# -*- coding: utf-8 -*-
"""
Created on Sat Feb  8 14:27:15 2020

@author: Taha
"""

#Libraries
################################
import cv2 as cv
################################


class Cropper():
    GREEN = [0,255,0]        # Bounding Box Color

    # setting up flags
    rect = (0,0,1,1)
    rectangle = False       # flag for drawing rect
    rect_over = False       # flag to check if rect drawn
    
    def onmouse(self, event, x, y, flags, param):
        # Draw Rectangle
        if event == cv.EVENT_RBUTTONDOWN:
            self.rectangle = True
            self.ix, self.iy = x,y

        elif event == cv.EVENT_MOUSEMOVE:
            if self.rectangle == True:
                self.img = self.img2.copy()
                cv.rectangle(self.img, (self.ix, self.iy), (x, y), self.GREEN, 2)
                self.rect = (min(self.ix, x), min(self.iy, y), abs(self.ix - x), abs(self.iy - y))
                self.rect_or_mask = 0

        elif event == cv.EVENT_RBUTTONUP:
            self.rectangle = False
            self.rect_over = True
            cv.rectangle(self.img, (self.ix, self.iy), (x, y), self.GREEN, 2)
            self.rect = (min(self.ix, x), min(self.iy, y), abs(self.ix - x), abs(self.iy - y))
            self.rect_or_mask = 0

    def process_image(self, image):

        self.img = image.copy()
        self.img2 = self.img.copy()                               
        cv.namedWindow('input')
        cv.setMouseCallback('input', self.onmouse)

        print("Draw A Bounding Box By Holding Down Right Mouse Button. Press Esc when Done \n")
        
        while(1):
            cv.imshow('input', self.img)
            k = cv.waitKey(1)
             
            # key bindings
            if k == 27:         # esc to exit
                break
        
        # rect = (x1,y1,x2,y2)
        self.rect = (self.rect[0], self.rect[1], self.rect[0]+self.rect[2], self.rect[1]+self.rect[3])
        return image[self.rect[1]:self.rect[3], self.rect[0]:self.rect[2]], self.rect

