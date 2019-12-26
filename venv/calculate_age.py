import datetime

# Print headers:
print("---------------------------------------------------")
print("Age Calulcator veriosn 2.0")
print("---------------------------------------------------")

while True:
    try:
        # Get the user's birthday
        myDay = input("Please enter the Day you were born: ")
        myMonth = input("Please enter the Month you were born: ")
        myYear = input("Please enter the Year you were born: ")

        print("Your birthday is on " + str(myDay) + "-" + str(myMonth) + "-" + str(myYear))

        # Calculating the user's age
        myBirthday = datetime.date(int(myYear), int(myMonth), int(myDay))
        today = datetime.date.today()
        dayDiff = (today - myBirthday)

        # Print the user's age
        print("Your age is " + str(int(dayDiff.days / 365.25)) + " Years")
        break;
    except:
        print("\nSorry, there is an error in your input!!")