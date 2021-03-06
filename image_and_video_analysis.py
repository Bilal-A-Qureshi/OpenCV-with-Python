import cv2
import numpy as np
import matplotlib.pyplot as plt

# for image
# img = cv2.imread('watch.jfif', cv2.IMREAD_GRAYSCALE)
#
# # cv2.imshow('img', img)
# # cv2.waitKey(0)
# # cv2.destroyAllWindows()
#
# plt.imshow(img, cmap='gray', interpolation='bicubic')
# plt.plot([50,100],[80,100],'c', linewidth=5)
# plt.show()


# for video
cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (540,480))

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow('gray',gray)
    cv2.imshow('frame',frame)

    if cv2.waitKey(1) & 0xFF==ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()
 
