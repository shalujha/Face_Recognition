# simple program to read and show image in opencv
import cv2
img=cv2.imread(r'C:\Users\ayush\Desktop\logo.png')
new_img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
gray=cv2.imread(r'C:\Users\ayush\Desktop\logo.png',cv2.IMREAD_GRAYSCALE)
cv2.imshow("Flower",img)
cv2.imshow("Gray",gray)
cv2.waitKey(0)
cv2.destroyAllWindows()