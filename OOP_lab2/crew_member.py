from constants import BASE_SALARY, ADDITIONAL_PER_YEAR

class CrewMember:
    def __init__(self, airline_name: str, name: str, position: str):
        self._airline_name = airline_name
        self._name = name
        self._position = position

    def get_info(self):
        return f"Crew Member: {self._name}, Position: {self._position}, Airline: {self._airline_name}"

    @staticmethod
    def calculate_salary(years_of_experience: int) -> float:
        return BASE_SALARY + (ADDITIONAL_PER_YEAR * years_of_experience)
