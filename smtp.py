import smtplib

sender='gdimitrov@borica.bg'
receiver='gdimitrov@borica.bg'

message='''From:Georgi Dimitrov
To:gdimitrov@borica.bg
Subject:test
this a test nessage.
'''
try:
	smtpObj = smtplib.SMTP('localhost')
	smtpObj.sendmail(sender, receiver, message) 
	print "Successfully sent email"
except SMTPException:
	 print "Error: unable to send email"
