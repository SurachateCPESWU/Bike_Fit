import numpy as np
import cv2
import math

def cal():
     C = math.sqrt(math.pow(temp_x[2]-temp_x[1],2) + math.pow(temp_y[2]-temp_y[1],2))
     B = math.sqrt(math.pow(temp_x[2]-temp_x[0],2) + math.pow(temp_y[2]-temp_y[0],2))
     A = math.sqrt(math.pow(temp_x[0]-temp_x[1],2) + math.pow(temp_y[0]-temp_y[1],2))
     #print "C = %d "%C
     #print "B = %d "%B
     #print "A = %d "%A
     
     ANS = math.acos(((math.pow(A,2))+(math.pow(C,2))-(math.pow(B,2)))/(2*A*C))
     global Degree
     Degree = math.degrees(ANS)
     print Degree
     
Y_max = 0
Degree = 0
Y_MAX_Degree = []

def check_max(y):
     global Y_max
     global Y_MAX_Degree
     if(y >= Y_max):
          Y_max = y
          #print "Y_MAX = %d"%Y_max
          Y_MAX_Degree.append(Degree)
          
def SHOW_Y_MAX_Degree():
     temp = 0
     global Y_MAX_Degree
     i = len(Y_MAX_Degree)
     if ( i > 10):
          for j in range(i/2,i):
               temp = (temp + Y_MAX_Degree[j])
          temp = temp / (i/2)
     return temp

cap = cv2.VideoCapture('vdo_process.avi')

while(cap.isOpened()):
     ret, img = cap.read()
     if(img != None):
          process = cv2.inRange(img,(90,50,10),(160,90,50),img)
          contours,hierarchy = cv2.findContours(process,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
          temp_x=[]
          temp_y=[]
          for cnt in contours :
               count_M = 0
               M = cv2.contourArea(cnt)
               if( M > 100 ):
                    count_M = count_M + 1
                    M = cv2.moments(cnt)
                    cx = int(M['m10']/M['m00'])
                    cy = int(M['m01']/M['m00'])
                    cv2.circle(img,(cx,cy),10,(0,255,0),2)
                    temp_x.append(cx)
                    temp_y.append(cy)
          i = len(temp_x)
          #cv2.line(img,(temp_x[0],temp_y[0]),(temp_x[i-1],temp_y[i-1]),(0,255,0),3)
          while (i > 1):
               cv2.line(img,(temp_x[i-1],temp_y[i-1]),(temp_x[i-2],temp_y[i-2]),(0,255,0),3)
               i = i - 1
          cal()
          check_max(temp_y[0])
          cv2.imshow("img",img)
          cv2.imshow("pro",process)
     if cv2.waitKey(1) & 0xFF == ord('q'):
          cv2.destroyAllWindows()
          cap.release()
          break
     
average = SHOW_Y_MAX_Degree()
print "##########################"
print "Average @ เวลายืดสุดขา = %d"%average
print "##########################"
print "END"
