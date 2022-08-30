# final-project-cs50p
My final project - cs50p

This is my final project in the "CS50p - Introduction to programming with Python" course. 
It is a program used for generating text messages to patients about their doctor's appointments. 
In my work I send messages like these up to 100 times a day, and we have three clinics at different locations and five different doctors.
The program we use at work, can for whatever reason not handle different locations in the buildt in text message generator, so I figured I'd make a program that can.
To make it easier to change names of doctors and addresses of clinics in the future, I've added this information in separate csv files, rather than hard coding them into the program. 
These are then read into the program into dicts, that are then read from in the relevant functions in the program. 
As we never plan appointments more than one year ahead, the only input needed from the user to generate the date and time, is day, month, hour and minute. 
The weekday is found by using the datetime module. The year is also found using the current year, and checking if the month given in 1-12 by the user, has a lower number than the month we're currently in, the year displayed in the message will be the current year + 1. 
