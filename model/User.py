from clcrypto import password_hash, generate_salt, check_password
from db.connect_workshop_2 import connect_workshop_2


class User:
    __ID_UNSAVED = -1

    def __init__(self):
        self.__id = User.__ID_UNSAVED
        self.__email = None
        self.__username = None
        self.__hashed_password = None

    @property
    def id(self):
        return self.__id

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, new_email):
        self.__email = new_email

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, new_username):
        self.__username = new_username

    def set_password(self, password):
        self.__hashed_password = password_hash(password, generate_salt())

    def is_password_correct(self, candidate):
        return check_password(candidate, self.__hashed_password)

    def save_to_db(self, cursor):
        if self.__id == User.__ID_UNSAVED:
            sql = "INSERT INTO users VALUES(default, %s, %s, %s) RETURNING id;"
            cursor.execute(sql, (self.__email, self.__username, self.__hashed_password))
            self.__id = cursor.fetchone()[0]
            return True
        else:
            # todo update
            raise Exception("Not implemented")


conn = connect_workshop_2()
cur = conn.cursor()

u = User()
u.username = "ala"
u.email = "ala@mairl.pl"
u.set_password("qwe")
u.save_to_db(cur)

cur.close()
conn.close()
