from threading import Thread
from api_lib.intra import ic
from res.colors import *
ic.progress_bar=True




#=============================================================================#
def	request_data(event_id):
	"""
	#➜ Requesting data according the event_id and return a list of data

	--------
	⦿params:
	➤ event_id: the id for the requested event.
	"""

	exam = ic.pages_threaded(f"events/{str(event_id)}/events_users")
	return exam

#=============================================================================#
def	create_users_dict(event_id):
	"""
	Requesting data about pisciners who subscribed to the exam and store the 
	(id:[final_mark, status, validated?, emails, login]) into users_data{} 
	dictionary
	--------
	⦿return: 
	users_data
	"""

	users_data = {}

	print("➜ " + B + BL + "Requesting Exams Data ...." + RES)
	#➜ store exam_event data into users_data{}
	for p in request_data(event_id):
		users_data[p['user']['id']] = [p['user']['email'], p['user']['login']]

	return users_data

#=============================================================================#
def	request_user_seat(users_data, user_id):
	"""
	Requesting the last seat according to user id and append that to 
	users_data{} value
	--------
	⦿params:
	➤ users_data{}: dictionary that contains the users that subscribed 
	to any one from the exams
	➤ user_id: the id of the user
	"""
	seats = ic.get("users/" + str(user_id) + "/locations").json()
	for p in seats:
		seat = p['host']
		users_data[user_id].append(seat)
		break

#=================================================================================#
def	add_user_seat(users_data):
	"""
	Adding the last seat for each user who subscribed to any of the exams and return 
	users_data{}
	--------
	⦿params:
	➤ users_data{}: dictionary that contains the users that subscribed to any one 
	from the exams
	--------
	⦿return:

	➤ users_data{}
	"""
	print("➜ " + B + G + "Requesting info about user last seat\n" + B + Y + 
	"➤➤➤ Please be patient ➤➤➤" + RES)
	threads = []
	for user_id in users_data:
		threads.append (Thread (target=request_user_seat,args=(users_data, user_id)))
		threads[-1].start()
	for t in threads:
		t.join()

	return users_data

#=================================================================================#
