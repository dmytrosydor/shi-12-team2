from aircraft import Aircraft

class Flight:
    def __init__(self, airline_name: str, aircraft: Aircraft, flight_number: str):
        self._airline_name = airline_name
        self._aircraft = aircraft
        self.flight_number = flight_number

    def get_flight_info(self):
        return f"Flight Number: {self.flight_number}, Aircraft: {self._aircraft.model}, Airline: {self._airline_name}"
