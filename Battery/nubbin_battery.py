from car import Car
from datetime import datetime
from car_factory import car_factory


class nubbin_battery(Car, car_factory):
    def __init__(self, last_service_date):
        super().__init__(last_service_date)
        self.current_date = None

    def needs_service(self):
        self.last_service_date = car_factory.__init__(last_service_date=datetime.today())
        self.current_date = car_factory.__init__(current_date=datetime.today())
