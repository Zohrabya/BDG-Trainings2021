#!usr\bin\env python 3

text_input = input("Please enter a text: ").capitalize()
if text_input == "":
    raise ValueError ("Your input is empty.")
text_list = list(text_input)


def correct_text_input(t_list):
    for s in range(len(t_list) - 1):
        if t_list[s] in ["?", "!", "."]:
            n = 1
            while t_list[s + n] == " ":
                n += 1
            else:
                t_list[s + n] = t_list[s + n].upper()
        if t_list[s] == "i" and t_list[s + 1] == " " and t_list[s - 1] == " ":
            t_list[s] = "I"

    return "".join(t_list)


print(correct_text_input(text_list))
