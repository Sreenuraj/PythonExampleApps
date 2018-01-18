import cv2, pandas
from datetime import datetime

"""
For details of the method used:
https://docs.opencv.org/2.4/index.html
"""

# create a video capture object, 0 means the default camera
video = cv2.VideoCapture(0)
first_frame = None
status_list = [None,None]
times = []
df = pandas.DataFrame(columns=["Start","End"])

# In a while loop, loop through frame which is return by video.read() method
while True:
    # video.read() return the boolean [check] and numpyarray[frame]
    check, frame = video.read()
    status = 0
    # reversing the color image getting captured
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    #Blurs an image using a Gaussian filter
    gray = cv2.GaussianBlur(gray,(21,21),0)
    # store the first frame to the variable
    if first_frame is None:
        first_frame=gray
        continue
    # delta frame to get the diif between the first_frame and current
    delta_frame = cv2.absdiff(first_frame,gray)
    #threshold_delta for making the image white[255] if the threshold is greater that 30
    threshold_delta_frame = cv2.threshold(delta_frame, 30, 255, cv2.THRESH_BINARY)[1]
    threshold_delta_frame = cv2.dilate(threshold_delta_frame, None, iterations=2)

    #find the contours
    (_,cnts,_) = cv2.findContours(threshold_delta_frame.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Checking if pixel is greater than a threshold value
    for contour in cnts:
        if cv2.contourArea(contour) < 1000:
            continue
        status = 1
        (x,y,width,height) = cv2.boundingRect(contour)
        cv2.rectangle(frame, (x, y), (x+width,y+height), (0,255,0), 3)
    status_list.append(status)

    # Adding the time when there is a motion detected
    if status_list[-1]==1 and status_list[-2]==0:
        times.append(datetime.now())
    if status_list[-1]==0 and status_list[-2]==1:
        times.append(datetime.now())
        
    # Showing the image
    cv2.imshow('Gray', gray)
    cv2.imshow('Delta', delta_frame)
    cv2.imshow('Threshold', threshold_delta_frame)
    cv2.imshow('Color', frame)

    # Wait key to capture 'q'
    key = cv2.waitKey(1)
    # Check if the user input is 'q' to break and come out of loop
    if key == ord('q'):
        times.append(datetime.now())
        break
#print(df)
#print(status_list)
print(times)

for i in range(0,len(times),2):
    if i+1 >= len(times):
        df = df.append({"Start":times[i],"End":times[i]}, ignore_index=True)
    else:
        df = df.append({"Start":times[i],"End":times[i+1]}, ignore_index=True)

df.to_csv('Times.csv')
# Releasing the video
video.release()
cv2.destroyAllWindows
