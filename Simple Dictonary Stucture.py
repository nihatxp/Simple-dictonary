users={}
for i in range(3):
    ogrenci_numarasi=input("NO: ")
    name=input('Student Name: ')
    surname=input('Student Surname: ')
    phone=input('Phone Number: ')
    age=input('Student age: ')
    users.update({
        ogrenci_numarasi: {
            'name':name,
            'phone':phone,
            'age':age,
            'surname':surname,
        }
    })
on=input('The student Code of the student you are looking for: ')
student=users[on]
print(f"The name of the student number {on} you are calling is {student['name']}, his age is {student['age']}")
