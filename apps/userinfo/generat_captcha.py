from captcha.image import ImageCaptcha
import random
import os
from txy import settings


number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
def random_captcha_text(char_set=number, captcha_size=4):
    captcha_text = []
    for i in range(captcha_size):
        c = random.choice(char_set)
        captcha_text.append(c)
    return captcha_text


# 生成字符对应的验证码
def gen_captcha_text_and_image():
    image = ImageCaptcha()
    captcha_text = random_captcha_text()
    captcha_text = ''.join(captcha_text)
    # print(captcha_text)
    image.write(captcha_text, os.path.join(settings.STATICFILES_DIRS[0], 'captcha.jpg'))  # 写到文件
    return captcha_text


if __name__ == '__main__':
    text = gen_captcha_text_and_image()
    print(os.path.join(settings.STATICFILES_DIRS[0], 'captcha.jpg'))
    print(text)