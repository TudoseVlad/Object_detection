
import cv2
def Object_removal(position, x, y ,w ,h, pic):
	img = cv2.imread(pic)
	#img = cv2.resize(img , None , fx = 0.4 , fy = 0.4)
	if position < 0:
		print("N-am gasit obicetul dorit!")
	else:
		
		print("Mutam bratul robotic centrat in cercul pus pe imagine")
		x_up =int(x-w/2)
		y_up = int(y-h/2)
		x_dn = int(x+w/2)
		y_dn = int(y+h/2)
		cv2.circle(img, (x,y),10, (0,255,0), 2)
		cv2.circle(img, (x_up, y), 10, (0,0,255), 2)
		cv2.circle(img, (x_dn, y), 10, (0,0,255), 2)
		cv2.rectangle(img , (x_up, y_up), (x_dn, y_dn), (255, 0, 0), 2)
		#cv2.circle(img, (x,y),  1, (0, 255, 0), 2)
		cv2.namedWindow("Obiectul care o sa fie extras", cv2.WINDOW_NORMAL)
		cv2.resizeWindow("Obiectul care o sa fie extras", 1366, 768)
		cv2.imshow("Obiectul care o sa fie extras",img)
		cv2.waitKey(0)
		cv2.destroyAllWindows()