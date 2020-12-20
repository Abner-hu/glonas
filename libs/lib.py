class StationConfiguration(object):
    pass


class ProductionLine(object):
    def add_connection(self):
        pass

    def add_pid_map(self):
        pass

    def assign_abort_users(self):
        pass

    def assign_pre_sequence(self):
        pass


class Area(object):
    def __init__(self, parent):
        self.parent = parent

    def add_configuration_data(self):
        pass

    def add_connection(self):
        pass

    def add_pid_map(self):
        pass

    def add_test_station(self):
        pass

    def assign_abort_users(self):
        pass

    def assign_pre_sequence(self):
        pass


class Station(object):
    def __init__(self, parent):
        self.parent = parent
    pass
