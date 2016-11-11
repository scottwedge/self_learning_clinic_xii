#!/usr/bin/env python

class Car(object):
    """
    car object
    """

    def __init__(self, name='General', model='GM', vehicle_type=None):
        """
        Instantiate objects
        """
        self.speed = 0
        self.name = name
        self.model = model
        self.vehicle_type = vehicle_type

        if self.name in ['Porshe', 'Koenigsegg']:
            self.num_of_doors = 2
        else:
            self.num_of_doors = 4

        if self.vehicle_type == 'trailer':
            self.num_of_wheels = 8
        else:
            self.num_of_wheels = 4

    def is_saloon(self):
        """
        check whether a vehicle is a saloon
        """
        if self.vehicle_type is not 'trailer':
            self.vehicle_type == 'saloon'
            return True
        return False

    def drive(self, moving_speed):
        if moving_speed == 3:
            self.speed = 1000
        elif moving_speed == 7:
            self.speed = 77
        return self
