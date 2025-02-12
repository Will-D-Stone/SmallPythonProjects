import qrcode

def generate_website_qr_code(url):
    # Create an object
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=20,
        border=2,
    )
    #Adds the data and creates a QR code
    qr.add_data(url)
    qr.make(fit=True) 

    #Creates a png file with the QR code
    #Will Overwrite any previous file named qrcode.png in the folder
    #Seems unnecessary to work around this at this time
    code = qr.make_image(fill_color="black", back_color="white")
    code.save("qrcode.png")
    code.show()

if __name__ == "__main__":
    
    # Users can scan the QR Code to take them to the entered website
    website_url = input("Input your website url: ")

    generate_website_qr_code(website_url)
    print(f"QR code for '{website_url}' ")
    