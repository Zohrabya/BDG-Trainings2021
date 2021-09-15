#!usr/bin/env python3

num_dict = {
            1: "first",
            2: "second",
            3: "third",
            4: "forth",
            5: "fifth",
            6: "sixth",
            7: "seventh",
            8: "eighth",
            9: "ninth",
            10: "tenth",
            11: "eleventh",
            12: "twelfth"
}

#Displaying each integer from 1 to 12 and its ordinal number
for key, value in num_dict.items():
    print(key, value)   

num_input = int(input())


def ordinal_num_output(i):
    try:
        if i in num_dict:
            print(num_dict[i])
        else:
            print(f"{i} is out of range. Please enter integers between 1 and 12 (inclusive).")
    except ValueError:
        print("You can enter only integers.")


ordinal_num_output(num_input)
