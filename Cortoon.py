import numpy as np
import cv2

image = cv2.imread("C:\\Users\\Administrator\\Desktop\\PYTHON Final projects\\cartoonizingCv2\\gurbaz.jpg")
# C:\Users\Administrator\Desktop\python\image cartoonizing in cv2
# image = cv2.imread("gurbaz.jpg")
if image is None:
    print("not found")
    exit()


gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray = cv2.medianBlur(gray, 5)
edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 7, 7)


color = cv2.bilateralFilter(image, 9, 200, 200)
cartoon = cv2.bitwise_and(color,color, mask = edges)


# small_image = cv2.resize(image, (660, 400))#,fx = 0.5, fy = 0.5)
# cv2.imshow("image", small_image)
# cv2.imshow("small image", small_image)

resized_original = cv2.resize(image,(0,0), fx = 1, fy = 1)
resized_cartoon = cv2.resize(cartoon, (0,0), fx = 1, fy = 1)
resized_edges = cv2.resize(edges, (0,0), fx = 1, fy = 1)
combined = np.hstack((resized_original, resized_cartoon))
cv2.imshow("Original vs Cartoon",combined)  



# cv2.imshow("image", image)

# cv2.imshow("Original image", resized_original)  

# cv2.imshow("cartoon", resized_cartoon) 

# cv2.imshow("edges", resized_edges) 

# cv2.imshow("cartoon", cartoon) 


cv2.waitKey(0)
cv2.destroyAllWindows()