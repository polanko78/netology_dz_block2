import psycopg2

students = (
    {
        'name': 'Михаил Воронин',
        'birth': '1978-10-10',
        'gpa': '4,5'
    },
    {
        'name': 'Александр Пушкин',
        'birth': '1977-02-03',
        'gpa': '4,8'
    },
    {
        'name': 'Иван Иванов',
        'birth': '1979-01-01',
        'gpa': '4,9'
    }
)
counter3 = 0

def create_db():
    with psycopg2.connect(dbname='testbd', user='test', password='12345') as conn:
        with conn.cursor() as cur:
            cur.execute('''
                    create table student (
                    id integer primary key,
                    name varchar(100),
                    gpa numeric(10,2),
                    birth timestamp with time zone
                    )          
            ''')
            cur.execute('''
                    create table course (
                    id integer primary key,
                    name varchar(100)
                    )                    
            ''')
            cur.execute('''
                    create table student_course (
                    id integer primary key,
                    student_id integer references student(id),
                    course_id integer references course(id)
                    )                 
            ''')
            count1 = 0
            for courses in ('Програмирование на Питоне', 'Програмирование на Java', 'UX-дизайнер'):
                count1 += 1
                cur.execute('''
                            insert into course
                            (id, name) values
                            (%s, %s)
                            ''', (count1, courses))
    print('Готово!')


def add_student(student):
    global counter3
    print(type(student['name']), type(student['gpa']), type(student['birth']))
    with psycopg2.connect(dbname='testbd', user='test', password='12345') as conn:
        counter3 += 1
        with conn.cursor() as cur:
            cur.execute('''
                insert into student (id, name, gpa, birth)
                values ($s, $s, $s, %s)
            ''', (counter3, student['name'], student['gpa'], student['birth'], ))


def get_student(student_id):
    with psycopg2.connect(dbname='testbd', user='test', password='12345') as conn:
        with conn.cursor() as cur:
            cur.execute('''
            select $s from student 
            ''', (student_id, ))


def get_students_short():
    with psycopg2.connect(dbname='testbd', user='test', password='12345') as conn:
        with conn.cursor() as cur:
            cur.execute('''
            select student.id, student.name from student 
            ''')
            res = cur.fetchall()
            for item in res:
                print(item)


def get_course_short():
    with psycopg2.connect(dbname='testbd', user='test', password='12345') as conn:
        with conn.cursor() as cur:
            cur.execute('''
            select * from course 
            ''')
            res = cur.fetchall()
            for item in res:
                print(item)


def get_students(course_id):
    # возвращает студентов определенного курса
    with psycopg2.connect(dbname='testbd', user='test', password='12345') as conn:
        with conn.cursor() as cur:
            cur.execute('''
            select student.name, course.name from student_course 
            join student.id = student_course.student.id
            join course.id = student_course.course.id
            where course.id = $s            
            ''', (course_id, ))


def add_students(course_id, students):
    # создает студентов и
    # записывает их на курс
    with psycopg2.connect(dbname='testbd', user='test', password='12345') as conn:
        with conn.cursor() as cur:
            count2 = 0
            for st in students:
                count2 += 1
                cur.execute('''
                    insert into student
                    (id, name, gpa, birth) values
                    ($s, $s, $s, %s)
                ''', (count2, st['name'], st['gpa'], st['birth']))
                cur.execute('''
                            insert into student_course
                            (student_id, course_id) values
                            (%s)
                            ''', (count2, course_id))


def menu():
    while True:
        print('''Меню наше БД:
         1 - Создать БД
         2 - Добавить студента
         3 - Показать студента
         4 - Показать студентов на курсе
         5 - Добавить студентов на курс
         ''')
        com = input()
        if int(com) == 1:
            create_db()
        elif int(com) == 2:
            name = input('Введите имя: ')
            gpa = (input('Средний балл'))
            birth = (input('Дата рождения формата (год-месяц-день): '))
            student = {
                'name': name,
                'gpa': gpa,
                'birth': birth
            }
            add_student(student)
        elif int(com) == 3:
            get_students_short()
            student_id = int(input('Выберете номер студента: '))
            get_student(student_id)
        elif int(com) == 4:
            get_course_short()
            course_id = input('Выберете номер курса: ')
            get_students(course_id)
        elif int(com) == 5:
            get_course_short()
            course_id = input('Выберете номер курса: ')
            print('Студентов добавим из заранее подготовленного словаря.')
            add_students(course_id, students)


if __name__ == '__main__':
    menu()
#    create_db()
#    get_course_short()