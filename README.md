Current integration methods for non-invasive therapies like
physiotherapy and acupressure lack accuracy, personalization, and
standardized techniques.
- Difficulty in accurately identifying and stimulating specific
acupressure points and meridian lines compromises therapy
effectiveness.
- Physiotherapy patients with mobility limitations struggle to attend
sessions and require supervision for effective exercise execution.

- Technical challenges, such as locating pressure points,
hinder acupressure's popularity and efficacy in self administration.
- The project aims to address these challenges by offering
precise guidance, personalized routines, and enhanced
accessibility through innovative solutions

By leveraging
1. 3D models
2. Chatbot-driven symptom analysis, and
3. Real-time exercise detection, the project seeks to
revolutionize the integration of physiotherapy and
acupressure into daily healthcare practices.

Posture Estimation:

Pose Estimation Model: The code uses a pre-trained pose estimation model (grapht-opt.pb) to detect key points on a human body in images. These key points include parts like the nose, shoulders, elbows, wrists, hips, knees, and ankles.

Reference Image Processing: The code loads a reference image (in this case, "namaste-yoga.jpg") and uses the pose estimation model to detect key points on a person's body in this reference image. These key points serve as a reference for a correct posture.

Webcam Processing Loop: The code then opens a webcam feed and enters a loop where it continuously captures frames from the webcam.

Pose Detection on Webcam Frames: For each frame captured from the webcam, the code uses the same pose estimation model to detect key points on the person's body in the webcam frame.

Comparison with Reference Points: It then compares the key points detected in the webcam frame with the reference points obtained from the reference image. The comparison is based on the proximity of key points between the webcam frame and the reference image.

Feedback on Posture: Based on the comparison, the code provides feedback on whether the person's posture matches the reference posture. If the match percentage exceeds a certain threshold, it's considered a success, and the feedback is displayed in green. Otherwise, it's considered incorrect, and the feedback is displayed in red.

User Interaction: The code displays the webcam feed with overlaid feedback text indicating whether the posture is correct or not.

   Dependencies to be installed:  
      pip install opencv-python

(Posture estimation is done by employing OpenCV)

Symptom-driven chatbot

A "symptom-driven chatbot" is designed to assist users by providing accurate information and guidance based on the symptoms they provide. In this scenario, the chatbot leverages its training on legitimate datasets obtained from medical textbooks to ensure the accuracy and reliability of the information it delivers.

The chatbot provides the user with the accurate acupressure points to be pressed, along with corresponding images for visual reference. These acupressure points are tailored to the specific symptoms provided by the user, ensuring personalized guidance.

3D Model:

Interactive 3D Models: By presenting acupressure and acupuncture points on a 3D body mesh, users can visualize the points in a more immersive and intuitive manner. This interactive visualization enhances understanding and engagement with the acupressure points.

Zoom Functionality: With automatic zoom functionality, when a user clicks on a particular acupressure point suggested by the chatbot, the system automatically zooms in on that point within the 3D body mesh. This immediate focus on the selected point provides users with a clear and close-up view, facilitating accurate stimulation.

Visualizing Distances: Displaying the distance between points, perhaps in terms of "cun" (the width of a thumb), offers valuable reference information. This feature can aid users in understanding the spatial relationships between acupressure points and ensuring precise stimulation.

Promoting Self-Care and Wellness: Empowering users to perform acupressure techniques accurately at home promotes self-care and wellness. By providing accessible and reliable guidance through the chatbot and interactive 3D models, users can effectively manage their health and well-being.

For the 3D models, WebGL is a JavaScript API for rendering interactive 2D and 3D graphics within any compatible web browser without the use of plug-ins. WebGL is fully integrated with other web standards, allowing GPU-accelerated usage of physics, image processing, and effects in the HTML canvas.


### Visual Representation
[![](https://mermaid.ink/img/pako:eNpVkc9uwyAMxl_F4ry-QA6T-m-3XdbtlPTggpMgJYCMWZtVfZu9yV5sTtepKkiAwT9_n8XZ2OjIVKYd4tH2yALvmyYs6900JokjAgUhJgeHCRKK13APi8UzrOpVlFy6jrJkSNEH3YROAiN2BBgcfHpHEZhyiiFT3jcBdCyv-HrG4c73U_ZRemJME9CJ2Po7slJiU38ciKGIH_wXqVRP99JXuflm-Qav2tDwT66V3NbLlAZv1X0M0JLYXgmmVvsKlsDPhv9K2MjsE2pdKBlZ28pSmODopYfwANwEtirwUu8UJGijEhwT8TBpkhfxobsZfWBhG2wsjN38znREdjBSzrMP-flWRB30cXDgZ6Ooht1N77o2YZ73CMA8mZF4RO_0L8_zTWNUeKTGVHp01GIZpDFNuGgqFom7KVhTCRd6MiU5FNp47BhHU7U4ZLr8AvTlvR8?type=png)](https://mermaid.live/edit#pako:eNpVkc9uwyAMxl_F4ry-QA6T-m-3XdbtlPTggpMgJYCMWZtVfZu9yV5sTtepKkiAwT9_n8XZ2OjIVKYd4tH2yALvmyYs6900JokjAgUhJgeHCRKK13APi8UzrOpVlFy6jrJkSNEH3YROAiN2BBgcfHpHEZhyiiFT3jcBdCyv-HrG4c73U_ZRemJME9CJ2Po7slJiU38ciKGIH_wXqVRP99JXuflm-Qav2tDwT66V3NbLlAZv1X0M0JLYXgmmVvsKlsDPhv9K2MjsE2pdKBlZ28pSmODopYfwANwEtirwUu8UJGijEhwT8TBpkhfxobsZfWBhG2wsjN38znREdjBSzrMP-flWRB30cXDgZ6Ooht1N77o2YZ73CMA8mZF4RO_0L8_zTWNUeKTGVHp01GIZpDFNuGgqFom7KVhTCRd6MiU5FNp47BhHU7U4ZLr8AvTlvR8)
