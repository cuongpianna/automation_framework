from db.mssql import SqlServer


class DatabaseBuilder:
    DATABASE_TYPE = {
        'default': SqlServer,
        'sql_server': SqlServer,
    }

    def __init__(self, config, options='default'):
        self.connection = self.DATABASE_TYPE[options](config)

    def execute_store(self, store_name, para, json=True):
        return self.connection.execute_store(store_name, para, json)

    def query(self, query, json=True):
        return self.connection.query(query, json)
