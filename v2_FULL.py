import numpy as np
import cv2
import math

def cal():
     if(temp_x[1]>temp_x[2]):
      try:
          # องศาเข่า
          C = math.sqrt(math.pow(temp_x[3]-temp_x[1],2) + math.pow(temp_y[3]-temp_y[1],2))
          B = math.sqrt(math.pow(temp_x[3]-temp_x[0],2) + math.pow(temp_y[3]-temp_y[0],2))
          A = math.sqrt(math.pow(temp_x[0]-temp_x[1],2) + math.pow(temp_y[0]-temp_y[1],2))
          ANS = math.acos(((math.pow(A,2))+(math.pow(C,2))-(math.pow(B,2)))/(2*A*C))
          Degree = int (math.degrees(ANS))
          cv2.putText(img,str(Degree),(temp_x[1]+30,temp_y[1]),cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255),3)
          # องศาหลัง
          C_2 = math.sqrt(math.pow(temp_x[3]-temp_x[5],2) + math.pow(temp_y[3]-temp_y[3],2))
          B_2 = math.sqrt(math.pow(temp_x[5]-temp_x[5],2) + math.pow(temp_y[5]-temp_y[3],2))
          A_2 = math.sqrt(math.pow(temp_x[5]-temp_x[3],2) + math.pow(temp_y[5]-temp_y[3],2))
          ANS_2 = math.acos(((math.pow(A_2,2))+(math.pow(C_2,2))-(math.pow(B_2,2)))/(2*A_2*C_2))
          Degree_2 = int(math.degrees(ANS_2))
          cv2.putText(img,str(Degree_2),(temp_x[3]-70,temp_y[3]),cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255),3)
          # องศาไหล่
          C_3 = math.sqrt(math.pow(temp_x[3]-temp_x[5],2) + math.pow(temp_y[3]-temp_y[5],2))
          B_3 = math.sqrt(math.pow(temp_x[4]-temp_x[3],2) + math.pow(temp_y[4]-temp_y[3],2))
          A_3 = math.sqrt(math.pow(temp_x[4]-temp_x[5],2) + math.pow(temp_y[4]-temp_y[5],2))
          ANS_3 = math.acos(((math.pow(A_3,2))+(math.pow(C_3,2))-(math.pow(B_3,2)))/(2*A_3*C_3))
          Degree_3 = int(math.degrees(ANS_3))
          cv2.putText(img,str(Degree_3),(temp_x[5]+20,temp_y[5]),cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255),3)
          # แขน
          C_4 = math.sqrt(math.pow(temp_x[2]-temp_x[4],2) + math.pow(temp_y[2]-temp_y[4],2))
          B_4 = math.sqrt(math.pow(temp_x[2]-temp_x[5],2) + math.pow(temp_y[2]-temp_y[5],2))
          A_4 = math.sqrt(math.pow(temp_x[4]-temp_x[5],2) + math.pow(temp_y[4]-temp_y[5],2))
          ANS_4 = math.acos(((math.pow(A_4,2))+(math.pow(C_4,2))-(math.pow(B_4,2)))/(2*A_4*C_4))
          Degree_4 = int(math.degrees(ANS_4))
          cv2.putText(img,str(Degree_4),(temp_x[4]-70,temp_y[4]),cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255),3)
      except: pass
     elif(temp_x[1]<temp_x[2]):
      try:
          # องศาเข่า
          C = math.sqrt(math.pow(temp_x[3]-temp_x[2],2) + math.pow(temp_y[3]-temp_y[2],2))
          B = math.sqrt(math.pow(temp_x[3]-temp_x[0],2) + math.pow(temp_y[3]-temp_y[0],2))
          A = math.sqrt(math.pow(temp_x[0]-temp_x[2],2) + math.pow(temp_y[0]-temp_y[2],2))
          ANS = math.acos(((math.pow(A,2))+(math.pow(C,2))-(math.pow(B,2)))/(2*A*C))
          Degree = int (math.degrees(ANS))
          cv2.putText(img,str(Degree),(temp_x[2]+30,temp_y[2]),cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255),3)
          # องศาหลัง
          C_2 = math.sqrt(math.pow(temp_x[3]-temp_x[5],2) + math.pow(temp_y[3]-temp_y[3],2))
          B_2 = math.sqrt(math.pow(temp_x[5]-temp_x[5],2) + math.pow(temp_y[5]-temp_y[3],2))
          A_2 = math.sqrt(math.pow(temp_x[5]-temp_x[3],2) + math.pow(temp_y[5]-temp_y[3],2))
          ANS_2 = math.acos(((math.pow(A_2,2))+(math.pow(C_2,2))-(math.pow(B_2,2)))/(2*A_2*C_2))
          Degree_2 = int(math.degrees(ANS_2))
          cv2.putText(img,str(Degree_2),(temp_x[3]-70,temp_y[3]),cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255),3)
          # องศาไหล่
          C_3 = math.sqrt(math.pow(temp_x[3]-temp_x[5],2) + math.pow(temp_y[3]-temp_y[5],2))
          B_3 = math.sqrt(math.pow(temp_x[4]-temp_x[3],2) + math.pow(temp_y[4]-temp_y[3],2))
          A_3 = math.sqrt(math.pow(temp_x[4]-temp_x[5],2) + math.pow(temp_y[4]-temp_y[5],2))
          ANS_3 = math.acos(((math.pow(A_3,2))+(math.pow(C_3,2))-(math.pow(B_3,2)))/(2*A_3*C_3))
          Degree_3 = int(math.degrees(ANS_3))
          cv2.putText(img,str(Degree_3),(temp_x[5]+20,temp_y[5]),cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255),3)
          # แขน
          C_4 = math.sqrt(math.pow(temp_x[1]-temp_x[4],2) + math.pow(temp_y[1]-temp_y[4],2))
          B_4 = math.sqrt(math.pow(temp_x[1]-temp_x[5],2) + math.pow(temp_y[1]-temp_y[5],2))
          A_4 = math.sqrt(math.pow(temp_x[4]-temp_x[5],2) + math.pow(temp_y[4]-temp_y[5],2))
          ANS_4 = math.acos(((math.pow(A_4,2))+(math.pow(C_4,2))-(math.pow(B_4,2)))/(2*A_4*C_4))
          Degree_4 = int(math.degrees(ANS_4))
          cv2.putText(img,str(Degree_4),(temp_x[4]-70,temp_y[4]),cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255),3)
      except:pass
     
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

#cap = cv2.VideoCapture('process_6dot.avi')
cap = cv2.VideoCapture(0)
while(cap.isOpened()):
     ret, img = cap.read()
     #temp_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HLS_FULL)
     if(img != None):
          process = cv2.blur(img,(3,3))
          process = cv2.inRange(process,(90,40,10),(160,90,100),img)
          contours,hierarchy = cv2.findContours(process,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
          temp_x=[]
          temp_y=[]
          for cnt in contours :
               count_M = 0
               M = cv2.contourArea(cnt)
               if( M > 30 ):
                    count_M = count_M + 1
                    M = cv2.moments(cnt)
                    cx = int(M['m10']/M['m00'])
                    cy = int(M['m01']/M['m00'])
                    cv2.circle(img,(cx,cy),10,(0,255,0),1)
                    temp_x.append(cx)
                    temp_y.append(cy)
          i = len(temp_x)
          if(i == 6):
               if(temp_x[1]>temp_x[2]):
                    cv2.line(img,(temp_x[0],temp_y[0]),(temp_x[1],temp_y[1]),(0,255,0),3)
                    cv2.line(img,(temp_x[1],temp_y[1]),(temp_x[3],temp_y[3]),(0,255,0),3)
                    cv2.line(img,(temp_x[3]-100,temp_y[3]),(temp_x[3],temp_y[3]),(255,0,0),3)
                    cv2.line(img,(temp_x[3],temp_y[3]),(temp_x[5],temp_y[5]),(0,255,0),3)
                    cv2.line(img,(temp_x[5],temp_y[5]),(temp_x[4],temp_y[4]),(0,255,0),3)
                    cv2.line(img,(temp_x[4],temp_y[4]),(temp_x[2],temp_y[2]),(0,255,0),3)
                    cv2.line(img,(temp_x[1],temp_y[1]),(temp_x[1],temp_y[0]+40),(255,0,0),2)
                    cal()
               else:
                    cv2.line(img,(temp_x[0],temp_y[0]),(temp_x[2],temp_y[2]),(0,255,0),3)
                    cv2.line(img,(temp_x[2],temp_y[2]),(temp_x[3],temp_y[3]),(0,255,0),3)
                    cv2.line(img,(temp_x[3],temp_y[3]),(temp_x[5],temp_y[5]),(0,255,0),3)
                    cv2.line(img,(temp_x[5],temp_y[5]),(temp_x[4],temp_y[4]),(0,255,0),3)
                    cv2.line(img,(temp_x[4],temp_y[4]),(temp_x[1],temp_y[1]),(0,255,0),3)
                    cv2.line(img,(temp_x[1],temp_y[1]),(temp_x[1],temp_y[0]+40),(255,0,0),2)
                    cal()
          #check_max(temp_y[0])
          #cv2.imshow("hsv",temp_hsv)
          cv2.imshow("img",img)
          cv2.imshow("pro",process)
     if cv2.waitKey(33) & 0xFF == ord('q'):
          cv2.destroyAllWindows()
          cap.release()
          break
     
average = SHOW_Y_MAX_Degree()
#print "##########################"
#print "Average @ เวลายืดสุดขา = %d"%average
#print "##########################"
print "END"
