import csv
import random
from res.colors import *



#=================================================================================#
def	dict_shuffle(users_data):
	"""
	Shuffle the users_data{} dictionary so each time you run the code, 
	the user is going to get different seat.
	--------
	⦿params:
	➤ users_data{}: dictionary that contains the users that subscribed to 
	any one from the exams
	--------
	⦿return:

	➤ users_data{}
	"""

	l = list(users_data.items())
	random.shuffle(l)
	users_data = dict(l)

	return users_data

#=================================================================================#
def distribute_comp1(comp1, users_data):
	"""
	Distribute the seats of comp1[] at the users from users_data{} and store 
	(id, final_mark, status, validated?, emails, login, last seat, given seat)
	inside csv file in the same directory
	--------
	⦿params:
	➤ users_data{}: dictionary that contains the users that subscribed to 
	any one from the exams
	➤ comp1[]: The list for the first combination of chosen labs seats
	"""

	#➜ shuffle the users_data{} dictionary
	users_data = dict_shuffle(users_data)
	#➜ open the csv file and add the data of the users.
	csv_file = open ('users_data.csv','w', newline='')

	#➜ write the header first at the top of the csv file.
	headerList = ['user_id', 'emails', 'login', 'last seat', 'given_seat']
	writer = csv.writer(csv_file)
	writer.writerow(headerList)

	#➜ Loop through the users_data{}
	for id, data in users_data.items():
		#➜ len(data == 3) -> means that we did not gave the user a seat.
		if (len(data) == 3):
			if comp1:
				#➜ check if the seat is same as the current user seat.
				if (comp1[0] not in data):
					users_data[id].append(comp1[0])
					#➜ write the changes to csv file.
					writer.writerow([id, *data])
					comp1.remove(comp1[0])
				#➜ if the first seat from comp1 same as the current seat for the user
				#	then give the user the next seat from comp1 if it is exist.
				elif (comp1[1]):
					users_data[id].append(comp1[1])
					writer.writerow([id, *data])
					comp1.remove(comp1[1])

	csv_file.close()

#=================================================================================#
def distribute_comp2(comp2, users_data):
	"""
	Distribute the seats of comp2[] at the users from users_data{} and store 
	(id, final_mark, status, validated?, emails, login, last seat, given seat)
	inside csv file in the same directory
	--------
	⦿params:
	➤ users_data{}: dictionary that contains the users that subscribed to 
	any one from the exams
	➤ comp2[]: The list for the second combination of chosen labs seats
	"""

	#➜ shuffle the users_data{} dictionary
	users_data = dict_shuffle(users_data)
	#➜ open the csv file and append the new data to its end
	csv_file = open ('users_data.csv','a', newline='')
	writer = csv.writer(csv_file)

	#➜ Loop through the users_data{}
	for id, data in users_data.items():
		#➜ len(data == 3) -> means that we did not gave the user a seat.
		if (len(data) == 3):
			if comp2:
				#➜ check if the seat is same as the current user seat.
				if (comp2[0] not in data):
					users_data[id].append(comp2[0])
					#➜ write the changes to csv file.
					writer.writerow([id, *data])
					comp2.remove(comp2[0])
				#➜ if the first seat from comp2 same as the current seat for the user
				#	then give the user the next seat from comp2 if it is exist.
				elif (comp2[1]):
					users_data[id].append(comp2[1])
					writer.writerow([id, *data])
					comp2.remove(comp2[1])

	csv_file.close()

#=================================================================================#
def distribute_comp3(comp3, users_data):
	"""
	Distribute the seats of comp3[] at the users from users_data{} and store 
	(id, final_mark, status, validated?, emails, login, last seat, given seat)
	inside csv file in the same directory
	--------
	⦿params:
	➤ users_data{}: dictionary that contains the users that subscribed to 
	any one from the exams
	➤ comp3[]: The list for the third combination of chosen labs seats
	"""

	#➜ shuffle the users_data{} dictionary
	users_data = dict_shuffle(users_data)
	#➜ open the csv file and append the new data to its end
	csv_file = open ('users_data.csv','a', newline='')
	writer = csv.writer(csv_file)

	#➜ Loop through the users_data{}
	for id, data in users_data.items():
		#➜ len(data == 3) -> means that we did not gave the user a seat.
		if (len(data) == 3):
			if comp3:
				#➜ check if the seat is same as the current user seat.
				if (comp3[0] not in data):
					users_data[id].append(comp3[0])
					#➜ write the changes to csv file.
					writer.writerow([id, *data])
					comp3.remove(comp3[0])
				#➜ if the first seat from comp3 same as the current seat for the user
				#	then give the user the next seat from comp3 if it is exist.
				elif (comp3[1]):
					users_data[id].append(comp3[1])
					writer.writerow([id, *data])
					comp3.remove(comp3[1])

	print("\n➜ " + B + R + "users_data.csv" + B + G + " has been created." + RES )
	print("➜ " + B + G + "Information for the " + B + Y + "users" + B + G + " stored inside users_data.csv" + RES)

	csv_file.close()

#=================================================================================#
def	distribute_all_comps_users(users_data, comp1, comp2, comp3):
	"""
	Execute all the three comps distributions

	--------
	⦿params:
	➤ comp1[]: The list for the first combination of chosen labs seats
	➤ comp2[]: The list for the second combination of chosen labs seats
	➤ comp3[]: The list for the third combination of chosen labs seats
	"""

	distribute_comp1(comp1, users_data)
	distribute_comp2(comp2, users_data)
	distribute_comp3(comp3, users_data)

#=================================================================================#