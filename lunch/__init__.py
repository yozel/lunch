import random

def place(person_pool):
    # calculate person count

    # shuffle and sort vehicles (cars first)
    vehicles = [x.vehicle for x in person_pool.people if x.has_vehicle()]
    random.shuffle(vehicles)
    vehicles = sorted(vehicles, key=lambda x: x.priority)

    # calculate person count per vehicle
    result = []
    for vehicle in vehicles:
        if len(person_pool) == 0:
            break
        if vehicle.place_people(person_pool):
            result.append(vehicle)

    if not len(person_pool) == 0:
        for vehicle in vehicles:
            if len(person_pool) == 0:
                break
            vehicle.place_people(person_pool, force_to_max=True)

    if len(person_pool) > 0:
        raise Exception("This lunch out is not possible")

    return result
