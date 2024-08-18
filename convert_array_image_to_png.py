from PIL import Image
import numpy as np

# Image data
image_data = [
 
]

width = 
height = 

# Calculate the number of bits per line
bits_per_line = len(image_data) * 8 // height

# Convert the image data to a numpy array
image_array = np.unpackbits(np.array(image_data, dtype=np.uint8)).reshape((-1, bits_per_line))[:, :width].reshape((height, width))

# Create an image object from the array 从数组创建图像对象
image = Image.fromarray(image_array * 255, 'L')

# Save the image as a PNG file
image.save('output28.png')
