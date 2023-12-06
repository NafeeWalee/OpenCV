import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3),dtype='uint8') #height, width, color channels, image type
#cv.imshow('Empty',blank)


#draw image
blank[100:400, 0:500] = 0,255,0

#draw rectanagle
cv.rectangle(blank,(0,0),(500,500),(100,100,255), thickness=5) # -1 or cv.FILLED to fill the rectangle with color
#cv.rectangle(blank,(0,0),(blank.shape[1]//2,blank.shape[0]//2),(255,0,0), thickness= cv.FILLED) # blank.shape[1]//2 similar to mediaquery, half size of it's parent

#draw circle
cv.circle(blank, (blank.shape[1]//2,blank.shape[0]//2), 60, (0,0,255),thickness= -1) # radius 40 & position is in center 

#draw line
cv.line(blank, (220,220) , (280,280), (255,255,255), thickness=2)
cv.line(blank, (280,220) , (220,280), (255,255,255), thickness=2)

#write text
cv.putText(blank,'Bangladesh?',(50,350),cv.FONT_HERSHEY_COMPLEX, 1.0, (155,120,220),thickness=2)

cv.imshow('Color',blank)
cv.waitKey(0)