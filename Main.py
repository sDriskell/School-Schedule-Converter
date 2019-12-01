import Utility


def main():
    utility: Utility.Utility = Utility.Utility()
    due_dates = utility.read_list()
    student_names = utility.read_names()

    test_write = utility.write_list()

    print(due_dates)
    print(student_names)


if __name__ == '__main__':
    main()
