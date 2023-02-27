# import cv2
# import numpy as np

# # Load the image
# img = cv2.imread("")

# # Convert the image to HSV color space
# hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# # Define the lower and upper bounds for orange cones and green path
# orange_lower = np.array([0, 70, 50])
# orange_upper = np.array([30, 255, 255])
# green_lower = np.array([30, 70, 50])
# green_upper = np.array([80, 255, 255])

# # Create masks for orange cones and green path
# orange_mask = cv2.inRange(hsv, orange_lower, orange_upper)
# green_mask = cv2.inRange(hsv, green_lower, green_upper)

# # Apply Canny edge detection to the orange mask
# orange_edges = cv2.Canny(orange_mask, 100, 200)

# # Find contours in the orange edges image
# orange_contours, _ = cv2.findContours(orange_edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# # Find the largest contour, which should correspond to the boundary of the path
# path_contour = max(orange_contours, key=cv2.contourArea)

# # Draw the path contour on the original image in green
# cv2.drawContours(img, [path_contour], -1, (0, 255, 0), 2)

# # Save the image as "answer.png"
# cv2.imwrite("answer.png", img)


###############################################################
#Doesn't work

# import cv2 as cv
# import numpy as np

# img= cv.imread("D:/original.png")
# #cv.imshow('original', img)

# #This rescales images

# def rescaleFrame(frame, scale=0.4):
#     width = int(frame.shape[1] * scale) #width
#     height = int(frame.shape[0] * scale) #height
#     dimensions=(width,height)

#     return cv.resize(frame,dimensions, interpolation=cv.INTER_AREA)

# # Reading images
# resized_image=rescaleFrame(img)
# #cv.imshow('ID-resized', resized_image)

# # Converting the imgage to HSV color space 
# hsv_img=cv.cvtColor(resized_image,cv.COLOR_BGR2HSV)
# #cv.imshow("HSV",hsv_img) 

# # Creating a range of values for opencv to detect red cones
# # Colors between [0,0,200] and [0,0,255] are considered red 
# lower_red = np.array([0, 0, 190], dtype = "uint8") 
# upper_red= np.array([0, 0, 256], dtype = "uint8")

# # Returns a binary image where white is for red color detected
# # and black is for not detected
# mask = cv.inRange(resized_image, lower_red, upper_red)
# cv.imshow("mask",mask)
# detected_output = cv.bitwise_and(resized_image, resized_image, mask =  mask) 

# cv.imshow("red color detection", detected_output) 

# # Canny edge detection
# # canny=cv.Canny(detected_output, 150,255)
# # cv.imshow("Canny",canny)

#######################################################################


import cv2
import numpy as np

# Reading the image

img = cv2.imread('D:/original.png')

#Rescaled
def rescaleFrame(frame, scale=0.4):
    width = int(frame.shape[1] * scale) #width
    height = int(frame.shape[0] * scale) #height
    dimensions=(width,height)

    return cv2.resize(frame,dimensions, interpolation=cv2.INTER_AREA)

img=rescaleFrame(img)


# convert to hsv colorspace 
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# lower bound and upper bound for Red color 
lower_bound = np.array([161,155,84])
upper_bound = np.array([179,255,255])


# find the colors within the boundaries using a mask
mask = cv2.inRange(hsv, lower_bound, upper_bound)
# cv2.imshow("mask",mask)

# Applying canny edge detection for detecting the edges
canny = cv2.Canny(mask, 100, 200)
# cv2.imshow("canny",canny)

# Finding contours in the image
contours, heirarchies = cv2.findContours(canny, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

list_contours=[]
for i in contours:
    list_contours.append([i[0][0][0],i[0][0][0]])

list_contours=sorted(list_contours)

top_right=max(list_contours)

bottom_left=min(list_contours)


# topmost left, topmost right, bottommost left bottommost right
corners=[[-1,-1],[-1,-1],[-1,-1],[-1,-1]]
for i in range(len(list_contours)):
    if corners==[[-1,-1],[-1,-1],[-1,-1],[-1,-1]]:
        corners=[list_contours[i],list_contours[i],list_contours[i],list_contours[i]]
    


    #Topmost right :top has highest value, right has highest value 
    elif list_contours[i][0]>corners[1][0] and list_contours[i][0]>corners[1][0]:
        corners[1]=list_contours[i]
    #Bottom right :bottom has least value, right has highest value 
    elif list_contours[i][0]<corners[3][0] and list_contours[i][0]>corners[3][0]:
         corners[3]=list_contours[i]



# Draw lines
# Bottom left to top left
cv2.line(img, bottom_left, corners[1], (0,0,255), thickness=2)
# Bottom right to top right 
cv2.line(img, corners[3],top_right, (0,0,255), thickness=2) 

# # assign the four corners based on the sorted coordinates

# top_left = list_contours[0]
# top_right = (list_contours[3][0], list_contours[len(list_contours)-1][1])
# bottom_right = list_contours[len(list_contours)-1]
# bottom_left = (list_contours[0][0], list_contours[3][1])
# cv2.line(img,top_left,bottom_left,(0,0,255), thickness=2)
# cv2.line(img,top_right,bottom_right,(0,0,255), thickness=2)

cv2.imshow("Image",img)
cv2.imwrite('answer.png',img)


#contours = max(contours, key=cv2.contourArea)

# Drawing contours on the image
# cv2.drawContours(img, contours, -1, (0,0,255), 1)
# cv2.imshow("Blank",img) 

cv2.waitKey(0) # Waits for an infinite amount of time