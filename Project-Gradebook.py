last_semester_gradebook = [["politics", 80], ["latin", 96], ["dance", 97], ["architecture", 65]]

subjects = ["physics", "calculus", "poetry", "history"]
grades = [98, 97, 85, 88]

gradebook = [["physics", 98], ["calculus", 97], ["poetry", 85], ["history", 88]]

comp = ["computer science", 100]
vis = ["visual arts", 93]

gradebook.append(comp)
gradebook.append(vis)

gradebook[-1][-1] = 98

gradebook[2].remove(85)

gradebook[2].append("Pass")

full_gradebook = last_semester_gradebook + gradebook




print(full_gradebook)