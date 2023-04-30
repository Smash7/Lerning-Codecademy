from roster import student_roster as roster
from classroom_organizer import ClassroomOrganizer

roster_iter = ClassroomOrganizer()

for student in roster_iter:
    print(student)

print(roster_iter.combine_students_in_classroom())

print(roster_iter.afterschool_program())
