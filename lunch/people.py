import random


class Person(object):
    def __init__(self, name, vehicle=None):
        self.name = name
        self.vehicle = vehicle

        if self.vehicle:
            self.vehicle.owner = self

    def __repr__(self):
        return '<%s: %s>' % (self.__class__.__name__, self.name)

    def has_vehicle(self):
        if self.vehicle:
            return True
        else:
            return False


class PersonPool(object):
    def __init__(self, person_list):
        self.people = list()
        for person in person_list:
            self.people.append(person)

    def __getitem__(self, name):
        for person in self.people:
            if name == person.name:
                return person
        raise KeyError(name)

    def __repr__(self):
        return "<PersonPool: %s>" % str(self.people)

    def __len__(self):
        return len(self.people)

    def pop(self, name=None):
        non_driver_people = [person for person in self.people
                                 if not person.has_vehicle()]

        if not self.people:
            raise IndexError()
        elif name:
            pop = self[name]
        elif non_driver_people:
            pop = random.choice(non_driver_people)
        else:
            pop = random.choice(self.people)

        index = self.people.index(pop)
        return self.people.pop(index)


