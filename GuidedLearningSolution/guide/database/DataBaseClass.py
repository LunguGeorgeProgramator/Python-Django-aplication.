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
                                 id int NOT NULL,
                                 step_content varchar(255) NOT NULL,
                                 step_selector varchar(255) NOT NULL,
                                 step_next int NOT NULL,
                                 id_guide int NOT NULL,
                                 PRIMARY KEY (ID_steps),
                                 FOREIGN KEY (id_guide) REFERENCES {table_results}(ID_guide)
                                );"""

    create_test_data_for_tables = {
        table_steps: [
            {1: "", "test text 1": "", ".class-1": "",  2: "", "1": ""},
            {"2": "", "test text 2": "", ".class-2": "",  3: "", "1": ""},
            {"3": "", "test text 3": "", "#id1": "",  4: "", "1": ""},
            {"4": "", "test text 4": "", "#id2": "",  5: "", "1": ""},
            {"5": "", "test text 5": "", ".class-3": "",  6: "", "1": ""}
        ],
        table_results: [
            {"Guide_1": ""},
            {"Guide_2": ""},
            {"Guide_3": ""},
            {"Guide_4": ""},
            {"Guide_5": ""}
        ]
    }

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
                print(table_to_check)
                check_table = cursor.execute(f"SHOW TABLES LIKE '%{table_to_check}%';")
                if check_table:
                    continue
                cursor.execute(sql_create)
                for result_to_put in self.create_test_data_for_tables.get(table_to_check, []):
                    # print(result_to_put)
                    # print('========')
                    if self.table_results == table_to_check:
                        self.insert_new_guides(*result_to_put)
                    else:
                        self.insert_new_guide_step(*result_to_put)

            return cursor, db
        except Error as e:
            raise BaseException("SQL error ", e)

    def connect_data_base(self):
        try:
            try:
                db = MySQLdb.connect(host=self.host_mysql, user=self.user_mysql, passwd=self.pass_mysql, database=self.data_base_name)

                # cursor = db.cursor()
                # cursor.execute(f'DROP DATABASE {self.data_base_name};')
                # return cursor, db

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

    def insert_new_guide_step(self, id_steps, step_content, step_selector, step_next, id_guide):
        cursor, db = self.connect_data_base()
        cursor.execute(f"""INSERT INTO {self.table_steps} 
                            SET 
                            id={id_steps},
                            step_content='{step_content}',
                            step_selector='{step_selector}',
                            step_next={step_next},
                            id_guide={id_guide};
                        """)
        db.commit()

    def update_guide_step(self, id_steps, step_content, step_selector, step_next, id_step):
        cursor, db = self.connect_data_base()
        cursor.execute(f"""UPDATE {self.table_steps} 
                            SET 
                            id={id_steps},
                            step_content='{step_content}',
                            step_selector='{step_selector}',
                            step_next={step_next}
                            WHERE ID_steps = {id_step};
                        """)
        db.commit()

    def remove_guid_step(self, id):
        cursor, db = self.connect_data_base()
        cursor.execute(f"DELETE FROM {self.table_steps} WHERE ID_steps={id}")
        db.commit()


if __name__ == '__main__':
    p1 = DataBase()
    # print(p1.get_results_guide_steps(1))
    # p1.insert_new_guides("Guide_10")
    print(p1.get_results_guides())
    # print(p1.get_results_guides(18))
    # print(p1.get_results_guide_steps(18))
    # p1.update_guide_step(1, "test text 1", ".class-1", 2, 1)
    # print(p1.get_results_guide_steps(1))
