class VehicleBase(object):
    optimum_capacity = None
    max_capacity = None
    priority = None

    def __init__(self):
        self.owner = None
        self.driver = None
        self.people = []

    def get_occupant_count(self):
        return int(bool(self.driver)) + len(self.people)

    def place_people(self, person_pool, force_to_max=False):
        if not self.driver:
            try:
                self.add(person_pool.pop(self.owner.name))
            except KeyError:
                return False

        capacity = self.max_capacity if force_to_max else self.optimum_capacity
        while self.get_occupant_count() < capacity:
            try:
                self.add(person_pool.pop())
            except IndexError:
                break
        return True

    def add(self, person):
        if self.get_occupant_count() == self.max_capacity:
            raise Exception("This vehicle is very full!")

        if not self.driver and person != self.owner:
            raise Exception("This vehicle has no driver!")

        if person is self.owner:
            self.driver = person
        else:
            self.people.append(person)

    def status(self):
        if self.get_occupant_count() == 0:
            return 'Empty'
        elif self.get_occupant_count() < self.optimum_capacity:
            return 'Available'
        elif self.get_occupant_count() < self.max_capacity:
            return 'Full'
        elif self.get_occupant_count() == self.max_capacity:
            return 'Very Full'

    def __repr__(self):
        people_string = ', '.join(person.name for person in self.people)
        if people_string:
            people_string = ' [%s]' % people_string
        return '<%s(%s): %s%s>' % (self.__class__.__name__, self.status(), self.driver.name, people_string)


class Car(VehicleBase):
    optimum_capacity = 5
    max_capacity = 6
    priority = 1


class Motocycle(VehicleBase):
    optimum_capacity = 1
    max_capacity = 2
    priority = 2

    def __init__(self, allow_twoup=True):
        super(Motocycle, self).__init__()
        self.max_capacity = 2 if allow_twoup else 1
