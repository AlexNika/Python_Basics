# Задание-1:
# Реализуйте описаную ниже задачу, используя парадигмы ООП:
# В школе есть Классы(5А, 7Б и т.д.), в которых учатся Ученики.
# У каждого ученика есть два Родителя(мама и папа).
# Также в школе преподают Учителя. Один учитель может преподавать 
# в неограниченном кол-ве классов свой определенный предмет. 
# Т.е. Учитель Иванов может преподавать математику у 5А и 6Б,
# но больше математику не может преподавать никто другой.

# Выбранная и заполненная данными структура должна решать следующие задачи:
# 1. Получить полный список всех классов школы
# 2. Получить список всех учеников в указанном классе
#  (каждый ученик отображается в формате "Фамилия И.О.")
# 3. Получить список всех предметов указанного ученика 
#  (Ученик --> Класс --> Учителя --> Предметы)
# 4. Узнать ФИО родителей указанного ученика
# 5. Получить список всех Учителей, преподающих в указанном классе
from functools import reduce


class Person:
    def __init__(self, first_name, middle_name, last_name):
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name

    def get_full_name(self):
        return self.last_name + ' ' + self.first_name + ' ' + self.middle_name

    def get_short_name(self):
        return self.last_name.title() + ' ' + self.first_name[0].upper() + '.' + self.middle_name[0].upper() + '.'


class Student(Person):
    def __init__(self, first_name, middle_name, last_name, mother_name, father_name, class_name):
        super().__init__(first_name, middle_name, last_name)
        self.mother_name = mother_name
        self.father_name = father_name
        self.class_name = class_name

    def get_class_name(self):
        return self.class_name

    def get_parents(self):
        return self.father_name.get_full_name(), self.mother_name.get_full_name()


class Teacher(Person):
    def __init__(self, first_name, middle_name, last_name, class_name, school_subject):
        super().__init__(first_name, middle_name, last_name)
        self.class_name = class_name
        self.school_subject = school_subject

    def get_school_subject(self):
        return self.school_subject

    def get_class_name(self):
        return self.class_name


letters = 'абв'
numbers = '678'
cl = [n + l for n in numbers for l in letters]

teachers = [Teacher('Клавдий', 'Владимирович', 'Семянин', [cl[0], cl[4], cl[5]] , 'Математика'),
            Teacher('Эммануил', 'Аникитевич', 'Михеев', [cl[0], cl[1], cl[2], cl[4], cl[5]] , 'Физика'),
            Teacher('Владлена', 'Тихоновна', 'Жернакова', [cl[5]] , 'Химия'),
            Teacher('Викентий', 'Георгиевич', 'Энговатов', [cl[0], cl[4], cl[5]], 'История'),
            Teacher('Арсений', 'Еремеевич', 'Корниец', [cl[4], cl[5]], 'Физкультура'),
            Teacher('Анатолий', 'Давидович', 'Артамонов', [cl[0], cl[1], cl[2], cl[3], cl[4], cl[5]], 'География'),
            Teacher('Эмиль', 'Никанорович', 'Пономарёв', [cl[0], cl[1], cl[2], cl[3], cl[4], cl[5]], 'Информатика'),
            Teacher('Владимир', 'Никонович', 'Бурый', [cl[0], cl[1], cl[2]], 'Литература'),
            Teacher('Потап', 'Тарасович', 'Самарин', [cl[3], cl[4], cl[5], cl[6], cl[7], cl[8]], 'НВП'),
            Teacher('Яна', 'Романовна', 'Муратова', [cl[0]], 'Русский язык')]
parents = [Person('Кузьма', 'Моисеевич', 'Шамов'), Person('Анна', 'Ивановна', 'Шамова'),
           Person('Елисей', 'Маркович', 'Казьмин'), Person('Ирина', 'Федоровна', 'Казьмина'),
           Person('Михей', 'Миронович', 'Морин'), Person('Елена', 'Сергеевна', 'Морина'),
           Person('Эмиль', 'Панкратиевич', 'Шихранов'), Person('Юлия', 'Петрона', 'Шихранова'),
           Person('Валерий', 'Измаилович', 'Синицын'), Person('Аглая', 'Валерьевна', 'Синицына')]
students = [Student('Алексей', 'Кузьмич', 'Шамов', parents[1], parents[0], cl[0]),
            Student('Игорь', 'Еличеевич', 'Казьмин', parents[3], parents[2], cl[5]),
            Student('Александр', 'Михеевич', 'Морин', parents[5], parents[4], cl[7]),
            Student('Панкрат', 'Эмильевич', 'Шихранов', parents[7], parents[6], cl[0]),
            Student('Эдуард', 'Валериевич', 'Синицын', parents[9], parents[8], cl[3])]

# Получить полный список всех классов школы
print('Список классов в школе (на основании списка учеников): ')
print(*(sorted(set([val.get_class_name() for val in students]))))
print()
print('Список классов в школе (на основании списка учителей): ')
print(*(sorted(set(reduce(lambda x, y: x + y, list([item.get_class_name() for item in teachers]))))))

# Получить список всех учеников в указанном классе(каждый ученик отображается в формате "Фамилия И.О.")
print()
current_class = '6а'
print(f'Список всех учеников в {current_class} классе:')
print(*[item.get_short_name() for item in students if item.get_class_name() == current_class], sep='\n')

# 3. Получить список всех предметов указанного ученика (Ученик --> Класс --> Учителя --> Предметы)
print()
current_student = students[4]
print(f'Списов всех предметов ученика {current_student.get_short_name()}')
temp_list = [item for item in teachers if current_student.get_class_name() in item.get_class_name()]
teachers_names = [item.get_full_name() for item in temp_list]
subj = [item.get_school_subject() for item in temp_list]
print(current_student.get_full_name() + ' --> ' + 'класс ' + current_student.get_class_name() + '\n'
      + 'Учителя --> ' + '\n' + '\n'.join(map(str, teachers_names)) + '\n' + 'Предметы --> '
      + '\n' + '\n'.join(map(str, subj)))

# 4. Узнать ФИО родителей указанного ученика
print()
print(f'Родители ученика {current_student.get_short_name()}')
student_parents = current_student.get_parents()
print(*student_parents)

# 5. Получить список всех учителей, преподающих в указанном классе
print()
print(f'В {current_class} классе, преподавали следующие учителя')
teach_list = [item.get_full_name() for item in teachers if current_class in item.get_class_name()]
print(*teach_list, sep='\n')
