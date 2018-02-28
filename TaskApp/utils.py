import base64
import random
import smtplib
import string

from rest_framework.renderers import JSONRenderer


def send_email(to_addr_list,
               subject, message,
               from_addr='lobanovskysvet@app.com'):
    header = 'From: %s\n' % from_addr
    header += 'To: %s\n' % to_addr_list
    header += 'Subject: %s\n\n' % subject
    message = header + message

    server = smtplib.SMTP(host='mail.smtp2go.com', port=2525)
    server.login(user='lobanovskysvet@app.com', password='qazwsxedc1')
    problems = server.sendmail(from_addr, [to_addr_list], message)
    server.quit()
    return problems


def send_reset_password_email(to_addr, restorePasswordData):
    send_email(to_addr,
               "Reset passoword",
               "To reset password folow link: http://localhost:8000/api/reset/" + restorePasswordData)


def get_encoded_base64_user_data_string(userData):
    return base64.urlsafe_b64encode(JSONRenderer().render(userData.data)).decode("utf-8")


def get_decoded_base64_user_data_encoded_string(base64String):
    return base64.urlsafe_b64decode(base64String).decode("utf-8")


def get_random_string(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))
