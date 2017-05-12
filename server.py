import tornado.ioloop 
import tornado.web
import smtplib
    
class emailHandler(tornado.web.RequestHandler):
    def get(self):
        self.add_header("Access-Control-Allow-Origin", "*")
        email = self.get_argument("email")
        with open("emailLog.txt", "a") as emailFile:
            emailFile.write(email + "\n")
            
        sender = 'snazzyemailsender@gmail.com'
        receivers = ['programmelearn@gmail.com', 'randomiseme33@gmail.com']

        userMessage = "reply-to: programmelearn@gmail.com, randomiseme33@gmail.com\nSubject: Thank you for using http://academical.ml\n\nNow you can send us feedbacks through this email.\n:)"

        adminMessage = "reply-to:" + email + "\nSubject: New Email Submission\n\nSomeone has submitted their email address!!\nThe email address was: " + email + "\nReply to this email to send message to user."

        try:
           smtpObj = smtplib.SMTP_SSL('smtp.gmail.com:465')
           smtpObj.login("snazzyemailsender@gmail.com", "wsxcdeWSXCDE99!")
           smtpObj.sendmail(sender, receivers, adminMessage)         
        except SMTPException:
           print "Error: unable to send email"
        finally:
           smtpObj.quit()
        try:
           smtpObj = smtplib.SMTP_SSL('smtp.gmail.com:465')
           smtpObj.login("snazzyemailsender@gmail.com", "wsxcdeWSXCDE99!")
           smtpObj.sendmail(sender, email, userMessage)    
        except SMTPException:
           print "Error: unable to send email"
        finally:
           smtpObj.quit()
            


if __name__ == "__main__":
    app = tornado.web.Application([
        (r"/", emailHandler),
    ])
    app.listen(95) 
    tornado.ioloop.IOLoop.current().start()






