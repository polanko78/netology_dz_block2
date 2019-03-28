from application import people, salary


if __name__ == '__main__':
    name1, salary1 = people.get_employees()
    salary.calculate_salary(name1, salary1)
