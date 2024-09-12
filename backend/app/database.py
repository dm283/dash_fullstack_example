import sys, os, configparser, pyodbc
from pathlib import Path
from abc import ABC, abstractmethod


BASE_DIR = Path(__file__).resolve().parent.parent

config = configparser.ConfigParser()
config_file = BASE_DIR / 'config.ini'
if os.path.exists(config_file):
    config.read(config_file, encoding='utf-8')
else:
    print("error! config file doesn't exist"); sys.exit()


DB_CONNECTION_STRING = config['db']['db_connection_string']


class Database(ABC):
    """
    Database context manager
    """

    def __init__(self, driver) -> None:
        self.driver = driver

    @abstractmethod
    def connect_to_database(self):
        raise NotImplementedError()
    
    def __enter__(self):
        self.connection = self.connect_to_database()
        self.cursor = self.connection.cursor()
        return self
    
    def __exit__(self, exception_type, exc_val, traceback):
        self.cursor.close()
        self.connection.close()


class DBConnect(Database):
    """PyODBC Database context manager"""

    def __init__(self) -> None:
        self.driver = pyodbc
        super().__init__(self.driver)

    def connect_to_database(self):
        return self.driver.connect(DB_CONNECTION_STRING)


DB_NAME = 'Luding'
DB_SCHEMA = 'dbo'


select = {}

select['product_quantity'] = f"""
  SELECT count(*) product_quantity FROM {DB_NAME}.{DB_SCHEMA}.tovar_sklad
"""

select['dt_quantity'] = f"""
  SELECT count(*) dt_quantity FROM (SELECT id_doc FROM {DB_NAME}.{DB_SCHEMA}.tovar_sklad GROUP BY id_doc) AS a
"""

select['tnved_quantity'] = f"""
            select * from (
            SELECT TOP 7 * FROM
                (SELECT LEFT(g33_in,4) g33, count(*) cnt
                FROM {DB_NAME}.{DB_SCHEMA}.tovar_sklad  WHERE 1=1
                GROUP BY LEFT(g33_in,4)) AS a
                ORDER BY 2 DESC) b
                order by cnt desc
        """

select['products_on_storage'] = f"""
  SELECT id,gtdnum,name, cast(date_in as date) date_in, g32,g31,g33_in,g31_2,
  CASE WHEN g41a <>'166' THEN g31_3 ELSE 0 END g31_3,
  CASE WHEN g41a <>'166' THEN g31_3a ELSE '' END g31_3a,
  g35,g41a, cast(date_chk as date) date_chk, country 
  FROM {DB_NAME}.{DB_SCHEMA}.TOVAR_SKLAD 
  ORDER BY date_in ASC,gtdnum,g32
"""


def select_widget_data(select_name):
    #
    with DBConnect() as db:
        query = select[select_name]
        db.cursor.execute(query)

        # print('description =', db.cursor.description)
        dataset_columns_info = [ (i[0], i[1]) for i in db.cursor.description ]
        # print('dataset_columns_info =', dataset_columns_info)


        dataset = db.cursor.fetchall()
        #print('dataset =', dataset) #

        objects = []
        for data in dataset:

            item = {}
            for i in range(len(dataset_columns_info)):
                item[dataset_columns_info[i][0]] = data[i]
            
            objects.append(item)

        # objects = [
        #     {   
        #         "g33": data[0],
        #         "cnt": data[1],
        #     }
        #     for data in dataset
        # ]

        # print('obj_list =', obj_list)
        # print('objects =', objects)
        
    return objects    


def select_dashboard_data():
    # with DBConnect() as db:
    #     query = """
    #         select * from (
    #         SELECT TOP 7 * FROM
    #             (SELECT LEFT(g33_in,4) g33, count(*) cnt
    #             FROM Luding.dbo.tovar_sklad  WHERE 1=1
    #             GROUP BY LEFT(g33_in,4)) AS a
    #             ORDER BY 2 DESC) b
    #             order by cnt
    #     """
    #     db.cursor.execute(query)
    #     objects = [
    #         {   
    #             "g33": data[0],
    #             "cnt": data[1],
    #         }
    #         for data in db.cursor.fetchall()
    #     ]
    objects = {}
    for s in select:
        # objects = {'tnved_quantity': select_widget_data('tnved_quantity')}
        objects[s] = select_widget_data(s)
        
    return objects
