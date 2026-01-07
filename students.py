def calculate_grade(avg):
    if 90 <= avg <= 100:
        return "S"
    elif 80 <= avg < 90:
        return "A"
    elif 65 <= avg < 80:
        return "B"
    elif 50 <= avg < 65:
        return "C"
    elif 40 <= avg < 50:
        return "D"
    else:
        return "F"


def main():
    name = input("Enter student name: ")
    department = input("Enter department: ")
    semester = input("Enter semester: ")

    marks = []
    for i in range(1, 4):
        mark = float(input(f"Enter marks for subject {i}: "))
        marks.append(mark)

    average = sum(marks) / len(marks)
    grade = calculate_grade(average)

    print("\n--- Student Report ---")
    print(f"Name       : {name}")
    print(f"Department : {department}")
    print(f"Semester   : {semester}")
    print(f"Average    : {average:.2f}")
    print(f"Grade      : {grade}")


if __name__ == "__main__":
    main()
