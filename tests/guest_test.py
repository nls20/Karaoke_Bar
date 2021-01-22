import unittest 

from src.guest import *

class TestGuest(unittest.TestCase):

    def setUp(self):
        self.guest = Guest("Dolly Parton", 60.00)
        self.guest_2 = Guest("Janet Joplin", 50.00)


    def test_guest_has_name(self):
        self.assertEqual("Dolly Parton", self.guest.name)

    def test_guest_has_wallet(self):
        self.assertEqual(60.00, self.guest.wallet)