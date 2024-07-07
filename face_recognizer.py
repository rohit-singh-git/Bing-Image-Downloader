import face_recognition
import os
import shutil


def load_face_encoding(image_path):
    image = face_recognition.load_image_file(image_path)
    face_encodings = face_recognition.face_encodings(image)
    if face_encodings:
        return face_encodings[0]
    return None


def filter_images(image_folder, known_face_encoding):
    for filename in os.listdir(image_folder):
        if filename.endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
            image_path = os.path.join(image_folder, filename)
            image = face_recognition.load_image_file(image_path)
            face_encodings = face_recognition.face_encodings(image)

            match_found = False
            for face_encoding in face_encodings:
                match = face_recognition.compare_faces([known_face_encoding], face_encoding, tolerance=0.56)
                if match[0]:
                    match_found = True
                    break

            if not match_found:
                shutil.copy2(image_path, "deleted")
                os.remove(image_path)


# Load and process the person image to get the face encoding
person_image_path = 'image_21.jpg'
known_face_encoding = load_face_encoding(person_image_path)

if known_face_encoding is not None:
    # Example usage
    filter_images('samantha prabhu', known_face_encoding)
else:
    print("No faces found in the provided person image.")
