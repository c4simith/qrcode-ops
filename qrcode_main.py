import qrcodeops

qrcodeops.encodetoqr("https://news.google.com")
decodedata = qrcodeops.decodefromqr("qrcode.png")
print(decodedata)
