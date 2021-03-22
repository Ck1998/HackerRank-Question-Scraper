from smtplib import SMTP_SSL, SMTPException


sender = '<YOUR GOOGLE EMAIL ID>'
gmail_password = "<GOOGLE APP PASSWORD>"
recv = [] # List of recipients
SUBJECT = "Hackerrank question for Today"


def send_email(questions_dict: dict):
    message = ""

    for topic, questions in questions_dict.items():
        temp = ""
        for q in questions:
            temp += f"{q}\n"
        message += f"{topic}:\n{temp}"

    email_text = """\
        From: %s
        To: %s
        Subject: %s

        %s
        """ % (sender, ", ".join(recv), SUBJECT, message)

    try:
        server = SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(sender, gmail_password)
        server.sendmail(sender, recv, email_text)
        server.close()
        print("sent")
    except SMTPException:
        print("error")
