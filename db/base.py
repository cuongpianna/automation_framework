import abc


class IDatabase(metaclass=abc.ABCMeta):
    def __init__(self, config):
        """
        Init database interface for all database type classes
        :param config: Data Source=192.168.38.34;User ID=sa;Password=123456;Database=AutoCMS_V2
        """
        try:
            arr = config.split(';')
            self.server = None
            self.user = None
            self.password = None
            self.database = None
            for item in arr:
                arr1 = item.split('=')
                if len(arr1) > 2:
                    # logging.exception('error config: ' + conf)
                    return
                if arr1[0].lower() == 'Data Source'.lower():
                    self.server = arr1[1]
                elif arr1[0].lower() == 'User ID'.lower():
                    self.user = arr1[1]
                elif arr1[0].lower() == 'Password'.lower():
                    self.password = arr1[1]
                elif arr1[0].lower() == 'Database'.lower():
                    self.database = arr1[1]
        except Exception:
            pass

    @abc.abstractmethod
    def execute_store(self, store_name, params, json=True):
        pass
