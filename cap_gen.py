from random import *
from func import *
def captcha_gen():
    captcha_size=6
    captcha_text=""
    alpha=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    for i in range(captcha_size):
        if i==2 or i==4:
            captcha_text += choice(alpha)
        else:
            captcha_text += str(randint(0,9))
    print(captcha_text)
    captcha_img(captcha_text)

captcha_gen()

