import cv2
import glob2

path = "/Sreenu/PythonExampleApps/Example_opencv/sample-images/"
images=glob2.glob(path+"**/*.jpg")

#print(images)
for each_image in images:
    img=cv2.imread(each_image,0)
    resized_image=cv2.resize(img,(100,100))
    cv2.imwrite(each_image+"_resized.jpg",resized_image)
