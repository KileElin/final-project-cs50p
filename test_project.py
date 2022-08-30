import project 


def test_gen_message(): 
    assert project.gen_message("Monday 22. February 2022", "10:15" , "Elin Kile", "First Clinic, First Road, First City") == "You have an appointment to see dr. Elin Kile \nMonday 22. February 2022 at 10:15\nat the First Clinic, First Road, First City.\nCall us on 000-PYTHON or send an email to: post@thepythonclinic.com if you have any questions.\nKind regards\nthe Python Clinic"

def test_get_day():
    assert project.get_day(2022, 8, 26) == "Friday"
    assert project.get_day(2016, 2, 25) == "Thursday"
    assert project.get_day(2020, 11, 19) =="Thursday"

def test_convert_month():
    assert project.convert_month(1) == "January"
    assert project.convert_month(2) == "February"
    assert project.convert_month(3) == "March"
    assert project.convert_month(4) == "April"
    assert project.convert_month(5) == "May"
    assert project.convert_month(6) == "June"
    assert project.convert_month(7) == "July"
    assert project.convert_month(8) == "August"
    assert project.convert_month(9) == "September"
    assert project.convert_month(10) == "October"
    assert project.convert_month(11) == "November"
    assert project.convert_month(12) == "December"
    assert project.convert_month(0) == False
    