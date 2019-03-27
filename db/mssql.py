import datetime
import pymssql

from db.base import IDatabase


class SqlServer(IDatabase):
    def __init__(self, config):
        super(SqlServer, self).__init__(config)
        self.conn = pymssql.connect(self.server, self.user, self.password, self.database)
        self.cursor = self.conn.cursor()

    def query(self, query, json=True):
        self.cursor.execute(query)
        rows = self.cursor.fetchall()
        if json:
            return [dict(
                (self.cursor.description[key][0], value.isoformat() if isinstance(value, datetime.datetime) else value)
                for key, value in enumerate(row)) for row in rows]
        return rows

    def execute_store(self, store_name, para, json=True):
        self.cursor.callproc(store_name, para)
        self.cursor.nextset()
        rows = self.cursor.fetchall()
        self.conn.commit()
        if json:
            return [dict(
                (self.cursor.description[i][0], value.isoformat() if isinstance(value, datetime.datetime) else value)
                for i, value in enumerate(row)) for row in rows]
        return rows
