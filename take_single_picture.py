import cv2
import time
# takes single photo with no display screen

cap = cv2.VideoCapture(0)
t = time.time() #time in seconds to name picture
t2 = int(t)/1 # remove decimal point

while(cap.isOpened()):
	ret, img = cap.read()	#will not work without ret for some reason
	#change save location to existing directory to store capture
	img_name = "C:\\Users\\Your_Name_Here\\Pictures\\camera\\{}.jpg".format(t2) # save location
	cv2.imwrite(img_name, img)
	break
cap.release()