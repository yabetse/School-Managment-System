import psycopg2
from Person import Person


class StudentDB:
    def __init__(self, connection):
        self.connection = connection
        self.__cursor = connection.cursor()
        self.context = "school.student"

    def put(self,
                first_name,
                last_name,
                gender,
                email,
                phone_number,
                date_of_birth,
                id, grade,
                section):
        try:
            print('creating student')
            self.__cursor.callproc('insert_into_student',
                                   [first_name,
                                    last_name,
                                    gender,
                                    email,
                                    phone_number,
                                    date_of_birth,
                                    id, grade,
                                    section])

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            # close the cursor
            if self.connection:
                self.__cursor.close()
                print("cursor closed")

    def get(self, grade="all", section="all", showid=False):
        try:
            self.__cursor.callproc('select_all_students', [grade, section])
            result = self.__cursor.fetchall()

            print("Fetched Data")

            for row in result:
                if showid is True:
                    print(" %s %s --  %d" % row[0], row[1], row[2], row[6])

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            # close the cursor
            if self.connection:
                self.__cursor.close()
                print("cursor closed")

    def delete(self, id, delete_all=False):
        try:
            self.__cursor.callproc('delete_student', [id, delete_all])
            if delete_all is True:
                print("Deleted all Students")
            else:
                print("Deleted student with id %s" % id)

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            # close the cursor
            if self.connection:
                self.__cursor.close()
                print("cursor closed")

    def change_name(self, id, value, first=True):
        try:
            self.__cursor.callproc('alterName', [id, value, first])
            print('Changed name')
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            # close the cursor
            if self.connection:
                self.__cursor.close()
                print("cursor closed")

    def change_grade(self, id, grade):
        try:
            self.__cursor.callproc('alterGrade', [id, grade])
            print('Changed grade')
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            # close the cursor
            if self.connection:
                self.__cursor.close()
                print("cursor closed")

    def change_section(self, id, section):
        try:
            self.__cursor.callproc('alterSection', section)
            print('Changed seciton')
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            # close the cursor
            if self.connection:
                self.__cursor.close()
                print("cursor closed")

    def change_phone_number(self, id, phone_number):
        try:
            self.__cursor.callproc('alterPhone', phone_number)
            print('Changed phone number')
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            # close the cursor
            if self.connection:
                self.__cursor.close()
                print("cursor closed")

    def change_email(self, id, email):
        try:
            self.__cursor.callproc('alterEmail', email)
            print('Changed email')
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            # close the cursor
            if self.connection:
                self.__cursor.close()
                print("cursor closed")


class Student(Person):
    def __init__(self):
        super(Student, self).__init__()
        self.__id = 0
        self.grade = None
        self.section = None

    def get_full_name(self):
        super(Student, self).get_full_name()

    def get_gender(self):
        super(Student, self).get_gender()

    def get_email(self):
        super(Student, self).get_email()

    def get_phone_number(self):
        super(Student, self).get_phone_number()

    def get_dateOfBirth(self):
        super(Student, self).get_dateOfBirth()

    def set_gender(self, gender):
        super(Student, self).set_gender(gender)

    def set_email(self, email):
        super(Student, self).set_email(email)

    def set_phone_number(self, phone_no):
        super(Student, self).set_phone_number(phone_no)

    def set_dateOfBirth(self, date_of_birth):
        super(Student, self).set_phone_number(date_of_birth)

    def get_id(self):
        return self.__id

    def get_grade(self):
        return self.grade

    def get_section(self):
        return self.section

    def set_grade(self, grade):
        if grade > 12 or grade < 1:
            print("Invalid value for grade")
        else:
            self.grade = grade

    def set_section(self, section):
        self.section = section

