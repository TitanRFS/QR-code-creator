import qrcode

def generate_qrcode(text,file_name):
    qr=qrcode.QRCODE(
        version=1,
        error_correction = qrcode.constants.ERROR,
        box_size=10,
        border=4
    )
    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color="#6aff9b", back_color="#000000")
    img.save(file_name)

    #input text to generate QR
    text = "https://github.com/titanrfs"
    #File name
    file_name = "qr_code.png"
    generate_qrcode(text, file_name)
    print(f"QR code saved as (file_name)") #print the file name