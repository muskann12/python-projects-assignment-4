import cv2

img = cv2.imread("my_qr.png")
detector = cv2.QRCodeDetector()
data, bbox, _ = detector.detectAndDecode(img)

if data:
    print("🔓 Decoded text from QR Code:")
    print(data)
else:
    print("❌ QR Code not found.")
