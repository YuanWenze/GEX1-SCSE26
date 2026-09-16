airport_info = (None, None, None)

allowed_gates = set()

restricted_destinations = set()

flights = {}

## Logic to find if a flight exists
def find_flight(flights, flight_number):
    key = flight_number.upper().strip()
    if key in flights:
        return key
    return None


## Logic to find if a passenger exists
def passenger_exists(passengers, passenger_name):
    target = passenger_name.lower().strip()
    for p in passengers:
        if p.lower().strip() == target:
            return True
    return False


## Logic to check in a passenger
def check_in_passenger(
    flights,
    flight_number,
    passenger_name,
    restricted_destinations
):
    key = find_flight(flights, flight_number)
    if key is None:
        return "FLIGHT_NOT_FOUND"

    name = passenger_name.strip().title()
    if name == "":
        return "EMPTY_NAME"

    flight = flights[key]

    if flight["destination"] in restricted_destinations:
        return "RESTRICTED"

    if passenger_exists(flight["passengers"], name):
        return "DUPLICATE"

    if len(flight["passengers"]) >= flight["capacity"]:
        return "FULL"

    flight["passengers"].append(name)
    return "OK"


## Logic to remove a passenger from a flight
def remove_passenger(
    flights,
    flight_number,
    passenger_name
):
    key = find_flight(flights, flight_number)
    if key is None:
        return "FLIGHT_NOT_FOUND"

    flight = flights[key]
    target = passenger_name.lower().strip()

    for i in range(len(flight["passengers"])):
        if flight["passengers"][i].lower().strip() == target:
            flight["passengers"].pop(i)
            return "OK"

    return "PASSENGER_NOT_FOUND"


# Logic to change the gate of a flight
def change_gate(
    flights,
    flight_number,
    new_gate,
    allowed_gates
):
    key = find_flight(flights, flight_number)
    if key is None:
        return "FLIGHT_NOT_FOUND"

    gate = new_gate.upper().strip()
    if gate not in allowed_gates:
        return "INVALID_GATE"

    flights[key]["gate"] = gate
    return "OK"


# Logic to get the status of a flight
def flight_status(flight):
    capacity = flight["capacity"]
    passengers_count = len(flight["passengers"])
    percent = (passengers_count / capacity) * 100

    if percent == 100:
        return "FULL"
    elif percent >= 75:
        return "ALMOST FULL"
    else:
        return "AVAILABLE"


# Logic to get the sorted manifest of a flight
def sorted_manifest(
    flights,
    flight_number
):
    key = find_flight(flights, flight_number)
    if key is None:
        return None

    passengers = flights[key]["passengers"]
    return sorted(passengers)


# Logic to get the total number of passengers across all flights
def total_passengers(flights):
    total = 0
    for flight in flights.values():
        total += len(flight["passengers"])
    return total


# Logic to check if any flight is full
def any_full_flight(flights):
    for flight in flights.values():
        if len(flight["passengers"]) >= flight["capacity"]:
            return True
    return False


# Logic to check if all flights have at least one passenger
def all_flights_have_passengers(flights):
    for flight in flights.values():
        if len(flight["passengers"]) == 0:
            return False
    return True