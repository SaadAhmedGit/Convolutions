import numpy as np
from PIL import Image

def convolute(kernel,convo_img,normalizer,reference,i,j):
    sum = 0
    for k in range(i, i+3):
        for l in range(j, j+3):
            sum += (reference[k][l] * kernel[k-i][l-j])
    sum = abs(sum)/normalizer
    for k in range(i, i+3):
        for l in range(j, j+3):
            if(sum > 120):
                convo_img[k][l] = 255
            else:
                convo_img[k][l] = 0

sobel_x = np.array( [ [-1, 0, 1],
                      [-2, 0, 2],
                      [-1, 0, 1] ] )

sobel_y = np.array( [ [-1,-2,-1],
                      [ 0, 0, 0],
                      [ 1, 2, 1] ] )


img = np.array(Image.open('motor.png').convert('L'))
img_height = img.shape[0]-2
img_width = img.shape[1]-2


img_xy = np.empty((img_height+2,img_width+2))
img_x = np.empty((img_height+2,img_width+2))
img_y = np.empty((img_height+2,img_width+2))

        
for i in range(0,img_height,1):
    for j in range(0,img_width,1):
        convolute(sobel_x, img_x, 1, img, i, j)
        convolute(sobel_y, img_y, 1, img, i, j)
        if(img_x[i][j] + img_y[i][j] >= 255):
            img_xy[i][j] = 192
        else:
            img_xy[i][j] = 0
        
Image.fromarray(img_xy).convert('L').save('edged-motor.png')
