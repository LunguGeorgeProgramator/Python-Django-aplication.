import MySQLdb
from MySQLdb import Error


class DataBase:

    host_mysql = "127.0.0.1"
    user_mysql = "root"
    pass_mysql = "secret"
    data_base_name = "GuideDataBase"
    table_results = "guideRows"
    table_steps = "guideSteps"
    # create tables queries
    SQL_create_guide_results = f"""CREATE TABLE {table_results} (
                                   ID_guide int NOT NULL AUTO_INCREMENT,
                                   name_guide varchar(255) NOT NULL,
                                   PRIMARY KEY (ID_guide)
                                );"""
    SQL_create_guide_steps = f"""CREATE TABLE {table_steps} (
                                 ID_steps int NOT NULL AUTO_INCREMENT,
                                 step_content varchar(255) NOT NULL,
                                 step_selector varchar(255) NOT NULL,
                                 step_next int NOT NULL,
                                 id_guide int NOT NULL,
                                 PRIMARY KEY (ID_steps),
                                 FOREIGN KEY (id_guide) REFERENCES {table_results}(ID_guide)
                                );"""

    def create_missing_data_base(self):
        db = MySQLdb.connect(host=self.host_mysql, user=self.user_mysql, passwd=self.pass_mysql)
        cursor = db.cursor()
        try:
            check_data_base = cursor.execute(f"SHOW DATABASES LIKE '{self.data_base_name}';")
            if not check_data_base:
                cursor.execute(f"CREATE DATABASE {self.data_base_name};")
            cursor.close()
            db = MySQLdb.connect(host=self.host_mysql, user=self.user_mysql, passwd=self.pass_mysql,  database=self.data_base_name)
            cursor = db.cursor()
            for table_to_check, sql_create in [(self.table_results, self.SQL_create_guide_results), (self.table_steps, self.SQL_create_guide_steps)]:
                check_table = cursor.execute(f"SHOW TABLES LIKE '%{table_to_check}%';")
                if check_table:
                    continue
                cursor.execute(sql_create)
            return cursor, db
        except Error as e:
            raise BaseException("SQL error ", e)

    def connect_data_base(self):
        try:
            try:
                #
                # db = MySQLdb.connect(host=self.host_mysql, user=self.user_mysql, passwd=self.pass_mysql,
                #                 database=self.data_base_name)
                # cursor = db.cursor()
                # cursor.execute(f'DROP DATABASE {self.data_base_name};')
                # return cursor, db
                db = MySQLdb.connect(host=self.host_mysql, user=self.user_mysql, passwd=self.pass_mysql, database=self.data_base_name)
                return db.cursor(), db
            except Error:
                # if the database dose not exist connect and create a new one and a new table
                return self.create_missing_data_base()
        except Error as e:
            print("Error while connecting to MySQL", e)

    def get_results_guides(self, id_row=None):
        cursor, _ = self.connect_data_base()
        set_condition = f" WHERE ID_guide={id_row} " if id_row else ""
        cursor.execute(f"select * from guideRows {set_condition};")
        return cursor.fetchall()

    def insert_new_guides(self, new_name):
        cursor, db = self.connect_data_base()
        cursor.execute(f"INSERT INTO guideRows SET name_guide='{new_name}'")
        db.commit()

    def update_new_guides(self, new_name):
        cursor, db = self.connect_data_base()
        cursor.execute(f"INSERT INTO guideRows SET name_guide='{new_name}'")
        db.commit()

    def remove_guide(self, id):
        cursor, db = self.connect_data_base()
        cursor.execute(f"DELETE FROM guideRows WHERE ID_guide={id}")
        db.commit()

    def get_results_guide_steps(self, id_guide, id_row=None):
        cursor, _ = self.connect_data_base()
        set_condition = f" AND ID_steps={id_row} " if id_row else ""
        cursor.execute(f"select * from {self.table_steps} WHERE ID_guide = {id_guide} {set_condition};")
        return cursor.fetchall()


p1 = DataBase()
# p1.insert_new_guides("Guide_3")
# p1.insert_new_guides("Guide_4")
# p1.insert_new_guides("Guide_5")
# p1.insert_new_guides("Guide_6")
# p1.insert_new_guides("Guide_7")
# p1.insert_new_guides("Guide_8")
# p1.insert_new_guides("Guide_9")
# p1.insert_new_guides("Guide_10")
# print(p1.get_results_guides())
# print(p1.get_results_guides(18))

for row in p1.get_results_guides():
    print(row[0])
    print(row[1])


