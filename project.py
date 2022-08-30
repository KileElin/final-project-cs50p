import datetime
import csv
import pyperclip
import sys

def main():
    sms = gen_message(get_info(), get_time(), get_dr(), get_clinic())
    print(sms)
    copy_sms(sms)


# Prompt user for input of both hour and minute of the appointment. 
# If the input is between 8 AM and 9 PM return time in correct format, 
# else return error message and prompt user again.
def get_time():
    hour = input("Hour: ")
    minute = input("Minute: ")
    if 7 < int(hour) < 21 and 0 <= int(minute) < 60:
        return f"{int(hour):02d}:{int(minute):02d}"
    else:
        print("Invalid time")
        get_time()

#create dict of clinics from csv file, return the dict.
def import_clinics():
    #create empty dict to store information about the clinics.
    clinics = {}

    #open and read from csv file with information about the clinics and append info as dictionaries containing two keys per dict, "city" and "address" to clinics list
    with open("clinics.csv") as file:
        reader = csv.DictReader(file)
        for row in reader:
            clinics[row["city"]] = row["address"]
    return clinics

#get user to chose which clinic the appointment is at
def get_clinic():
    clinics = import_clinics()
    clinic = input("Clinic (1 = First Clinic, 2 = Second Clinic, 3 = Third Clinic): ")
    if clinic in clinics:
        return clinics[clinic]
    else:
        exit("Invalid Clinic")


# creates a dict of doctors from csv file, return the dict.
def import_doctors():
    #create empty dict to store information about the doctors
    doctors = {}
    #open and read from csv file of the doctors and create a dict to store the info
    with open("doctors.csv") as file:
        reader = csv.DictReader(file)
        for row in reader:
            doctors[row["abbreviation"]] = row['name']
    return doctors


#get user to chose which doctor the patient has an appointment to, keep prompting until input is valid
def get_dr():
    doctors = import_doctors()
    doctor = input("Which doctor(m = Maria McDoctor, j = John Medicalson, s = Sophie Health): ")
    if doctor in doctors:
        return doctors[doctor]
    else:
        print("Invalid doctor")
        get_dr()

# takes all input from user and generate a day and date string to return
def get_info():
    year = get_year()
    month = get_month()
    if month < datetime.datetime.today().month:
        year = int(year)+1
    name_month = convert_month(month)
    dateday = get_date()
    weekday = get_day(year, month, dateday)
    appointment = f"{weekday} {dateday}. {name_month} {year}"
    return appointment

# Generate message text based on input from user
def gen_message(day, time, doctor, clinic):
    message = f"You have an appointment to see dr. {doctor} \n{day} at {time}\nat the {clinic}.\nCall us on 000-PYTHON or send an email to: post@thepythonclinic.com if you have any questions.\nKind regards\nthe Python Clinic"
    return message

# find weekday using the datetime module based on date provided by user. If user has provided an invalid date inform user with message.
def get_day(y, m, d):
    try:
        weekday = datetime.datetime(y, m, d, 00, 1, 00).strftime('%A')
        return weekday
    except ValueError:
        exit("Invalid date")


# Using the datetime module, find the year we are currently in and return the year
def get_year():
    return datetime.datetime.today().year


# Prompt user for month, as in the number of the month, strip whitespace. Check that the month number is valid, if not reprompt user until input is valid. 
def get_month():
    month = int(input("Month(1-12): ").strip())
    if 0 < month < 13:
        return month
    else:
        print("Invalid input, month must be a number between 1-12")
        get_month()


# Prompt user for day of the appointment, strip whitespace. Check that day number is valid, if not reprompt user until input is valid. 
def get_date():
    day = (int(input("Date (1-31): ").strip()))
    if 0 < day < 32:
        return day
    else:
        print("Invalid input, day must be a number betweeen 1-31")
        get_date()


# The function takes as input the number of the month and returns the name of the month. The functions returns False if the number is not between 1-12.
def convert_month(n):
    months = ["January", "February", "March", "April", "Mai", "June", "Juli", "August", "September", "October", "November", "December"]
    if 0 < n < 13:
        index = n - 1
        return months[index]
    else:
        return False

# Copies the generated text to the clipboard so that it can be pasted into the message to the patient.
def copy_sms(text):
    try:
        input("Do you wish to copy the text? (press enter if yes, ctr+c if no): ")
    except KeyboardInterrupt:
        sys.exit()
    pyperclip.copy(text)


if __name__ == "__main__":
    main()

