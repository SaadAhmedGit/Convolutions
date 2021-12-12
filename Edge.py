import numpy as np
from PIL import Image

sobel_x = np.array( [ [-1, 0, 1],
                      [-2, 0, 2],
                      [-1, 0, 1] ] )

sobel_y = np.array( [ [-1,-2,-1],
                      [ 0, 0, 0],
                      [ 1, 2, 1] ] )


img = np.array(Image.open('motor.png').convert('L'))
img_height = img.shape[0]
img_width = img.shape[1]

img_xy = np.empty((img_height,img_width))

for i in range(img_height-2):
    for j in range(img_width-2):
        edge_x = np.sum(np.multiply(sobel_x, img[i:i + 3, j:j + 3]))
        edge_y = np.sum(np.multiply(sobel_y, img[i:i + 3, j:j + 3]))
        img_xy[i+1][j+1] = np.sqrt(edge_x**2 + edge_y**2)

final = Image.fromarray(img_xy).convert('L')
final.save('motor-edged.png')
final.show()
