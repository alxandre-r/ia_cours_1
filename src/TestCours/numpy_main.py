import numpy as np
from PIL import Image

image = Image.open("../../datasets/20240824_154535.jpg")
image_data = np.array(image)

print("Height (x), width (y) and number of channel (rgb) of the image :", image_data.shape)

image_data[:,:, 2] = 0 #change value of b (of rgb) to 0
#B of rgb is 2 because it starts at 0 = r, 1=g, 2=b, 3=a (opacité)

print(image_data)

#save the image
processed_image = Image.fromarray(image_data)
processed_image.save("datasets/outputNumpy.jpg")


#-- Tests fait en cours
#new_array = np.array([[1,2], [3,4]])
#print("new_array is :",(new_array * 2))
#--
#sequence_data = np.arange(2,14)
#print("sequence_data is :", sequence_data)
#--
#sequence_data = sequence_data.reshape(6,2)
#print("After reshape, sequence_data is :",sequence_data)