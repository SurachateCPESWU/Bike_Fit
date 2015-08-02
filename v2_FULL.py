import numpy as np
import cv2
import math


      
colors = []
Y_max = 0
Degree = 0
Y_MAX_Degree = []


def nothing(x):
    pass


def on_mouse_click (event, x, y,flags,param):
     global range_colors
     global colors
     if event == cv2.EVENT_LBUTTONUP:
          colors = img[y,x].tolist()
     

               
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
     

def check_max(y):
     global Y_max
     global Y_MAX_Degree
     if(y >= Y_max):
          Y_max = y
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

cap = cv2.VideoCapture(0)
st = np.zeros((100,500,3), np.uint8)
cv2.namedWindow('setting')
cv2.createTrackbar('Range','setting',30,150,nothing)
cv2.createTrackbar('Area','setting',30,1000,nothing)
cv2.createTrackbar('switch', 'setting',0,1,nothing)
cv2.putText(st,"          by SurachateCPESWU",(7,90),cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255),1)
cv2.putText(st,"Press q to exit.",(7,40),cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255),2)


while(cap.isOpened()):
     ret, img = cap.read()
     if(ret==True):
          range_colors = cv2.getTrackbarPos('Range','setting')
          range_area = cv2.getTrackbarPos('Area','setting')
          switch = cv2.getTrackbarPos('switch','setting')
          process = img.copy()
          if(colors!=[]):
               process = cv2.inRange(process,(colors[0]-range_colors,colors[1]-range_colors,colors[2]-range_colors),(colors[0]+range_colors,colors[1]+range_colors,colors[2]+range_colors),img)
               contours,hierarchy = cv2.findContours(process,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
               temp_x=[]
               temp_y=[]
               for cnt in contours :
                    count_M = 0
                    M = cv2.contourArea(cnt)
                    if( M > range_area ):
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
                         if(switch==1):
                              cv2.line(img,(temp_x[1],temp_y[1]),(temp_x[1],temp_y[0]+40),(255,0,0),2)
                         cal()
                    else:
                         cv2.line(img,(temp_x[0],temp_y[0]),(temp_x[2],temp_y[2]),(0,255,0),3)
                         cv2.line(img,(temp_x[2],temp_y[2]),(temp_x[3],temp_y[3]),(0,255,0),3)
                         cv2.line(img,(temp_x[3],temp_y[3]),(temp_x[5],temp_y[5]),(0,255,0),3)
                         cv2.line(img,(temp_x[5],temp_y[5]),(temp_x[4],temp_y[4]),(0,255,0),3)
                         cv2.line(img,(temp_x[4],temp_y[4]),(temp_x[1],temp_y[1]),(0,255,0),3)
                         if(switch==1):
                              cv2.line(img,(temp_x[1],temp_y[1]),(temp_x[1],temp_y[0]+40),(255,0,0),2)
                         cal()
          cv2.imshow("img",img)
          cv2.imshow("setting",st)
          cv2.setMouseCallback('img',on_mouse_click)
          
          
     if cv2.waitKey(33) & 0xFF == ord('q'):
          cv2.destroyAllWindows()
          cap.release()
          break
     
print "END"
