class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return "Ошибка"

    def avg_grades(self):
        summ, count = 0, 0
        if not self.grades:
            return "Нет оценок за курсы"
        else:
            for course in self.grades:
                summ += sum(self.grades[course])
                count += len(self.grades[course])
            return summ / count

    def __str__(self):
        return (f"\nИмя: {self.name}\n"
                f"Фамилия: {self.surname}\n"
                f"Средняя оценка за домашние задания: {self.avg_grades()}\n"
                f"Курсы в процессе изучения: {', '.join(self.courses_in_progress)}\n"
                f"Завершенные курсы: {', '.join(self.finished_courses)}")

    def __le__(self, student):
        return self.avg_grades() <= student.avg_grades()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def avg_grades(self):
        summ, count = 0, 0
        if not self.grades:
            return "Нет оценок за лекции"
        else:
            for course in self.grades:
                summ += sum(self.grades[course])
                count += len(self.grades[course])
            return summ / count

    def __str__(self):
        return (f"\nИмя: {self.name}\n"
                f"Фамилия: {self.surname}\n"
                f"Средняя оценка за лекции {self.avg_grades()}")

    def __ge__(self, lecturer):
        return self.avg_grades() >= lecturer.avg_grades()


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return (f"\nИмя: {self.name}\n"
                f"Фамилия: {self.surname}")

def average_hw(students_list, course):
    summ_hw = 0
    for student in students_list:
        if course in student.grades:
            summ_hw += sum(student.grades[course])
    return summ_hw / len(students_list)

def average_lecture(lecturers_list, course):
    summ_hw = 0
    for student in lecturers_list:
        if course in student.grades:
            summ_hw += sum(student.grades[course])
    return summ_hw / len(lecturers_list)


student_1 = Student('Иван', 'Здоровый', 'м')
student_1.courses_in_progress += ['Python']
student_1.finished_courses += ['Java']

student_2 = Student('Василиса', 'Перова', 'ж')
student_2.courses_in_progress += ['Python', 'Тестирование']
student_2.finished_courses += ['Java']

lecturer_1 = Lecturer('Анастасия', 'Боровицкая')
lecturer_1.courses_attached += ['Python']

lecturer_2 = Lecturer('Андрей', 'Смирнов')
lecturer_2.courses_attached += ['Тестирование']

reviewer_1 = Reviewer('Павел', 'Болотов')
reviewer_1.courses_attached += ['Python', 'Тестирование']

reviewer_2 = Reviewer('Серафима', 'Степанова')
reviewer_2.courses_attached += ['Python']


reviewer_1.rate_hw(student_1, 'Python', 10)
reviewer_1.rate_hw(student_2, 'Тестирование', 8)
reviewer_2.rate_hw(student_1, 'Python', 6)
reviewer_2.rate_hw(student_2, 'Python', 9)

student_1.rate_lecturer(lecturer_1, 'Python', 7)
student_2.rate_lecturer(lecturer_1, 'Python', 4)
student_2.rate_lecturer(lecturer_2,'Тестирование', 6)


print(student_1)
print(student_2)
print(lecturer_1)
print(lecturer_2)
print(reviewer_1)
print(reviewer_2)

print(student_2 <= student_1)
print(lecturer_1 >= lecturer_2)

print()

student_list = [student_1, student_2]
lecturers_list = [lecturer_1, lecturer_2]
print(average_hw(student_list, 'Python'))
print((average_lecture(lecturers_list, 'Python')))
