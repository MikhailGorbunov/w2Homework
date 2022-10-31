from itertools import count


class KaraokeRoom:
    
    def __init__(self, name, till, capacity, entrance_fee):
        self.name = name
        self.till = till
        self.capacity = capacity
        self.room = {}
        self.entrance = entrance_fee

    def add_to_room(self, person):
        self.room.append(person)

    def room_busy(self):
        room_counter = len(self.room)

    def add_to_counter(self, room):
        counter = 0
        person = len(room)
        for p in person:
            counter +=1
            
        if counter > 5:
            return "fail"