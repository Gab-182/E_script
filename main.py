import os

#➜ Files inside project dir
from res.colors import *
from algorithm import distribute_all_comps_users
from request_data import create_users_dict, add_user_seat
from chosen_labs.seats_comps import comp1, comp2, comp3
from send_emails import send_emails
#=================================================================================#

event_id = 11167

#=================================================================================#
def	users():
	#➜ Creating dictionary that contain the users data with their last seat
	users_data = create_users_dict(event_id)
	users_data = add_user_seat(users_data)
	#➜ Distribution of the labs seats for the users
	distribute_all_comps_users(users_data, comp1, comp2, comp3)

#=================================================================================#
def main():
	choice = input("""
➜ Choose:
  [1] ➢ Run the script for the cursus users [+] sending the emails [press 1]
  [2] ➢ Sending emails to the users if you already have (users_data.csv) [press 2]
      ➢ """)

	while True:

		if choice == "1":
			users()
			#➜ Sending emails for the users
			send_emails("users_data.csv")
			return True

		#➜ Sending emails to the users
		elif choice == "2":
			if os.path.exists("./users_data.csv"):
				send_emails("users_data.csv")
				return True
			else:
				print("The file [users_data.csv] dose not exist in your directory !!!")
				print("You should create it first by pressing [1]")
				return False

		else:
			os.system("clear")
			print("➜ " + B + R + "Invalid choice ❌❌" + RES)
			choice = input("""
➜ Please choose again wisely:
  [1] ➢ Run the script for the cursus users [+] sending the emails [press 1]
  [2] ➢ Sending emails to the users if you already have (users_data.csv) [press 2]
      ➢ """)

#=================================================================================#
if __name__ == "__main__":
	main()

#=================================================================================#