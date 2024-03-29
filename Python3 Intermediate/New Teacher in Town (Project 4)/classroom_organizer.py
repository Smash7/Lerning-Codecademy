from roster import student_roster
import itertools
# Import modules above this line
class ClassroomOrganizer:
  def __init__(self):
    self.sorted_names = self._sort_alphabetically(student_roster)

  def _sort_alphabetically(self, students):
    names = []
    for student_info in students:
      name = student_info['name']
      names.append(name)
    return sorted(names)

  def get_students_with_subject(self, subject):
    selected_students = []
    for student in student_roster:
      if student['favorite_subject'] == subject:
        selected_students.append((student['name'], subject))
    return selected_students

  def combine_students_in_classroom(self):
    combined_students = itertools.combinations(self.sorted_names, 2)
    return list(combined_students)

  def afterschool_program(self):
    iter = itertools.chain(self.get_students_with_subject('Math'), self.get_students_with_subject('Science'))
    afterschool_students = []
    for i in iter:
      afterschool_students.append(i[0])

    return list(itertools.combinations(afterschool_students, 4))

  def __iter__(self):
    self.index = 0
    return self

  def __next__(self):
    index = self.index
    if index >= len(self.sorted_names) - 1:
      raise StopIteration
    self.index += 1
    return self.sorted_names[index]
