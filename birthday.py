import openpyxl
import datetime
from tkinter import Tk, Label, Button
import sys

def read_excel_data(file_path):
    wb = openpyxl.load_workbook(file_path)
    sheet = wb.active
    birthdays = {}
    for row in sheet.iter_rows(values_only=True):
        name = row[0]
        dob = row[1]
        birthdays[name] = dob.strftime("%d-%m")
    return birthdays

def check_birthdays(birthdays):
    today = datetime.datetime.now().strftime("%d-%m")
    birthday_list = []
    for name, dob in birthdays.items():
        if dob == today:
            birthday_list.append(name)
    return birthday_list

def show_message(birthday_list):
    message = "Today's birthdays are:\n"
    for name in birthday_list:
        message += name + "\n"
    label = Label(text=message)
    label.pack()
    button = Button(text="OK", command=exit)
    button.pack()

file_path = sys.argv[1]
birthdays = read_excel_data(file_path)
birthday_list = check_birthdays(birthdays)

root = Tk()
show_message(birthday_list)
root.mainloop()
