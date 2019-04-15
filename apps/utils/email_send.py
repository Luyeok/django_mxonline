from users.models import EmailVerifyRecord
from django.core.mail import send_mail
from mxonline.settings import EMAIL_FROM
from random import Random

def send_register_email(email,send_type="register"):
    email_record = EmailVerifyRecord()
    random_str = generate_random_str(16)
    email_record.code= random_str
    email_record.email=email
    email_record.send_type=send_type
    email_record.save()

    email_title=''
    email_body=''
    if send_type=="register":
        email_title="慕学在线网注册激活链接"
        email_body='请点击下边的链接激活你的账号：http://127.0.0.1:8000/active/{0}'.format(random_str)
        send_status=send_mail(email_title,email_body,EMAIL_FROM,[email])
        if send_status==True:
            pass


def generate_random_str(randomlength=8):
    str=''
    chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
    length = len(chars)-1
    random= Random()
    for i in range(randomlength):
        str+=chars[random.randint(0,length)]
    return str