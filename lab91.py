"""The first step is to create an SMTP object, each object is used for connection 
with one server."""

import smtplib
server = smtplib.SMTP('smtp.gmail.com', 587)

#Next, log in to the server
server.starttls()
server.login("ranjitharaju3010", "unique3010")

#Send the mail
msg = "hey"
server.sendmail("ranjitharaju3010@gmail.com", "priyankarmakar17@gmail.com", msg)
print('msg sent')
server.quit()