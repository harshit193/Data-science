import smtplib
try: 
    server = smtplib.SMTP("smtp.gmail.com",port=587)
    server.starttls()

    ##receive mail
    receiver_mail=input("enter the receiver e-mail:")

    # email credentials
    sender_email="joshitushar1774@gmail.com"
    password = "gahg fbau lkjf ozaz"


    #login to mail
    server.login(sender_email,password) 


    # sending mail
    subject=input("enter the subject:")
    body=input("enter the body:")
    message = f"Subject : {subject}\n\n{body}"
    server.sendmail(sender_email, receiver_mail,message)
    print("mail sent successfully")
    server.quit()
except Exception as e:
    print("an error occured",e)