import cv2

# Read a image file
img = cv2.imread('galaxy.jpg',0)

#resizing the image excepts the file name and tuple containing the shape
resized_image = cv2.resize(img,(int(img.shape[1]/2),int(img.shape[0]/2)))
# create an image
cv2.imwrite('galaxy_resized.jpg',resized_image)
#Dispaly the image
cv2.imshow('Galaxy',resized_image)
#where to kill the image shown, 0 means when user clicks any key
cv2.waitKey(0)
#what to kill, in this case the window
cv2.destroyAllWindows()
