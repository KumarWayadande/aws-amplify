import random

class Flight:
    def __init__(self, flight_id, origin, destination, departure_time, arrival_time, aircraft_capacity):
        self.flight_id = flight_id
        self.origin = origin
        self.destination = destination
        self.departure_time = departure_time
        self.arrival_time = arrival_time
        self.aircraft_capacity = aircraft_capacity  # max passengers or weight for cargo
        self.assigned_cargo = []
        
    def __str__(self):
        return f"Flight {self.flight_id}: {self.origin} -> {self.destination} (Departure: {self.departure_time}, Arrival: {self.arrival_time})"

    def can_assign_cargo(self, cargo_weight):
        # Check if the flight has enough capacity for the cargo
        return sum([cargo['weight'] for cargo in self.assigned_cargo]) + cargo_weight <= self.aircraft_capacity


class Cargo:
    def __init__(self, cargo_id, cargo_type, weight, priority):
        self.cargo_id = cargo_id
        self.cargo_type = cargo_type  # e.g., 'perishable', 'standard', 'heavy'
        self.weight = weight
        self.priority = priority  # 1 for high priority, 2 for medium, 3 for low
        
    def __str__(self):
        return f"{self.cargo_type} Cargo {self.cargo_id} (Weight: {self.weight}kg, Priority: {self.priority})"


class AirlineScheduler:
    def __init__(self, flights, cargos):
        self.flights = flights
        self.cargos = cargos

    def assign_cargo_to_flights(self):
        """
        Assign cargos to available flights based on priority and available capacity.
        """
        for cargo in sorted(self.cargos, key=lambda x: x.priority):  # prioritize high priority cargo
            assigned = False
            for flight in self.flights:
                if flight.can_assign_cargo(cargo.weight):
                    flight.assigned_cargo.append({'cargo': cargo, 'weight': cargo.weight})
                    assigned = True
                    print(f"Assigning {cargo} to {flight}")
                    break
            if not assigned:
                print(f"Cargo {cargo} could not be assigned to any flight due to capacity constraints.")

    def print_schedules(self):
        print("\nFlight Schedules and Assigned Cargo:")
        for flight in self.flights:
            print(f"\n{flight}")
            if flight.assigned_cargo:
                for assigned_cargo in flight.assigned_cargo:
                    print(f"  - {assigned_cargo['cargo']}")
            else:
                print("  No cargo assigned.")

# Example of flights and cargo
flights = [
    Flight(flight_id=101, origin="New York", destination="London", departure_time="2025-05-01 08:00", arrival_time="2025-05-01 20:00", aircraft_capacity=10000),  # kg capacity
    Flight(flight_id=102, origin="London", destination="Tokyo", departure_time="2025-05-02 10:00", arrival_time="2025-05-02 22:00", aircraft_capacity=8000),
    Flight(flight_id=103, origin="Tokyo", destination="New York", departure_time="2025-05-03 12:00", arrival_time="2025-05-03 23:00", aircraft_capacity=12000)
]

cargos = [
    Cargo(cargo_id=1, cargo_type="Perishable", weight=5000, priority=1),
    Cargo(cargo_id=2, cargo_type="Heavy", weight=7000, priority=2),
    Cargo(cargo_id=3, cargo_type="Standard", weight=2000, priority=3),
    Cargo(cargo_id=4, cargo_type="Perishable", weight=1000, priority=1),
    Cargo(cargo_id=5, cargo_type="Standard", weight=4000, priority=3)
]

# Create an AirlineScheduler instance
scheduler = AirlineScheduler(flights, cargos)

# Assign cargo to flights and print the schedules
scheduler.assign_cargo_to_flights()
scheduler.print_schedules()
