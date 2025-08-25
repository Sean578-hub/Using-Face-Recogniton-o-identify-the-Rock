import cv2
import face_recognition

rock = face_recognition.load_image_file("rock.jpg")
rock_encoding = face_recognition.face_encodings(rock)[0]


familly_rock = face_recognition.load_image_file("The rock.jpg")
familly_encoding = face_recognition.face_encodings(familly_rock)
familly_location = face_recognition.face_locations(familly_rock)
familly_bgr = cv2.cvtColor(familly_rock, cv2.COLOR_RGB2BGR)

for (face_encoding, (top, right, bottom, left)) in zip(familly_encoding, familly_location):
    match = face_recognition.compare_faces([rock_encoding], face_encoding)[0]
    if match:
        name = "The Rock"
        color = (0, 255, 0)
    else:
        name = "Unkown"
        color = (0, 0, 255)
    cv2.rectangle(familly_bgr, (left, top), (right, bottom), color, 2)
    cv2.putText(familly_bgr, name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, color, 2)
cv2.imwrite("Rock finder.jpg", familly_bgr)
cv2.imshow("Rock", familly_bgr)
cv2.waitKey(0)
cv2.destroyAllWindows()










