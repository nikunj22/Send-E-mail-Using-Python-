import smtplib

sender_email = "chitrodanikunj22@gmail.com"
rec_email = "techmahasay@gmail.com"
password = input(str("Please Enter Your Email Password :"))
message = "Hello , Friend In this Video Will Be Show You SEnd Email Using Python...."

server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(sender_email, password)
print("Your Email Login is Succesfuly...")
server.sendmail(sender_email, rec_email,message)
print("Your Email has been Sent Sucessfully....",rec_email)
