import cv2
import numpy as np

# Load the predefined dictionary
dictionary = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_6X6_250)

# Generate the marker
markerImage = np.zeros((200, 200), dtype=np.uint8)
markerImage = dictionary.drawMarker(33, 200)
cv2.imwrite("marker33.png", markerImage)

# Placeholder function for generating voice. 
# You can replace this with your actual model's function.
def generate_voice(text):
    print(f"Speaking: {text}")

# Initialize webcam
cap = cv2.VideoCapture(0)

# Placeholder for lip-sync animation (oscillating circle size)
circle_radius = 30
direction = 1
max_radius = 40
min_radius = 20

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Convert the frame to gray
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect ArUco markers
    parameters = cv2.aruco.DetectorParameters_create()
    corners, ids, rejectedImgPoints = cv2.aruco.detectMarkers(gray, dictionary, parameters=parameters)

    # If we detected any markers, overlay animated circle (figure)
    if ids is not None:
        for corner, id in zip(corners, ids):
            # Get the center of the marker
            cX = int((corner[0][0][0] + corner[0][2][0]) / 2)
            cY = int((corner[0][0][1] + corner[0][2][1]) / 2)

            # Draw the animated circle (figure) at the center
            cv2.circle(frame, (cX, cY), circle_radius, (0, 255, 0), -1)

            # Update the circle radius for animation
            circle_radius += direction
            if circle_radius > max_radius or circle_radius < min_radius:
                direction = -direction

            # Generate the voice (replace with your model's function later)
            generate_voice("Hello AR!")

    # Display the frame
    cv2.imshow("Frame", frame)

    # Check for 'q' key to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
