import unittest
from src.guest import Guest
from src.drink import Drink
from src.food import Food
from src.karaoke_room import KaraokeRoom

class TestKaraokeRoom(unittest.TestCase):
    
    def setUp(self):
        
        self.drink = Drink("cocktail", 8.00, 8)
        self.food = Food("Drunken_noodles", 8, 5)
        self.guest = Guest("Tom", 40.00, 40, 0, "Jingle Bells")
        self.guest_2 = Guest("Sam", 1.00, 25, 2, "Human")
        self.karaoke = KaraokeRoom("Octapus", 100, 5, 10)


                
    def test_karaoke_has_name(self):
        self.assertEqual("Octapus", self.karaoke_room.name)

    def test_customer_has_till(self):
        self.assertEqual(100, self.karaoke_room.till)
     
    def test_customer_has_capacity(self):
        self.assertEqual(5, self.karaoke_room.capacity)        
    
    def test_customer_has_entrance_fee(self):
        self.assertEqual(10, self.karaoke_room.entrance)


    def test_room_starts_empty(self):
        room_counter = self.karaoke_room.room_busy
        self.assertEqual(0,room_counter )


    def test_can_add_person_to_queue(self):
        self.karaoke_room.add_to_queue(self.guest)
         self.karaoke_room.add_to_queue(self.guest_2)
        counter = self.karaoke_room.add_to_counter( )
        self.assertEqual(1, counter)