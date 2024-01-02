import qrcode
features=qrcode.QRCode(version=1,box_size=30,border=2)
features.add_data('https://shivalikcollege.edu.in/')


features.make(fit=True)
generateImage=features.make_image(fill_color="black",back_color="white")
generateImage.save("qrcode.png")