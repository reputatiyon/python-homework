python taklif
جلسه 1
weight=float(input("yoyr weight in kg: "))
height=float(input("your height in m: "))
bmi=weight/(height**2)
print("your bmi is", bmi)
تمرین2

n=int(input("how many numbers do we have? "))
sum=0
for i in range(n):
    num=float(input("enter the number: "))
    sum+=num
average=sum/n
print("average", average)
تمرین 3
days=[]
lessons=[]
for i in range(7):
    day=input("روز هفته: ")
    days.append(day)
    lesson=input("درس: ")
    lessons.append(lesson)

print("\nبرنامه درسی دانشجو: ")
for i in range(7):
    print(days[i],":",lessons[i])
تمرین 4
cars=[]
n=int(input("ظرفیت پارکینگ: "))
for i in range(n):
    plate=input("پلاک ماشین : ")
    if plate in cars:
        print("پلاک تکراری")
    else:
        cars.append(plate)

print("\n cars in parking: ")
for car in cars:
    print(car)        
تمرین5
parking={}
number=int(input("ظرفیت پارکینگ: "))
while i < number:
    plate=input("پلاک ماشین: ")
    if plate in parking :
        print("پلاک تکراری")
    else:
        time=input("زمان ورود: ")
        parking[plate] = time
        print("ماشین ثبت شد.")
        i+=1
        
print("\nparking list:")
for plate,time in parking.items():
    print("plate:", plate , "entering time", time)
تمرین 6
contacts = []


def add_contact():
    contact = {}

    contact["name"] = input("Name: ")
    contact["family"] = input("Family: ")
    contact["number"] = input("Number: ")
    contact["description"] = input("Description: ")

    contacts.append(contact)

    print("Contact added successfully.")
تمرین 7
courses = []


def add_course():
    global courses

    code = input("Course Code: ")
    title = input("Course Title: ")
    professor = input("Professor: ")
    unit = int(input("Units: "))

    # بررسی تکراری بودن عنوان درس
    for course in courses:
        if course["title"] == title:
            print("This course already exists.")
            return

    # محاسبه مجموع واحدها
    total = 0
    for course in courses:
        total += course["unit"]

    if total + unit > 17:
        print("You cannot choose more than 17 units.")
        return

    course = {
        "code": code,
        "title": title,
        "professor": professor,
        "unit": unit
    }

    courses.append(course)
    print("Course added successfully.")


def show_list():
    if len(courses) == 0:
        print("No courses.")
    else:
        for course in courses:
            print("------------------------")
            print("Code:", course["code"])
            print("Title:", course["title"])
            print("Professor:", course["professor"])
            print("Unit:", course["unit"])


def search_professor():
    name = input("Professor Name: ")

    found = False

    for course in courses:
        if course["professor"] == name:
            print("------------------------")
            print("Code:", course["code"])
            print("Title:", course["title"])
            print("Unit:", course["unit"])
            found = True

    if not found:
        print("Course not found.")


def save_file():
    file = open("courses.txt", "w")

    for course in courses:
        file.write(
            course["code"] + "," +
            course["title"] + "," +
            course["professor"] + "," +
            str(course["unit"]) + "\n"
        )

    file.close()


while True:

    print("\n1. Add Course")
    print("2. Show List")
    print("3. Search by Professor")
    print("4. Exit")

    choice = input("Choose: ")

    if choice == "1":
        add_course()

    elif choice == "2":
        show_list()

    elif choice == "3":
        search_professor()

    elif choice == "4":
        save_file()
        print("Information saved.")
        break

    else:
        print("Invalid Choice")
تمرین 8
from tkinter import *

contacts = []

# ---------------- Functions ----------------

def add_contact():
    contact = {
        "name": name_entry.get(),
        "family": family_entry.get(),
        "number": number_entry.get(),
        "description": description_entry.get()
    }

    contacts.append(contact)

    result.delete(1.0, END)
    result.insert(END, "Contact Added Successfully")

    name_entry.delete(0, END)
    family_entry.delete(0, END)
    number_entry.delete(0, END)
    description_entry.delete(0, END)


def find_family():
    family = family_entry.get()

    result.delete(1.0, END)

    found = False

    for contact in contacts:
        if contact["family"] == family:
            result.insert(END,
                          f'Name: {contact["name"]}\n'
                          f'Family: {contact["family"]}\n'
                          f'Number: {contact["number"]}\n'
                          f'Description: {contact["description"]}\n\n')
            found = True

    if not found:
        result.insert(END, "Contact Not Found")


def find_number():
    number = number_entry.get()

    result.delete(1.0, END)

    found = False

    for contact in contacts:
        if contact["number"] == number:
            result.insert(END,
                          f'Name: {contact["name"]}\n'
                          f'Family: {contact["family"]}\n'
                          f'Number: {contact["number"]}\n'
                          f'Description: {contact["description"]}\n\n')
            found = True

    if not found:
        result.insert(END, "Contact Not Found")


def show_list():
    result.delete(1.0, END)

    if len(contacts) == 0:
        result.insert(END, "Phone Book is Empty")
    else:
        for contact in contacts:
            result.insert(END,
                          f'Name: {contact["name"]}\n'
                          f'Family: {contact["family"]}\n'
                          f'Number: {contact["number"]}\n'
                          f'Description: {contact["description"]}\n')
            result.insert(END, "---------------------------\n")


# ---------------- GUI ----------------

window = Tk()
window.title("Phone Book")
window.geometry("500x500")

Label(window, text="Name").pack()
name_entry = Entry(window)
name_entry.pack()

Label(window, text="Family").pack()
family_entry = Entry(window)
family_entry.pack()

Label(window, text="Number").pack()
number_entry = Entry(window)
number_entry.pack()

Label(window, text="Description").pack()
description_entry = Entry(window)
description_entry.pack()

Button(window, text="Add Contact", command=add_contact).pack(pady=5)

Button(window, text="Find by Family", command=find_family).pack(pady=5)

Button(window, text="Find by Number", command=find_number).pack(pady=5)

Button(window, text="Show List", command=show_list).pack(pady=5)

result = Text(window, width=55, height=12)
result.pack()

window.mainloop()