import smtplib


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
