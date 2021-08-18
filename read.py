import cv2 as cv

# Reading images in openCV
# img =cv.imread('Photos/cat_large.jpg')
# cv.imshow('Cat', img)
# cv.waitKey(0)

# Reading videos in openCV
capture = cv.VideoCapture('Videos/dog.mp4')

while True:
    isTrue, frame = capture.read()
    cv.imshow('Video', frame)

    if cv.waitKey(20) & 0xF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()


