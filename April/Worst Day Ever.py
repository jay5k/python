from sys import exit

print("""XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
         XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
         XXXXXX______________________________________XXXXXX
         XXXXXX                                      XXXXXX
         XXXXXX______________________________________XXXXXX                                     
         XXXXXX______________________________________XXXXXX
		 XXXXXX                                      XXXXXX
         XXXXXX______________________________________XXXXXX
         XXXXXX______________________________________XXXXXX
		 XXXXXX                                      XXXXXX
		 XXXXXX______________________________________XXXXXX
		 XXXXXX______________________________________XXXXXX
		 XXXXXX                                      XXXXXX
		 XXXXXX______________________________________XXXXXX
		 XXXXXX                                      XXXXXX
         XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
""")

print("You return home from a long day of work and open the garage door.")
print("You exit the car and the kitchen door with a strange man standing in the doorway.")

def garage():
	print("Shocked the strange man asks for your name?\n")
	name = input("Well?...")
	
	print(f"Well {name} how was your day?")
	print("""1. Great, until you arrived
			 2. Who the hell are you?!?!?!
			 3  Terrible I don't want to talk about it
			 4  Dr. Timlin would not stop talking about NBA games
		""")
	
	mood = int(input("Please enter number response. \n>  "))
	if mood == 1:
		print(f"I'm happy to hear you are having a great day (name} and sad I've ruined it for you")
	elif mood == 2:
		print(f"I am you {name}, who are you?"
	elif mood == 3:
		print(f"Please do {name}")
	elif mood == 4:
		print(f"Classic T. He should really work on less KD and more deep cleans")
	else
		print("Please select a number")
	
	
	
