class NationalPark:

    def __init__(self, name):
        self.name = name
        self._trips = []
        self._visitors = []

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if not hasattr(self, 'name') and isinstance(name, str):
            self._name = name
        else:
            raise Exception
        
    def trips(self, new_trip=None):
        from classes.trip import Trip
        if new_trip and isinstance(new_trip, Trip):
            self._trips.append(new_trip)
        return self._trips
    
    def visitors(self, new_visitor=None):
        from classes.visitor import Visitor
        if new_visitor and new_visitor not in self._visitors and isinstance(new_visitor, Visitor):
            self._visitors.append(new_visitor)
        return self._visitors
    
    def total_visits(self):
        return len(self._trips)
    
    def best_visitor(self):
        best_visitor = None
        most_trips = 0
        for visitor in self._visitors:
            visitor_trips = len([trip for trip in self._trips if trip.visitor == visitor])
            if visitor_trips > most_trips:
                most_trips = visitor_trips
                best_visitor = visitor
        return best_visitor