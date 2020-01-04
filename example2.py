# import the necessary packages
from collections import namedtuple
import numpy as np
import cv2

# define the `Detection` object
Detection = namedtuple("Detection", ["image_path", "gt", "pred"])

def jaccard_similarity(boxA, boxB):
	# determine the (x, y)-coordinates of the intersection rectangle
	xA = max(boxA[0], boxB[0])
	yA = max(boxA[1], boxB[1])
	xB = min(boxA[2], boxB[2])
	yB = min(boxA[3], boxB[3])

	# compute the area of intersection rectangle
	interArea = max(0, xB - xA + 1) * max(0, yB - yA + 1)

	# compute the area of both the prediction and ground-truth
	# rectangles
	boxAArea = (boxA[2] - boxA[0] + 1) * (boxA[3] - boxA[1] + 1)
	boxBArea = (boxB[2] - boxB[0] + 1) * (boxB[3] - boxB[1] + 1)

	# compute the Jaccard Index value by taking the intersection
	# area and dividing it by the sum of prediction + ground-truth
	# areas - the interesection area
	jaccard_index = interArea / float(boxAArea + boxBArea - interArea)

	# return the Jaccard Index value value
	return jaccard_index

# define the list of example detections
examples = [
	Detection("demo.jpg", [39, 63, 203, 112], [54, 66, 198, 114])
]

# loop over the example detections
for detection in examples:
	# load the image
	image = cv2.imread(detection.image_path)

	# draw the ground-truth bounding box along with the predicted
	# bounding box
	cv2.rectangle(image, tuple(detection.gt[:2]), 
		tuple(detection.gt[2:]), (0, 255, 0), 2)
	cv2.rectangle(image, tuple(detection.pred[:2]), 
		tuple(detection.pred[2:]), (0, 0, 255), 2)

	# compute the Jaccard Index value and display it
	jaccard_index = jaccard_similarity(detection.gt, detection.pred)
	cv2.putText(image, "Jaccard index: {:.4f}".format(jaccard_index), (10, 30),
		cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
	print("{}: {:.4f}".format(detection.image_path, jaccard_index))

	# show the output image
	cv2.imshow("Image", image)
	cv2.waitKey(0)