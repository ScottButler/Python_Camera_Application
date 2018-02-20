""" This is a simple camera program that will access the webcam on your computer with OpenCV.

To take a picture hit SPACEBAR and to exit hit ESC.
You must hit ESC to exit and not click the x on the window to exit. 
For this to work properly the camera window should be highlighted if going between windows while in use. 

This program is based on a systems running Windows opperating system and has Windows based file paths. 
For the pictures to save the directory that pictures are saved in must exist. 
NOTE: Windows paths use \\ and not / like on Unix and Linux

Pictures are saved under a value of the amout of secondes since January 1, 1970 and are increminted,
this allows pictures to be saved under unique names and for files to not overwrite eachother. 


For this program to work on your machine the address path on the line containing
img_name = "C:\\Users\\YOUR_USER_NAME_HERE\\Pictures\\camera\\{}.jpg".format(t2), must be changed to the desired location
"""


import cv2
import time

# os.chdir('C:\\Users\\YOUR_USER_NAME_HERE\\Pictures\\camera') #save location
cap = cv2.VideoCapture(0)    # (0) for camera built into laptop, (1) for external webcam
t = time.time() #time in seconds to name picture
t2 = int(t)/1 # remove decimal point

print "PRESS SPACEBAR TO TAKE PHOTO"
print "PRESS ESC TO EXIT"

while(cap.isOpened()):
	ret, img = cap.read()
	cv2.imshow("output", img)
	# waitkey is delay in ms?
	k = cv2.waitKey(10)
	# k = 27 is the esc key
	# press esc to break while loop
	if k == 27:
		break
	# k = 32 is SPACEBAR
	# hit spacebar to save image
	elif k == 32:
		#img_name = "C:\\Users\\root\\Pictures\\camera\\Testpicture{}.jpg".format(img_count)
		#YOUR_USER_NAME_HERE must be changed you your windows user name, or create a different custom path
		# Ff the path below is used after YOUR_USER_NAME_HERE, a directory named camera must be added to the pictures directory
		img_name = "C:\\Users\\YOUR_USER_NAME_HERE\\Pictures\\camera\\{}.jpg".format(t2)    # Location of saved pictures
		cv2.imwrite(img_name, img)
		#img_count += 1
		t2 +=1
cap.release()
cv2.destroyAllWindows()
