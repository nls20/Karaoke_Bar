import unittest

from src.bar import *
from src.guest import *
from src.room import * 
from src.song import *

class TestBar(unittest.TestCase):
    def setUp(self):
        self.bar = Bar("The Karaoke Bar", 15.00, 100.00)

        self.guest = Guest("Dolly Parton", 60.00)
        self.guest2 = Guest("Janet Joplin", 50.00)
        guests = [self.guest, self.guest2]

        self.song1 = Song("Toxic", "Britney Spears", 2.00)
        self.song2 = Song("Wonderwall", "Oasis", 2.00)

        self.room1 = Room("Room 1", 5, 20.00)
        self.room2 = Room("Room 2", 5, 20.00)
        rooms = [self.room1, self.room2]

    def test_bar_has_name(self):
        self.assertEqual("The Karaoke Bar", self.bar.name)

    def test_bar_has_till(self):
        self.assertEqual(100.00, self.bar.till)
    
    def test_bar_has_entry_fee(self):
        self.assertEqual(15.00, self.bar.entry)

    # def test_add_entry_fee_to_till(self):
    #     entry_fee = 15.00
    #     self.pay_for_entry_free(entry_fee)
    #     self.assertEqual(115.00, self.bar.till)

    # def test_charge_entry_fee(self):
    #     self.bar.charge_entry_fee(self.bar.entry)
    #     self.assertEqual(45.00, self.guest.wallet)


    




    



  
 




 

    



    

    
     

