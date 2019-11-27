faculty_file = open("C:\\Users\\Enes\\Desktop\\intro-to-python\\Uygulamalar\\3.2 Uygulama\\faculty-codes.txt", "r")
faculties = faculty_file.readlines()
faculty_file.close()

numbers_file = open("C:\\Users\\Enes\\Desktop\\intro-to-python\\Uygulamalar\\3.2 Uygulama\\school-numbers.txt", "r")
numbers = numbers_file.readlines()
numbers_file.close()

faculty_dict = {}

for faculty in faculties:
    faculty_dict[faculty.split(",")[1][:-1]] = faculty.split(",")[0]

msg = input("Enter your faculty: ")

code = faculty_dict[msg]

for num in numbers:
    if num[:3] == code:
        print(num[:-1])
        
# ----

msg = input("Enter your year: ")

for num in numbers:
    if num[3:5] == msg:
        print(num[:-1])
