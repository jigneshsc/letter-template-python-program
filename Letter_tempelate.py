
letter = '''hii <name> Congratulattions to join Namaste Bharat AJ
you are so intelligent as you tell us your age is <age>
you joined on <date>
your father name is <fname>
Thanking You From NBAJ'''
name = input("Enter Your name: ")
age = input("enter your age: ")
date = input ("enter today date: ")
fname = input("enter your father name: ")
letter = letter.replace("<name>", name)
letter = letter.replace("<age>", age)
letter = letter.replace("<date>", date)
letter = letter.replace("<fname>", fname)
print (letter)