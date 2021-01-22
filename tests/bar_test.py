import unittest

from src.bar import *
from src.guest import *
from src.room import * 

class TestBar(unittest.TestCase):
    def setUp(self):
        self.bar = Bar("The Karaoke Bar", 15.00)
        self.guest1 = Guest("Dolly Parton", 60.00)
        self.guest2 = Guest("Janet Joplin", 50.00)
        guests = [self.guest1, self.guest2]

    def test_bar_has_name(self):
        self.assertEqual("The Karaoke Bar", self.bar.name)



    

    
     

