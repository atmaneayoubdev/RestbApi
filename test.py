import cv2
import json
import base64

# Load JSON data
with open('bbox.json', 'r') as f:
    data = json.load(f)

# Extract bounding box coordinates
bbox = data['response']['detections'][0]['bbox']
x_min, y_min, x_max, y_max = bbox

# Read image
image = cv2.imread('image.jpeg')

# Draw bounding box on image
color = (0, 255, 0)  # BGR color format (green)
thickness = 2
cv2.rectangle(image, (x_min, y_min), (x_max, y_max), color, thickness)

# Save the image with the bounding box
cv2.imwrite('mask.jpeg', image)

# Convert image to base64
retval, buffer = cv2.imencode('.jpg', image)
base64_image = base64.b64encode(buffer).decode('utf-8')

# Save base64 representation to a file
with open('base64_image.txt', 'w') as f:
    f.write(base64_image)

# Display image with bounding box
cv2.imshow('Image with Bounding Box', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
