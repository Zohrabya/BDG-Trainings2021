  #!/usr/bin/env python3

month = input("Enter a month: ").lower()
month_days = {
            "january": 31, 
            "february": 28,
            "march": 31,
            "april": 30,
            "may": 31,
            "june": 30,
            "july": 31,
            "august": 31,
            "september": 30,
            "october": 31,
            "november": 30,
            "december": 31
}

if month not in month_days:
    exit("Wrong input")

try:
    year = int(input("Enter a year"))
except ValueError:
    print("You can enter only integers. Try again")
    year = int(input("Enter a year"))


def month_days_output(m, y):            
    if y % 4 == 0:
        month_days["february"] = 29
    
    return month_days[m]


print(month_days_output(month, year))
