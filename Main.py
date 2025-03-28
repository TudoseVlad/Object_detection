import Yolo as Y
import Object_removal as OR
import GUI as G
def main():
	print("pre GUI")
	object_found, precision, pic =  G.GUI();
	print ("post GUI")
	print(object_found, precision, pic)
	confidences = []
	class_ids = []
	boxes = []
	class_ids, confidences, boxes = Y.Yolo(precision ,pic);
	names_in_ro = []
	with open("coco.nume","r") as f:
		names_in_ro = [line.strip() for line in f.readlines()]
	classes = []
	with open("coco.names","r") as f:
		classes = [line.strip() for line in f.readlines()]
	no_objects_detected = len(boxes)
	dictionar = {names_in_ro[i] : classes[i] for i in range(len(names_in_ro))}
	object_found = dictionar.get(object_found)
	print (object_found)
	position = -1
	maximum = 0
	x_center = -1
	y_center = -1
	w_object = -1
	h_object = -1
	for i in range(len(boxes)):
		x, y, w, h = boxes[i]
		val = w*h
		label = classes[class_ids[i]]
		if label == object_found:
			if maximum < val:
				position = i
				maximum  = val
				x_center = int(x + w / 2)
				y_center = int(y + h / 2)
				w_object = w 
				h_object = h
	OR.Object_removal( position, x_center,  y_center,  w_object, h_object, pic);
main()