class School():
    def __init__(self, name: str, level: str, numberOfStudents: int):
        self.name = name
        self.level = level
        self.numberOfStudents = numberOfStudents

    def get_name(self):
        return self.name

    def get_level(self):
        return self.level

    def get_number_of_students(self):
        return self.numberOfStudents

    def set_number_of_students(self, numOfStudents):
        self.numberOfStudents = numOfStudents

    def __repr__(self):
       return 'A ' + self.level + 'school named ' + self.name + ' with ' + str(self.numberOfStudents) + ' students'

class PrimarySchool(School):
    def __init__(self, name: str, numberOfStudents: int, pickupPolicy: str,):
        super().__init__(name, "primary", numberOfStudents)
        self.pickupPolicy = pickupPolicy

    def get_pickup_policy(self):
        return self.pickupPolicy

    def __repr__(self):
        parentRepr = super().__repr__()
        return parentRepr + "\nThe pickup policy is {pickupPolicy}".format(pickupPolicy = self.pickupPolicy)

class HighSchool(School):
    def __init__(self, name: str, numberOfStudents: int, sportsTeams=["footbal", "basketball"]):
        super().__init__(name, "high", numberOfStudents)
        self.sportsTeams = sportsTeams

    def get_sports_teams(self):
        return self.sportsTeams

    def __repr__(self):
        parentRepr = super().__repr__()
        return parentRepr + "\nThe sports teams are {sportsTeams}".format(sportsTeams = self.sportsTeams)

# testing
school = School("MySchool", "defailt", 100,)
print(school.get_level())
print(school.get_name())
print(school.get_number_of_students())
print(repr(school))
school.set_number_of_students(200)
print(school.get_number_of_students())

print("--------------------------------")

school = PrimarySchool("MySchool", 100, "strict")
print(school.get_level())
print(school.get_name())
print(school.get_number_of_students())
print(repr(school))
school.set_number_of_students(200)
print(school.get_number_of_students())

print("--------------------------------")

sports = ["badminthon", "tennis"]
school = HighSchool("MySchool", 100, sports)
print(school.get_level())
print(school.get_name())
print(school.get_number_of_students())
print(repr(school))
school.set_number_of_students(200)
print(school.get_number_of_students())
