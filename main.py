import matplotlib.pyplot as plt
students_names=["sanjay", "Rahul", "Karan", "Wasim", "Ramesh", "Ajay", "Sartaj", "Priya"]
student_marks=[35,50,20,45,25,40,25,40]
marks_perc = []
for x in student_marks:
    res = (x/50)*100
    marks_perc.append(res)
print(marks_perc)
def line_chart_of_students_and_marks():
    plt.plot(students_names,student_marks)
    plt.title("Students Marks Graph")
    plt.xlabel("Students Names")
    plt.ylabel("Students Marks")
    plt.show()
line_chart_of_students_and_marks()
def percentage_bar_chart():
    plt.bar(students_names,student_marks)
    plt.title("Students Percentage Graph")
    plt.xlabel("Students Names")
    plt.ylabel("Students Percentage")
    plt.show()
percentage_bar_chart()