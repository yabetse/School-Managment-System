import psycopg2
import StringIO


class Connection:
    def __init__(self, username, password, database='school_mgt_system', host='localhost'):
        self.__database = database
        self.__dbUsername = username
        self.__dbPassword = password
        self.host = host
        self.__conn = None
        self.is_connected = False  # connection flag

    def __build_connection_string(self):
        concat = StringIO.StringIO()
        concat.write('host=')
        concat.write(self.host)
        concat.write(' ')
        concat.write('dbname=')
        concat.write(self.__database)
        concat.write(' ')
        concat.write('user=')
        concat.write(self.__dbUsername)
        concat.write(' ')
        concat.write('password=')
        concat.write(self.__dbPassword)

        return concat.getvalue()

    def connect(self):
        connection_string = self.__build_connection_string()
        print(connection_string)
        try:
            self.__conn = psycopg2.connect(connection_string)
            self.is_connected = True
            print('Connected to the database %s' % self.__database)
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

        return self.__conn

    def close_connection(self):
        if self.is_connected is True:
            self.__conn.close()
            print('Connection closed')


if __name__ == '__main__':
    con = Connection('postgres', 'root')
    con.connect()
    con.close_connection()