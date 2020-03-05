class School:
    def __init__(self):
        self.school_dict = dict()

    def add_student(self, name, grade):
        if self.school_dict.get(grade) == None:
            self.school_dict[grade] = [name]
        else:
            self.school_dict[grade].append(name)

    def roster(self):
        return_list = []
        for key in sorted(self.school_dict):
            self.school_dict[key].sort()
            return_list += self.school_dict[key]
        return return_list

    def grade(self, grade_number):
        if grade_number in self.school_dict.keys():
            self.school_dict[grade_number].sort()
            return self.school_dict[grade_number]
        else:
            return []