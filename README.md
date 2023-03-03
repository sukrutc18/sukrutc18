- 👋 Hi, I’m @sukrutc18
- 👀 I’m interested in Computer Science
- 🌱 I’m currently ...
- 💞️ I’m looking to collaborate on ...
- 📫 How to reach me ...

<!---
sukrutc18/sukrutc18 is a ✨ special ✨ repository because its `README.md` (this file) appears on your GitHub profile.
You can click the Preview link to take a look at your changes.
--->

Wisconsin Autonomous Perception Coding Challenge:

This the image of my answer: 
![answer](https://user-images.githubusercontent.com/116688211/222628063-ccda1ccb-4c68-442b-9f44-d7da7ee362f1.png)

Methodology:
1. I first read and rescaled my image to show it fully on my screen. Then I converted it into hsv colorspace for detecting the colors in the image.
2. Then, I defined two arrays for the upper and lower bounds for red color and used the inRange() function to color the parts having red white and the rest black.(binary image)
3. Next, I used canny edge detection to detect the edges in the binary image and found the contours using the canny image
4. Then, I stored the contours in a list, sorted the list, and divided the contours into two lists - left_contours for the contours to the left of the median contour, and right_contours for the cotours to the right of the median including the median. I converted the two lists to numpy arrays
5. Then, using np.polyfit(), I found two line equations for the contours.
6. Using np.linspace(), I generated equally spaced out x coordinates for the lines and found the y coordinates for all the x coordinates using np.polyval()
7. Finally, I made 2-D arrays of (x,y) coordinates using np.columnstack() and then drew the lines on the image using polylines()
8. I think the reason why I am not getting a clear line is because I'm getting the x and y-coordinates of the line (that might be floats) and then converting them to integers to pass as arguments in the columnstack (as polylines takes only a 2-D array of integers). The x and y coordiates are slightly off the line so it couldn't draw a fully straight line. I could use the equation obtained from polyfit() directly on the contours to get the contours on the line as pass those as an array to polylines (although there might be no contour fitting the line).

What did you try and why do you think it did not work:
I first tried getting the coordinates for the lines by finding the topmost left, topmost right, bottommost left and bottommost right. However, I only got one line going across the image (I didn't understand why). Later, I realized that I may get a completely different line as the findContours() method gets the red contours over the whole image.
Then, I tried using fitLine() method but there were some issues while passing the input list and I didn't really understand how to use it. Using polylines made more sense but I had to understand how to use the numpy methods first.

What libraries are used:
1. cv2
2. numpy
