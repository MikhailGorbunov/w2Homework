import unittest
from src.guest import Guest
from src.drink import Drink
from src.food import Food
from src.karaoke_room import KaraokeRoom

class TestGuest(unittest.TestCase):
    
    def setUp(self):
        
        self.drink = Drink("cocktail", 8.00, 8)
        self.food = Food("Drunken_noodles", 8, 5)
        self.guest = Guest("Tom", 40.00, 40, 0, "Jingle Bells")
        self.guest_2 = Guest("Sam", 1.00, 25, 2, "Human")
        self.karaoke = KaraokeRoom("Octapus", 100, 5, 10)


                
    def test_guest_has_name(self):
        self.assertEqual("Tom", self.guest.name)
        
        
    def test_guest_has_wallet(self):
        self.assertEqual(40.00, self.guest.wallet)
        
    
    def test_guest_has_drunkenness(self):
        self.assertEqual(0, self.guest.drunkenness)
    
    
    def test_guest_has_age(self):
        self.assertEqual(40, self.guest.age)
    

    def test_fav_song_name(self):
        self.assertEqual("Jingle Bells", self.guest.fav_song)


    def test_sufficient_funds(self):
     self.assertEqual(True, self.guest.sufficient_funds(self.karaoke.entrance_fee))


    def test_guest_can_buy_entrance_fee__deacreases_wallet(self): 
        self.guest.buy_entrance_fee(self.karaoke.entrance)
        self.assertEqual(30.00, self.guest.wallet)
    

    def test_sufficient_funds__not_enough_cash(self):
        customer = self.guest_2
        self.assertEqual(False, customer.sufficient_funds(self.karaoke.entrance_fee))
    
    def test_fav_song(self):
        # self.guest.fav_song(self.guest.fev_song)
        self.assertEqual("Whoo!", self.guest.fav_song(self.guest.fev_song))
    