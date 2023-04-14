from datetime import datetime
from car import Car

class car_factory:
    def __init__(self, current_date, last_service_date, current_mileage, last_service_mileage):
        self.last_service_date = last_service_date
        self.last_service_mileage = last_service_mileage
        self.current_mileage = current_mileage
        self.current_date = current_date

    def create_calliope(self, current_date, last_service_date, current_mileage, last_service_mileage):
        self.current_date = datetime.today()
        self.last_service_date = datetime.today()
        self.current_mileage = 0
        self.last_service_mileage = 0

    def create_glisssade(self, current_date, last_service_date, current_mileage, last_service_mileage):
        self.current_date = datetime.today()
        self.last_service_date = datetime.today()
        self.current_mileage = 0
        self.last_service_mileage = 0

    def create_rorschach(self, current_date, last_service_date, current_mileage, last_service_mileage):
        self.current_date = datetime.today()
        self.last_service_date = datetime.today()
        self.current_mileage = 0
        self.last_service_mileage = 0

    def create_thovex(self, current_date, last_service_date, current_mileage, last_service_mileage):
        self.current_date = datetime.today()
        self.last_service_date = datetime.today()
        self.current_mileage = 0
        self.last_service_mileage = 0
