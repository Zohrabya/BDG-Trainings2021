#!/usr/bin/env python3

with open("C:\\Users\\37494\\Desktop\\QA\\Automation\\BDG_Trainings\\BDG-Trainings2021\\ani.voskanyan\\repo\\Lesson_7\\exercise_14\\file_14.txt") as f:
    content = f. readlines()

new_list = []

for l in content:
    l = l.replace("\n", "").strip().lower()
    l_list = l.split(" ")
    new_list += l_list

with open("new_file_14.txt", "a") as f:
    for w in new_list:
        w = list(w)
        for s in ["!","?", ".", ","]:
            if s in w:
                w.remove(s)
        f.write("".join(w) + "\n") 
    
with open("new_file_14.txt") as f:    
    new_content = f.readlines()
    my_dict = dict()
    for word in new_content:
        if word in my_dict:
            my_dict[word] += 1
        else:
            my_dict[word] = new_content.count(word)

print(max(my_dict, key = my_dict.get))
