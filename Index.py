import qrcode
qr=qrcode.QRCode(
	version=1,
	box_size=10,
	border=5

	)
print("**********QR CODE GENERATOR**********\n")
print("|*|*|*|*|Kashipara.com|*|*|*|*|\n")
data = input("Please Enter Your Link: ")
qr.add_data(data)
qr.make(fit=True)
img=qr.make_image(fill="black",back_color="white")
img.save("2.png")
print("Done")
