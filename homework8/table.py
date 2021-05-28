import sqlite3
from functools import wraps
from typing import Callable, Dict, Iterable


class TableData:
    """It is a wrapper class for database table that acts as collection object.
    Database should be in sqlite3 format and its tables must have column name
    with unique values.

    :param database_name: A name of database to which instances of class
    will connect
    :type database_name: str
    :param table_name: A name of table which instances of class will query
    :type table_name: str
    """

    def __init__(self, database_name: str, table_name: str) -> None:
        """Constructor method."""
        self.database_name = database_name
        self.table_name = table_name

    def _connection(func) -> Callable:
        """Decorator for methods to connect to database before query
        and disconnect after it.

        :param func: A bound method for decorating
        :type func: func
        :return: decorated bound method
        :rtype: func
        """

        @wraps(func)
        def wrapper(self, *args, **kwargs):
            conn = sqlite3.connect(self.database_name)
            cursor = conn.cursor()
            to_return = func(self, cursor, *args, **kwargs)
            conn.close()
            return to_return

        return wrapper

    @_connection
    def __getitem__(self, cursor, name: str) -> tuple:
        """Returns single data row for name :name: in the table

        :param cursor: A cursor of connection to database
        :type cursor: A database cursor object
        :param name: A value of name column for which method searches data row
        :type name: str
        :return: data row for name in table
        :rtype: tuple
        """
        query = "SELECT * FROM '%s' WHERE name='%s'"
        cursor.execute(query % (self.table_name, name))
        result = cursor.fetchone()
        return result

    @_connection
    def __contains__(self, cursor, name: str) -> bool:
        """Returns if record whith the same name exists in the table.

        :param cursor: A cursor of connection to database
        :type cursor: A database cursor object
        :param name: A value of name column for which method searches data row
        :type name: str
        :return: boolean if the same record exists or not
        :rtype: bool
        """
        query = "SELECT * FROM '%s' WHERE name='%s'"
        cursor.execute(query % (self.table_name, name))
        result = cursor.fetchone()
        return bool(result)

    def __iter__(self) -> Iterable:
        """Iteration method.
        :return: object of instance
        :rtype: iterable
        """
        self.n = 1
        return self

    @_connection
    def __next__(self, cursor) -> Dict:
        """Returns the next item of iterable while it's not StopIteration.

        :param cursor: A cursor of connection to database
        :type cursor: A database cursor object
        :raise StopIteration: Raises when iterator went through all items
        :return: The next item of object, which represented by dict whith
        columns as keys and row values as values
        :rtype: dict
        """
        cursor.execute("SELECT * FROM '%s'" % self.table_name)
        keys = (member[0] for member in cursor.description)

        for _ in range(self.n):
            next_data = cursor.fetchone()

        self.n += 1
        if not next_data:
            self.n = 0
            raise StopIteration

        result = dict(zip(keys, next_data))
        return result

    @_connection
    def __len__(self, cursor) -> int:
        """Gives current amount of rows in the table.

        :param cursor: A cursor of connection to database
        :type cursor: A database cursor object
        :return: Amount of table's rows
        :rtype: int
        """
        query = "SELECT COUNT(*) FROM '%s'"
        length = cursor.execute(query % self.table_name).fetchone()[0]
        return length
