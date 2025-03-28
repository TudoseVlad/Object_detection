import cv2
import numpy as np
import Image_preview  as IP
def Yolo(precision, pic):
	#Loading Yolo
	net = cv2.dnn.readNet("yolov3.weights","yolov3.cfg")	
	layer_names = net.getLayerNames()
	outputlayes = [layer_names[ i[0]-1 ] for i in net.getUnconnectedOutLayers()]
	#image Load
	img = cv2.imread(pic)
	#img = cv2.resize(img , None , fx = 0.4 , fy = 0.4)
	height, width, channels = img.shape
	class_ids = []
	confidences = []
	boxes = [] 
	#Object Detection
	# image used, scale factor, image size, mean , RGB swap(opencv work with BGR format), crop()
	blob = cv2.dnn.blobFromImage(img, 0.00392, (416,416), (0,0,0), True, crop= False)
	net.setInput(blob)
	outs =net.forward(outputlayes)

	# Show info

	for out in outs:
			for detection in out:
				scores = detection[5:]
				class_id = np.argmax(scores)
				confidence  = scores[class_id]
				if confidence > precision:
					#Object detected
						center_x = int(detection[0] * width)
						center_y = int(detection[1] * height)
						w= int(detection[2]*width)
						h= int(detection[3]*height)
						#Rectangle Transformation
						x = int(center_x - w / 2)
						y = int(center_y - h / 2)
						boxes.append([x,y,w,h])
						confidences.append(float(confidence))
						class_ids.append(class_id)
					cv2.rectangle(img, (x,y), (x + w, y+ h), (0,255, 0), 2)
	
	cv2.namedWindow("Toate obiectele detectate", cv2.WINDOW_NORMAL)
	cv2.resizeWindow("Toate obiectele detectate", 1366, 768)
	cv2.imshow("Toate obiectele detectate",img)
	#IP.Image_preview(img)
	cv2.waitKey(0)
	cv2.destroyAllWindows()
	return class_ids, confidences, boxes

