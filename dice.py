import random
exitprogram=0
while exitprogram != "q":
	print("This is Waldo's dice rolling program")
	print("Press enter to roll")
	input()
	number=random.randint(1,6)
	if number==1:
		print("[-----------]")
		print("[           ]")
		print("[     O     ]")
		print("[           ]")
		print("[-----------]")
		print("You rolled a one")
		print()
		print("Type 'q' to quit")
		exitprogram=input()
	if number==2:
		print("[-----------]")
		print("[           ]")
		print("[  O     O  ]")
		print("[           ]")
		print("[-----------]")
		print("You rolled a two")
		print("Type 'q' to quit")
		exitprogram=input()
	if number==3:
		print("[-----------]")
		print("[  O     O  ]")
		print("[           ]")
		print("[     O     ]")
		print("[-----------]")
		print("You rolled a 3")
		print("Type 'q' to quit")
		exitprogram=input()
	if number==4:
		print("[-----------]")
		print("[  O     O  ]")
		print("[           ]")
		print("[  O     O  ]")
		print("[-----------]")
		print("You rolled a 4")
		print("Type 'q' to quit")
		exitprogram=input()
	if number==5:
		print("[-----------]")
		print("[  O     O  ]")
		print("[     O     ]")
		print("[  O     O  ]")
		print("[-----------]")
		print("You rolled a 5")
		print("Type 'q' to quit")
		exitprogram=input()	
	if number==6:
		print("[-----------]")
		print("[  O     O  ]")
		print("[  O     O  ]")
		print("[  O     O  ]")
		print("[-----------]")
		print("You rolled a 6")
		print("Type 'q' to quit")
		exitprogram=input()