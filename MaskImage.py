#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cv2
import numpy as np
print(cv2.__version__)

def main():
	width,height = 1280, 720;
	color = [255,255,255]
	im = np.full((height,width,3),color,dtype=np.uint8)
	# im = cv2.imread('img/image.png')
	mask = np.array(
		[
		[0, 250],
		[0, 720],
		[1280, 720],
		[1280, 250],
		[1000, 560],
		[330, 560],
		]
	)
	cv2.fillPoly(im, pts=[mask], color=(0, 0, 0))   
	cv2.imwrite('result.jpg', im)

if __name__ == '__main__':
	main()