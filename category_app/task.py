from celery.decorators import task


@task(name="updation_sending_task")
def send_updation(category_name):
    import smtplib  # lazy import

    FROM = "gauravskt22@gmail.com"
    TO = "gaurav.baliyan@bigdrop.io"
    SUBJECT = "New category generated(Assignment test mail)"
    TEXT = "hi, \nThis is mail regard to new category post.({}).\n\n Note:- This is test case only. Ignore it.".format(category_name)

    # This is for testing purpose here, we can put in environ.
    USER= "auto.bike1992@gmail.com"
    PASSWORD = "arya@arya"

    # Prepare actual message
    message = """From: %s\nTo: %s\nSubject: %s\n\n%s
    """ % (FROM, ", ".join(TO), SUBJECT, TEXT)

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(USER, PASSWORD)
        server.sendmail(FROM, TO, message)
        server.close()
    except Exception as e:
        print (e)
        pass
