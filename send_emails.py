import csv
import smtplib
import getpass
from res.colors import *



#=================================================================================#
def	send_emails(dict_data):
	"""
	Send emails to the user inside dict_data file (csv file)

	--------
	⦿params:
	➤ dict_data: the csv file that contains the users data
	"""

	while True:
		#➜ Take the sender login credentials.
		sender = input("\n➜ Enter the sender email please\n➜ ")
		password = getpass.getpass("➜ Enter the sender password please\n➜ ")

		#➜ The message part (subject, text)
		subject = "Exam seat"
		text = """
Hello {name}\n
your exam seat for the upcoming exam is [{given_seat}]
Make sure to set in that seat precisely.
	"""
		msg = 'Subject: {}\n\n{}'.format(subject, text)

		#➜ Connect to host
		try:
			port = 587
			server = "smtp-mail.outlook.com"
			server = smtplib.SMTP(server, port)
		except smtplib.socket.gaierror:
			print("➜ " + B + R + "Failed to connect to SMTP server, try to enter you credentials again" + RES)
			continue

		#➜ Login
		try:
			server.starttls()
			server.login(sender, password)
		except smtplib.SMTPAuthenticationError:
			print("➜ " + B + R + "Login failed, Wrong credentials!!, Try again" + RES)
		except Exception:
			print("➜ " + B + R + "Login failed, Wrong credentials!!, Try again" + RES)
			continue

		#➜ Reading csv file and send the emails && Send message
		try:
			with open(dict_data) as file:
				threads = []
				reader = csv.reader(file)
				next(reader) # To skip the header row
				for row in reader:
					if len(row) > 0:
						name = row[2]
						email = row[1]
						given_seat = row[4]
						server.sendmail(sender, email, msg.format(name=name, email=email,given_seat=given_seat))
						print(Y + f"Email has been sent to {name}" + RES)
				print("➜ " + B + G + "All emails sent to the users successfully." + RES)
				return True
		except Exception:
			print("➜ " + B + R + "Error while reading CSV file" + RES)

		finally:
			server.quit()
			return True

#=================================================================================#
