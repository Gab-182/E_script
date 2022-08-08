from chosen_labs.exam_choices import seats_list



#=================================================================================#

def	first_combination(seats_list):
	"""
	Create a combination of the seat that contains seats [s1, s7, s8, s14]
	from all raws of the chosen labs
	NOTE: The students are going to distribute at this combination first
	--------
	⦿params:
	➤ seats_list[]: the list that contains the generated seats

	--------
	⦿return:
	➤ first_combination[]: list of the first combination of generated seats
	"""

	first_combination = []
	list_len = len(seats_list)

	if (list_len != 0):
		for seat in seats_list:
			if (seat[6:] == "s1" or
				seat[6:] == "s7" or
				seat[6:] == "s8" or
				seat[6:] == "s14"):
				first_combination.append(seat)

	return first_combination

#=================================================================================#
def	second_combination(seats_list):
	"""
	Create a combination of the seat that contains seats [s3, s5, s10, s12]
	from all raws of the chosen labs
	NOTE: The students are going to distribute at this combination after filling
	all the seats from the first_combination[]
	--------
	⦿params:
	➤ seats_list[]: the list that contains the generated seats

	--------
	⦿return:
	➤ second_combination[]: list of the second combination of generated seats
	"""

	second_combination = []
	list_len = len(seats_list)

	if (list_len != 0):
		for seat in seats_list:
			if (seat[6:] == "s3"  or
				seat[6:] == "s5"  or
				seat[6:] == "s10" or
				seat[6:] == "s12"):
				second_combination.append(seat)

	return second_combination

#=================================================================================#
def	third_combination(seats_list):
	"""
	Create a list of seats that remain in the seats_list
	and remove all these seats from the seats_list[]
	NOTE: The students are going to distribute at this combination after filling
	all the seats from both first_combination[] and second_combination[]
	--------
	⦿params:
	➤ seats_list[]: the list that contains the generated seats

	--------
	⦿return:
	➤ third_combination[]: list of the third combination of generated seats
	"""

	third_combination = []
	list_len = len(seats_list)

	if (list_len != 0):
		for seat in seats_list:
			if not (seat[6:] == "s1"  or
					seat[6:] == "s7"  or
					seat[6:] == "s8"  or
					seat[6:] == "s14" or
					seat[6:] == "s3"  or
					seat[6:] == "s5"  or
					seat[6:] == "s10" or
					seat[6:] == "s12"):
				third_combination.append(seat)

	return third_combination

#=================================================================================#
#➜ Generate all the three combination and store the values inside three variables 
#  to use theme inside the main algorithm

comp1 = first_combination(seats_list)
comp2 = second_combination(seats_list)
comp3 = third_combination(seats_list)

#=================================================================================#