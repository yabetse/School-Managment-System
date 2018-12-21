import psycopg2


class PersonDB:
    def __init__(self, connection_cursor):
        self.__connection_cursor = connection_cursor
        self.context = "school.person"


class Person:
    def __init__(self):
        self.first_name = None
        self.last_name = None
        self.gender = None
        self.email = None
        self.phone_number = None
        self.date_of_birth = None

    def get_full_name(self):
        if self.first_name is not None and self.last_name is not None:
            return self.first_name + " " + self.last_name

        return None

    def get_gender(self):
        return self.gender

    def get_email(self):
        return self.email

    def get_phone_number(self):
        return self.phone_number

    def get_dateOfBirth(self):
        return self.date_of_birth

    def set_gender(self, gender):
        if gender is not 'M' or gender is not 'F':
            print("Invalid entry for gender. Gender value should be either 'M' or 'F")
        else:
            self.gender = gender

    def set_email(self, email):
        if ('@' and '.') not in email:
            print("Invalid entry for email. Email should contain '@' and '.'")
        else:
            self.email = email

    def set_phone_number(self, phone_no):
        if not phone_no.isalpha():
            print("Invalid entry for phone number. Phone number should not contain letters")
        else:
            self.phone_number = phone_no

    # TODO: check for the format of date
    def set_dateOfBirth(self, date_of_birth):
        self.date_of_birth = date_of_birth
