#!usr\bin\env python 3

length_list = []

while len(length_list) < 3:
    try:
        length = int(input(f"Enter the length N{len(length_list) + 1}: "))
        length_list.append(length)
    except ValueError:
        print("You can enter only integers.")
        length = int(input(f"Enter the length N{len(length_list) + 1}: "))
        length_list.append(length)


def construct_triangle(*list):
    if list[0] <= list[1] + list[2]  and list[1] <= list[0] + list[2] and list[2] <= list[0] + list[1]:
        return True
    else:
        return False


construct_triangle(*length_list)
