#a.Using one statement with one print function
line_a_1 = ("*" * 19) + "\n" + "*" + (" " * 17) + "*\n" + "*" + (" " * 17) + "*\n" + ("*" * 19)
print(line_a_1)

#b.Using four statement with one print function
line_b_1 = "*" * 19 +"\n"
line_b_2 = "*" + " " * 17 + "*\n"
line_b_3 = line_b_2
line_b_4 = line_b_1
print(line_b_1 + line_b_2 + line_b_3 + line_b_4)

#c.Using four statement with four print function
line_c_1 = "*" * 19
line_c_2 = "*" + " " * 17 + "*"
line_c_3 = line_c_2
line_c_4 = line_c_1
print(line_c_1)
print(line_c_2)
print(line_c_3)
print(line_c_4)
