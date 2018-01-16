import cv2

# load haarcascade into the variable
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#image to find faces
img = cv2.imread('news.jpg')
# image invert so that the accuracy may improve
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#Using face_cascade.detectMultiScale scanning the image for facess
faces = face_cascade.detectMultiScale(gray_img, scaleFactor= 1.1, minNeighbors=5)
print(type(faces))
print(faces)

# Drawing a rectagle in the image using the return faces values
for x,y,w,h in faces:
    img = cv2.rectangle(img, (x,y),(x+w,y+h),(0,255,0),3)

resized_img = cv2.resize(img,(int(img.shape[1]/2),int(img.shape[0]/2)))

cv2.imshow('FaceMarked', resized_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
