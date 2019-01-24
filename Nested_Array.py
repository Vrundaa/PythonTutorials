students=["","","","",""]

students[0]=list(raw_input("Enter student full name, age and class: ").split(','))
students[1]=list(raw_input("Enter student full name, age and class: ").split(','))
students[2]=list(raw_input("Enter student full name, age and class: ").split(','))
students[3]=list(raw_input("Enter student full name, age and class: ").split(','))
students[4]=list(raw_input("Enter student full name, age and class: ").split(','))
print "Total students : "+ str(len(students))

print "Students First names in sorted order : "
student_sorted=["","","","",""]
student_sorted[0]=(students[0][0].split(' '))[0]
student_sorted[1]=(students[1][0].split(' '))[0]
student_sorted[2]=(students[2][0].split(' '))[0]
student_sorted[3]=(students[3][0].split(' '))[0]
student_sorted[4]=(students[4][0].split(' '))[0]
student_sorted.sort()
print student_sorted

print "Students Last names in reverse order : "
student_reverse=["","","","",""]
student_reverse[0]=(students[0][0].split(' '))[1]
student_reverse[1]=(students[1][0].split(' '))[1]
student_reverse[2]=(students[2][0].split(' '))[1]
student_reverse[3]=(students[3][0].split(' '))[1]
student_reverse[4]=(students[4][0].split(' '))[1]
student_reverse.reverse()
print student_reverse


marks=int(students[0][1])+int(students[1][1])+int(students[2][1])+int(students[3][1])+int(students[4][1])
print "Sum of age of students: "+ str(marks)