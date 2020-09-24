# Pencil-Sketching-and-cartoonization-with-Opencv
Created a Program which will help you to conver your image into a Pencil Sketch and cartoon sketch with the help of opencv.
So what i have done is 
read the image then with the help of kernel matrix i make the image little bit sharp so that it looks disturbed
then after this i converted it into greyscale image then created a inversion by doing 255-grey
then again little bit of blurring after removing it from the colors with the help of GaussianBlur then dividing the grey and the gaussian like removing the gaussian colors 
from the grey image and we will get the pencil sketch
now for cartoonization i used a class stylization to create a cartoon image
