import pickle

# Creating and opening file
fobj = open("student.dat", "wb")
rec = []

# Entering student details
while True:
    rno = int(input("Enter roll no.: "))
    name = input("Enter name: ")
    marks = int(input("Enter marks: "))

    lst = [rno, name, marks]
    rec.append(lst)

    ch = input("Want to enter more records? Y/N: ")

    if ch in "Nn":
        break

# Writing records into file
pickle.dump(rec, fobj)

print("The students details are:", rec)

fobj.close()

# Opening file for reading
fobj = open("student.dat", "rb")
found = 0

try:
    # Reading records
    rec = pickle.load(fobj)

    # Searching student by roll number
    rno = int(input("Enter roll no. whose marks are to be updated: "))

    for i in rec:
        if i[0] == rno:
            sm = int(input("Enter updated marks: "))
            i[2] = sm

            print("The updated record of the student is:", i)
            found = 1
            break

except EOFError:
    pass

fobj.close()

# Checking whether record is found
if found == 0:
    print("No such record found")

else:
    # Saving updated records
    fobj = open("student.dat", "wb")
    pickle.dump(rec, fobj)
    fobj.close()
