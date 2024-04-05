
# ID (int): Unique identifier for plant instance
# schedule (int): Watering schedule type (0=undefined, 1=periodic, 2=weekly, 3=sensor)
# name (str): human-readable identifier for Plant instance
# water_interval (int): time interval (in minutes) between waterings (periodic schedule only)
# water_days (set of int): weekdays on which to water (weekly schedule only) - (Mon=0, Tue=1, Wed=2, Thu=3, Fri=4, Sat=6, Sun=6)
# water_times (set of int): times at which to water on watering days, represented as a single int defined by time_int=(hour*60)+minute (weekly schedule only)
# variance (int): allowable variance (+/- in minutes) between intended and actual watering time (periodic & weekly schedule only)

class Plant:

    def __init__(self, ID=None, schedule=0, name="unnamed", water_interval=0, water_days=set(), water_times=set(), variance=0):
        # Universally applicable attributes
        self.ID = ID
        self.schedule = schedule
        self.name = name

        # Schedule-specific attributes

        # Set attributes for periodic schedule
        if schedule == 1:
            self.water_interval = water_interval
            self.variance = variance

        # Set attributes for weekly schedule
            
        # Set attributes for sensor schedule
