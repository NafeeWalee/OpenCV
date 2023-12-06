#========= 05-dec-2023 =========#
#========= run from cmd =========#
#python --version
#========= Python 3.12.0 =========#
#pip3 install opencv-contrib-python
#pip3 install caer


import cv2 as cv


#========= Function to change width-height =========#
def rescaleFrame(frame , scale = 0.20):
    # width & height are int
    width = int(frame.shape[1]*scale) # 1 is width
    height = int(frame.shape[0]*scale) # 2 is height


    return cv.resize(frame, (width,height), interpolation=cv.INTER_AREA)


#========= Read Images =========#
image = cv.imread('Photos/cat_large.jpg')

image_resized = rescaleFrame(image)
cv.imshow('Cat', image_resized)
cv.waitKey(0)

#========= Read Videos =========#
video = cv.VideoCapture('Videos/dog.mp4')

while True:
    isTrue, frame = video.read()
    frame_resized = rescaleFrame(frame)


    #cv.imshow('Video', frame)
    cv.imshow('Video', frame_resized)

    #break when letter 'd' is pressed
    if cv.waitKey(20) & 0xFF==ord('d'):           
        break

video.release()
cv.destroyAllWindows()
#error: (-215:Assertion failed) ===========> ran out of frame/ wrong path

