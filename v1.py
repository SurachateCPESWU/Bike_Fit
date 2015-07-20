import numpy as np
import cv2
import math

def cal():
     C = math.sqrt(math.pow(temp_x[2]-temp_x[1],2) + math.pow(temp_y[2]-temp_y[1],2))
     B = math.sqrt(math.pow(temp_x[2]-temp_x[0],2) + math.pow(temp_y[2]-temp_y[0],2))
     A = math.sqrt(math.pow(temp_x[0]-temp_x[1],2) + math.pow(temp_y[0]-temp_y[1],2))
     print "C = %d "%C
     print "B = %d "%B
     print "A = %d "%A
     
     ANS = math.acos(((math.pow(A,2))+(math.pow(C,2))-(math.pow(B,2)))/(2*A*C))
     print math.degrees(ANS)

     
img = cv2.imread('process.jpg',1)
process = cv2.inRange(img,(30,50,180),(50,90,210),img)
contours,hierarchy = cv2.findContours(process,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
temp_x=[]
temp_y=[]
for cnt in contours :
     M = cv2.contourArea(cnt)
     if( M > 100 ):
          M = cv2.moments(cnt)
          cx = int(M['m10']/M['m00'])
          cy = int(M['m01']/M['m00'])
          cv2.circle(img,(cx,cy),20,(0,255,0),2)
          temp_x.append(cx)
          temp_y.append(cy)

i = len(temp_x)
cv2.line(img,(temp_x[0],temp_y[0]),(temp_x[i-1],temp_y[i-1]),(0,255,0),3)
while (i > 1):
     cv2.line(img,(temp_x[i-1],temp_y[i-1]),(temp_x[i-2],temp_y[i-2]),(0,255,0),3)
     i = i - 1

cal()

cv2.imshow("img",img)
cv2.imshow("pro",process)
cv2.waitKey(0)
