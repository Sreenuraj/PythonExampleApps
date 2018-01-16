import cv2

# create a video capture object
video = cv2.VideoCapture(0)

# In a while loop, loop through frame which is return by video.read() method
while True:
    # video.read() return the boolean [check] and numpyarray[frame]
    check, frame = video.read()
    print(check)
    print(frame)
    # reversing the color image getting captured
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    # Showing the image
    cv2.imshow('Capturing', gray)
    # Wait key to capture 'q'
    key = cv2.waitKey(1)
    # Check if the user input is 'q' to break and come out of loop
    if key == ord('q'):
        break
# Releasing the video
video.release()
cv2.destroyAllWindows
