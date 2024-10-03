from crew_member import CrewMember
from aircraft import Aircraft
from constants import MIN_HOURS_FOR_PROMOTION

class Pilot(CrewMember):
    def __init__(self, airline_name: str, name: str, position: str, aircraft: Aircraft):
        super().__init__(airline_name, name, position)
        self._aircraft = aircraft
        self.flight_hours = 0

    def log_flight_hours(self, hours: int):
        self.flight_hours += hours

    def check_promotion(self):
        if self.flight_hours >= MIN_HOURS_FOR_PROMOTION:
            return f"{self._name} is eligible for promotion!"
        return f"{self._name} needs more flight hours for promotion."

    def get_pilot_info(self):
        return f"Pilot: {self._name}, Position: {self._position}, Airline: {self._airline_name}, Aircraft: {self._aircraft.model}"
