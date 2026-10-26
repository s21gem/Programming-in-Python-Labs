marks = float(input("Enter marks: "))

if 90 <= marks <= 100:
    print("A+")
elif 85 <= marks < 90:
    print("A")
elif 80 <= marks < 85:
    print("B+")
elif 75 <= marks < 80:
    print("B")
elif 70 <= marks < 75:
    print("C+")
elif 65 <= marks < 70:
    print("C")
elif 60 <= marks < 65:
    print("D+")
elif 50 <= marks < 60:
    print("D")
elif 0 <= marks < 50:
    print("F")
else:
    print("Invalid marks")
