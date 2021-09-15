month = int (input ('month (1-12): '))
if month < 13:
    if month == 2:
        year = int (input ('year: '))
        if year % 4 == 0:
            if year % 100 == 0:
                if year % 400 == 0:
                    print ('29')
                else:
                    print ('28')
            else:
                print ('29')
        else:
            print ('28')

    elif month >= 8:
        if month % 2 == 0:
            print ('31')
        else:
            print ('30')

    elif month % 2 == 0:
        print ('30')
    else:
        print ('31')

else:
    print ('Only 1-12 accepted')
