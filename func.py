from captcha.image import ImageCaptcha

def captcha_img(captcha_text):
    image=ImageCaptcha()
    data = image.generate(captcha_text)
    image.write(captcha_text,'cap_img.png')