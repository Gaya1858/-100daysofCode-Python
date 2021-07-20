'''
Email SMTP and the datetime module
automated birthday wishes
Email SMTp - simple mail transfer protocol - is a pre bundled with python library
sendind emails using python
'''
# import smtplib
import datetime as dt
#
# my_email = "tbite2256@yahoo.com" # tbite2256 is my identity and gmail.com is an identity tot he email provider
# password ="gaya123456789!"
# connection= smtplib.SMTP("smtp.mail.yahoo.com")
#
# connection.starttls()# transport layer security. it makes the connection secure with email server.
# # Uses some kind of encryption
# connection.login(user=my_email,password=password)
# connection.sendmail(from_addr=my_email,to_addrs="tbite2256@gmail.com",msg="Subject:Hello\n\n "
#                                                                           "This is just test email from python")
# connection.close()

now = dt.datetime.now() # current time wirth date year
print(now)# display (2021-07-20 14:36:20.917049) type = datetime object
y =now.year # class interger
m =now.month # integer
day_of_week = now.weekday()
print(day_of_week) # today is tuesday and it returns 1 as computers start from 0 ( monday0, t =1...)

