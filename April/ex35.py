from sys import exit

print("""
         XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX                    
         XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX                    
         XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX                    
         XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX                    
         XXXXXX         XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX         XXXXXX                    
         XXXXXX         XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX         XXXXXX                    
         XXXXXX         XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX         XXXXXX                    
         XXXXXX X       XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX X       XXXXXX                    
         XXXXXX         XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX         XXXXXX                    
         XXXXXX         XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX         XXXXXX                    
         XXXXXX         XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX         XXXXXX                    
         XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX                    
		 """)

def king_room():
	print("Congratulations on reaching the final room my lord.")
	print("The king room is the true place for leaders.")
	print("What shall we do next my leige? Prepare for war, peace, or build our kingdom? ")
	ruler = input("> ") 
	
	if ruler == "war":
		dead("Peace comes before war sire")
	elif ruler == "peace":
		print("You shall rule fovever....THE END")
	else:
		print("Long live the king!")

def gold_room():
	print("This room is full of gold.")
	
	choice = input("How many pounds of gold will you take?> ")
	
	if "0" in choice or "1" in choice or "7" in choice:
		how_much = int(choice)

	else:
		dead("Man, learn to type a number.")
		
	if how_much < 50:
		print("Nice, you're not greedy, you win!")
		exit(0)
	elif how_much == 777:
		print("Welcome your majesty")
		king_room()
	else:
		dead("You greedy bastard!")
		

def bear_room():
	print("There is a bear here.")
	print("The bear has a bunch of honey.")
	print("The fat bear is in front of another door.")
	print("How are you going to move the bear?(taunt, take, open door)")
	bear_moved = False
	
	while True:
		choice = input("> ")
		
		if choice == "take honey":
			dead("The bear looks at you then slaps your face off.")
		elif choice == 'taunt bear' and not bear_moved:
			print("The bear has moved from the door.")
			print("You can go through it now.")
			bear_moved = True
		elif choice == 'taunt bear' and bear_moved:
			dead("The bear gets pissed off and chews your leg off.")
		elif choice == 'open door' and bear_moved:
			gold_room()
		else:
			print("I got no idea what that means.")
			

def cthulhu_room():
	print("Here you see the great evil Cthulhu.")
	print("He, it, whatever stares at you and you go insane.")
	print("Do you flee for your life, eat your head or sit and calmly cover your eyes?")
	
	choice = input("> ")
	
	if "flee" in choice:
		start()
	elif "head" in choice:
		dead("Well that was tasty!")
	elif "cover" in choice:
		print('Remember the number 777')
		gold_room()
	else:
		cthlhu_room()
			

def dead(why):
	print(why, "Good job!")
	exit(0)

def start():
	print("You are in a dark room.")
	print("There is a door to your right and left.")
	print("Which one do you take?")
	
	choice = input("> ")
	
	if choice == "left":
		bear_room()
	elif choice == "right":
		cthulhu_room()
	else:
		dead("You stumble around the room until you starve")
		
start()