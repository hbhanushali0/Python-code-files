
import cv2

img = cv2.imread('QRcode.png')
detector = cv2.QRCodeDetector()

data, bbox, straight_qrcode = detector.detectAndDecode(img)

print(data)
