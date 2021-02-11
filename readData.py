with open("dummydata.csv", "r") as file:
    all_lines = file.readlines()
    for line in all_lines:
        words = line.split(",")
        for word in words:
            print(word)

	
