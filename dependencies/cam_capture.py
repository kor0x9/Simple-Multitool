import cv2
import requests

webhook_url = input("Your webhook : ")

# Ouvrir la webcam
cap = cv2.VideoCapture(0)

# Vérifier si la webcam est ouverte
if not cap.isOpened():
    print("Erreur : impossible d'ouvrir la webcam")
    exit()

# Prendre une photo
ret, frame = cap.read()
if ret:
    cv2.imwrite("photo.jpg", frame)
    print("Photo prise avec succès!")
    input("Press enter to leave")

    # Envoyer la photo à un webhook
    files = {"file": open("photo.jpg", "rb")}
    response = requests.post(webhook_url, files=files)
    if response.status_code == 200:
        print("Photo envoyée avec succès!")
        input("Press enter to leave")
    else:
        print("Erreur lors de l'envoi de la photo :", response.text)
        input("Press enter to leave")

else:
    print("Erreur : impossible de prendre une photo")
    input("Press enter to leave")

# Fermer la webcam
cap.release()
cv2.destroyAllWindows()
