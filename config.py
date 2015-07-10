import os

FILE_FORMAT = "db-%s.sql"

ZIP_STATUS = True

CURRENT_DIRECTORY = os.path.dirname(os.path.abspath(__file__))

# MySql configurations
RDB_HOST = "localhost"
RDB_PORT = 3306
RDB_USER = "test"
RDB_PASSWORD = "test"
RDB_DEFAULT_DB = "test_db"
RDB_IGNORE = ["information_schema", "performance_schema", "mysql"]

RDB_LIST_LOAD_FROM_DB = True
RDB_LIST_SOURCE_FILE = os.path.join(CURRENT_DIRECTORY, "db_list.txt")
RDB_DESTINATION_DIRECTORY = os.path.join(CURRENT_DIRECTORY, "backup", "rdb")
