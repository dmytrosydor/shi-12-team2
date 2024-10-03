from airline import Airline
from flight import Flight
from aircraft import Aircraft
from pilot import Pilot

def main():
    airline = Airline("Lviv Airlines")
    print(airline)

    aircraft = Aircraft("Boeing 747", "Turbofan", 50000, 64.4, "Fixed-wing")
    print(aircraft)

    flight = Flight("Lviv Airlines", aircraft, "SW123")
    airline.add_flight(flight)

    pilot = Pilot("Lviv Airlines", "Alice Smith", "Pilot", aircraft)
    pilot.log_flight_hours(500)
    print(pilot.check_promotion())
    pilot.log_flight_hours(600)
    print(pilot.check_promotion())


    print(f"Total Airlines: {Airline.count_airlines()}")

if __name__ == "__main__":
    main()
