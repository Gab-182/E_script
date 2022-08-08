from res.colors import *



#=================================================================================#
def	range_checker(labs):
	"""
	Check whether the items of labs[] are all in the range (1, 2, 3)

	--------
	⦿params:
	➤ labs[]: the list of all the chosen labs
	"""

	i = 0
	if len(labs) == 0:
		return False
	while i < len(labs):
		if int(labs[i]) < 1 or int(labs[i]) > 3:
			return False
		i += 1
	return True

#=================================================================================#
def	check_if_duplicates(labs):
	"""
	Check if there duplicates in the labs list

	--------
	⦿params:
	➤ labs[]: the list of all the chosen labs
	"""

	set_of_elements = set()
	for elem in labs:
		if elem in set_of_elements:
			return True
		else:
			set_of_elements.add(elem)
	return False


#=================================================================================#
def	lab_raws_seats(seats_list, list_length, labs, lab_raws):
	"""
	Generate all the seats names for the lab from the arguments

	--------
	⦿params:
	➤ seats_list[]: the list that contains the generated seats
	➤ list_length: the length of the labs[] list used as an index to get the required lab
	➤ labs[]: the list of all the chosen labs
	➤ lab_raws: the number of the raws in the (labs[list_length]) lab
	"""

	raw = 1
	while raw <= lab_raws:
		seat = 1
		while seat <= 14:
			seats_list.append("lab" + labs[list_length] + "r" + str(raw) + "s" + str(seat))
			seat += 1
		raw += 1

#=================================================================================#
def	get_exam_labs():
	"""
	Collecting labs data from the examiner

	--------
	⦿return:
	➤ labs[]: the list of all the chosen labs
	"""

	while True:
		labs = list(input("➜ Enter exam labs number separated by spaces:\n➢ ").split())

		#➜ Check if all the input is integer numbers.
		while not all([item.isdigit() for item in labs])\
			or not range_checker(labs)\
			or check_if_duplicates(labs):
			print("➜ " + B + R + "Invalid choice ❌❌" + RES)
			labs = list(input("➜ Please enter numbers from (1, 2, 3) separated by spaces, without duplicates:\n➢ ").split())

		#➜ Check if the examiner want to continuo with their choice.
		to_continue = input("➜ Are you sure you want to continue with the current labs? (y, n)\n➢ ").lower()
		while to_continue not in ("y", "n"):
			print("➜ " + B + R + "Invalid choice ❌❌" + RES)
			to_continue = input("➜ Please choose (y or n)\n➢ ")
		if to_continue == "y":
			break

	return labs

#=================================================================================#
def generate_seats(labs):
	"""
	Generate a list of all the seats in the chosen (lab/labs).

	--------
	⦿params:
	➤ labs[]: the list of all the chosen labs

	--------
	⦿return:

	➤ seats_list
	"""

	seats_list = []
	list_length = 0
	
	while list_length < len(labs):
		if labs[list_length] == '1':
			lab_raws_seats(seats_list, list_length, labs, 6)
		elif labs[list_length] == '2':
			lab_raws_seats(seats_list, list_length, labs, 4)
		elif labs[list_length] == '3':
			lab_raws_seats(seats_list, list_length, labs, 8)
		list_length += 1

	return seats_list

#=================================================================================#
#➜ Let the examiner choose in which labs the exam is going to happen
labs = get_exam_labs()

#➜ Generate all the seats names for these labs
seats_list = generate_seats(labs)

#=================================================================================#