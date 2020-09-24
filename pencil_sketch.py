# importing the library
import cv2
import numpy
# reading the image
image=cv2.imread("averaged_frame.jpg")
# making the image sharp
# blurring the image in a negative way
# making it sharp so that it will look some disturbed
# using this kernel matrix
kernel=numpy.array([[-1,-1,-1],
                    [-1,9,-1],
                    [-1,-1,-1]])
sharp=cv2.filter2D(image,-1,kernel=kernel)
# now converting that disturbed image into grey scale
grey=cv2.cvtColor(sharp,cv2.COLOR_BGR2GRAY)
# removing the colors as 255 means white so removing everything from white
inversion=255-grey
# blurring the inversion one
gauss=cv2.GaussianBlur(inversion,ksize=(15,15),sigmaX=0,sigmaY=0)
# diving the grey and color inversion gauss
pencil=cv2.divide(grey,255-gauss,scale=256)
cv2.imshow("Pencil Sketch",pencil)
# cartoonization of the image
cartoon=cv2.stylization(image,sigma_s=150,sigma_r=0.25)
cv2.imshow("Cartoon Image",cartoon)
cv2.waitKey(0)
cv2.destroyAllWindows()