class Airline:
    airlines = []

    def __init__(self, name: str):
        self._flights = []
        self._name = name
        Airline.airlines.append(self)

    def __str__(self):
        return f"Airline: {self._name}, Number of Flights: {len(self._flights)}"

    def add_flight(self, flight):
        self._flights.append(flight)

    def remove_flight(self, flight_number: str):
        self._flights = [f for f in self._flights if f.flight_number != flight_number]

    def get_flight_info(self, flight_number: str):
        for flight in self._flights:
            if flight.flight_number == flight_number:
                return flight.get_flight_info()
        return f"Flight {flight_number} not found in {self._name}."

    @staticmethod
    def count_airlines():
        return len(Airline.airlines)
