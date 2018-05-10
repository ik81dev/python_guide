import numpy as np
import cv2

cap = cv2.VideoCapture(0)

# Define the codec and create VideoWriter object
#fourcc = cv2.VideoWriter_fourcc(*'XVID')
fourcc = cv2.VideoWriter_fourcc('M','J','P','G')
#'M','R','L','E'
#fourcc = cv2.VideoWriter_fourcc('M','R','L','E')
out = cv2.VideoWriter('output_2.avi',fourcc, 20.0, (640,480))

while(cap.isOpened()):
    ret, frame = cap.read()
    print(ret)
    if ret==True:
        #frame = cv2.flip(frame,0)
        #write the flipped frame
		#print("Writing frame...")
        #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        print("Writing image ...")
        out.write(frame)
        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# Release everything if job is finished
cap.release()
out.release()
cv2.destroyAllWindows()