import cv2
import numpy as np

# Reading the image
img = cv2.imread('original.png')

#Rescaling the image
def rescaleFrame(frame, scale=0.4):
    width = int(frame.shape[1] * scale) #width
    height = int(frame.shape[0] * scale) #height
    dimensions=(width,height)

    return cv2.resize(frame, dimensions, interpolation=cv2.INTER_AREA)

img=rescaleFrame(img)


# converts to hsv colorspace for detecting colors 
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Defining lower bound and upper bound for Red color 
lower_bound = np.array([161,155,84])
upper_bound = np.array([179,255,255])


# finds red color within the range
# returns a binary image which is white 
# where the colors are detected and 0 otherwise
mask = cv2.inRange(hsv, lower_bound, upper_bound)


# Applying canny edge detection for detecting the edges
canny = cv2.Canny(mask, 100, 200)

# Finding contours in the image
contours, heirarchies = cv2.findContours(canny, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

# Storing the contours in a list
list_contours=[]
for i in contours:
    list_contours.append([i[0][0][0],i[0][0][1]])

# sorting the list based on the x-value of the contours
list_contours=sorted(list_contours)


# dividing the array into left-sided and right-sided contours 
# based on the median 
left_contours=list_contours[:len(list_contours)//2]
right_contours=list_contours[len(list_contours)//2:]


# converts the lists into to np arrays
left_pts = np.array(left_contours)
right_pts= np.array(right_contours)

# left_pts[:,0] returns the x coordinates of left_pts
# right_pts[:,1] returns the y coordinates of right_pts
# fits a polynomial curve of degree 1 (a line) to a set of data points 
# using least squares polynomial approximation.
left_coeffs = np.polyfit(left_pts[:,0], left_pts[:,1], 1)
right_coeffs = np.polyfit(right_pts[:,0], right_pts[:,1], 1)


# linspace generates x coordinates that are equally spaced 
# between minimum x and maximum x coordinates of the contours
left_x_coords=np.linspace(min(left_pts[:,0]),max(left_pts[:,0]),100)
right_x_coords=np.linspace(min(right_pts[:,0]),max(right_pts[:,0]),100)

# polyval gets the corresponding y coordinates from the input x coordinates
# based of the curve obtained by coeffs 
left_y_coords=np.polyval(left_coeffs,left_x_coords)
right_y_coords=np.polyval(right_coeffs,right_x_coords)

# column_stack stacks the 1-D lists of x points and y points horizontally
# as points in a 2-D array to be drawn
left_line_pts = np.column_stack((left_x_coords.astype(int), left_y_coords.astype(int)))
right_line_pts = np.column_stack((right_x_coords.astype(int), right_y_coords.astype(int)))

# draws a line from a set of integer x and y coordinates
cv2.polylines(img, [left_line_pts], False, (0, 0, 255), thickness=4)
cv2.polylines(img, [right_line_pts], False, (0,0,255), thickness=4)

cv2.imshow("Answer",img)
cv2.imwrite('answer.png',img)
cv2.waitKey(0) # Waits for an infinite amount of time