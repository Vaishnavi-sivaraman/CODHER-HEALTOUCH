import cv2 as cv
import numpy as np

def home():
   BODY_PARTS = { "Nose": 0, "Neck": 1, "RShoulder": 2, "RElbow": 3, "RWrist": 4,
               "LShoulder": 5, "LElbow": 6, "LWrist": 7, "RHip": 8, "RKnee": 9,
               "RAnkle": 10, "LHip": 11, "LKnee": 12, "LAnkle": 13, "REye": 14,
               "LEye": 15, "REar": 16, "LEar": 17, "Background": 18 }

   POSE_PAIRS = [ ["Neck", "RShoulder"], ["Neck", "LShoulder"], ["RShoulder", "RElbow"],
               ["RElbow", "RWrist"], ["LShoulder", "LElbow"], ["LElbow", "LWrist"],
               ["Neck", "RHip"], ["RHip", "RKnee"], ["RKnee", "RAnkle"], ["Neck", "LHip"],
               ["LHip", "LKnee"], ["LKnee", "LAnkle"], ["Neck", "Nose"], ["Nose", "REye"],
               ["REye", "REar"], ["Nose", "LEye"], ["LEye", "LEar"] ]

   inWidth = 368
   inHeight = 368

   net = cv.dnn.readNetFromTensorflow("graph_opt.pb")

   def draw_pose(image):
    frameWidth = image.shape[1]
    frameHeight = image.shape[0]
    
    net.setInput(cv.dnn.blobFromImage(image, 1.0, (inWidth, inHeight), (127.5, 127.5, 127.5), swapRB=True, crop=False))
    out = net.forward()
    out = out[:, :19, :, :]  # MobileNet output [1, 57, -1, -1], we only need the first 19 elements

    assert(len(BODY_PARTS) == out.shape[1])

    points = []
    for i in range(len(BODY_PARTS)):
        # Slice heatmap of corresponding body part.
        heatMap = out[0, i, :, :]

        # Find the local maximum.
        _, conf, _, point = cv.minMaxLoc(heatMap)
        x = (frameWidth * point[0]) / out.shape[3]
        y = (frameHeight * point[1]) / out.shape[2]
        # Add a point if its confidence is higher than the threshold.
        points.append((int(x), int(y)) if conf > 0.2 else None)

    for pair in POSE_PAIRS:
        partFrom = pair[0]
        partTo = pair[1]
        assert(partFrom in BODY_PARTS)
        assert(partTo in BODY_PARTS)

        idFrom = BODY_PARTS[partFrom]
        idTo = BODY_PARTS[partTo]

        if points[idFrom] and points[idTo]:
            cv.line(image, points[idFrom], points[idTo], (0, 255, 0), 3)
            cv.circle(image, points[idFrom], 5, (0, 0, 255), -1)
            cv.circle(image, points[idTo], 5, (0, 0, 255), -1)

    return image, points

# Load input image
   input_image = cv.imread("namaste-yoga.jpg")

# Draw pose lines on input image
   annotated_image, reference_points = draw_pose(input_image)
   window_name = "Annotated Image"
   cv.namedWindow(window_name, cv.WINDOW_NORMAL)  # Create a resizable window
   cv.resizeWindow(window_name, 800, 800)  # Set window size

# Save annotated image
   cv.imwrite("namaste_output.jpg", annotated_image)

# Open window for annotated image
   cv.imshow("Annotated Image", annotated_image)

# Open webcam window
   cap = cv.VideoCapture(0)

   while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Draw pose lines on webcam frame
    _, user_points = draw_pose(frame)

    # Check if user points match reference points
    match_count = sum(1 for user_point, reference_point in zip(user_points, reference_points) if user_point is not None and reference_point is not None)

    if match_count >= len(reference_points) * 0.55:  # If more than 55% points match
        feedback = "Success! You are in the correct posture. Score: "+str(match_count)+" Expected: "+ str(len(reference_points) * 0.55)
        feedback_color = (0, 255, 0)  # Green color for success
    else:
        feedback = "Incorrect posture. Please adjust your posture. Score: "+str(match_count)+" Expected: "+ str(len(reference_points) * 0.55)
        feedback_color = (0, 0, 255)  # Red color for incorrect posture

    # Display feedback on webcam window
    cv.putText(frame, feedback, (10, 40), cv.FONT_HERSHEY_SIMPLEX, 0.5, feedback_color, 2)
    cv.imshow("Webcam", frame)

    # Check for key press to exit
    key = cv.waitKey(1)
    if key == ord('q'):
        break

# Release resources
   cap.release()
   cv.destroyAllWindows()