import cv2

face_re= cv2.CascadeClassifier("D:\images\hqdefault.jpg")
img=  cv2.imread("D:\images\hqdefault.jpg",1) # 0 for black and white image 1 for color image
grey=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
face=face_re.detectMultiscale(grey, scaleFactor=1.05, minNeighbours=5)
# print(img)  print which type of matrices used by image 2d for black and white and 3d for color image
# print(type(img))  show dimensional array
print(img.shape)  #if 0 is in imread method then only 2d matrices print and no channel if 1 is in then 3d matrices print and 3 is also print with if we use shape method
#cv2.imshow("hqdefaul",img) # to show the image
#resized=cv2.resize(img,(int(img.shape[1]/2),int(img.shape[0]/2)))
#cv2.imshow("Rishabh",resized)
#print(resized.shape)
print(type(face))
print(face)
cv2.waitKey(0) # to hold the image for a time we specify the value in place of 0 but here 0 means when user click it image automatically disappear we can also put time here in milisecond then after that time the window automatically destroy
cv2.destroyAllWindows() # when we click any key the window automtically destroy
