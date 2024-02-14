#!/usr/bin/python

from PIL import Image
from io import BytesIO
import numpy as np

#image = 'sunny.png'
#image = 'cloudy.png'
#image = 'rainy.png'
images = ['sunny.png', 'cloudy.png', 'rainy.png']
imgdir = './'

w = 40
h = 40
threshold = 10

for image in images:
	print(image)
	img = Image.open(f"{imgdir}/{image}")
	img_resized = img.resize((w, h))
	#img_resized.show()
	img_mono = img_resized.convert("L")
  
	img_array = np.where(np.asarray(img_mono) > threshold, 1, 0)
	#img_mono.show()

	for y in range(h):
		for x in range(w):
			print("{}".format("xx" if img_array[y][x] else ".."), end='')
		print()

	file = image.replace('.png', '.dat')
	with open(f"{imgdir}/weather_dats/{file}", 'w') as f:
		for y in range(h):
			for x in range(w):
				f.write(str(img_array[y][x]))
			f.write("\n")
		f.close()
	print(f"saved to {imgdir}/weather_dats/{file}")
