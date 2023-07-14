import qrcode
import cv2


def encodetoqr(data, filename="qrcode.png"):
    """Encode the data paramater into QR Code and save the image to filename provided"""
    qr = qrcode.QRCode(version=4, box_size=10)
    qr.add_data(data)
    qr.make()
    encodeddata = qr.make_image()
    encodeddata.save(filename)


def decodefromqr(filename):
    """Decode the qrcode image and return the data"""
    qrimage = cv2.imread(filename)
    data, vertices, binaryqrcode = cv2.QRCodeDetector().detectAndDecode(qrimage)
    if vertices is None:
        return "ERROR"
    else:
        return data
    