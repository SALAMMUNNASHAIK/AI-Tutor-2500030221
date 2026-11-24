n=int(input("Enter the number of entries: "))
student={}
for i in range(n):
    key=input("Enter Key ")
    value=int(input("Enter Value "))
    student[key]=value
    print(student)