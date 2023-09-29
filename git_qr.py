# I am once again coding when I should be doing homework

def github_qr_generator():
    import qrcode
    from qrcode.image.styledpil import StyledPilImage
    from qrcode.image.styles.moduledrawers.pil import RoundedModuleDrawer
    from qrcode.image.styles.colormasks import SolidFillColorMask

    qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_M,
            image_factory=StyledPilImage
    )

    github = 'https://www.github.com/ari-gaskins'
    qr.add_data(github)
    qr.make(fit=True)

    img = qr.make_image(
                color_mask=SolidFillColorMask(
                    front_color=(255, 255, 255),
                    back_color=(82, 113, 255)
                ),
                module_drawer=RoundedModuleDrawer()
    )


    img_file = 'mygitqr.png'
    img.save(img_file)

#    img_file_path = '~/Documents/GitHub_QR/mygitqr.png'
    
#    with open('mygitqr.svg', 'wb') as file:
#        img.save(file)

github_qr_generator()
