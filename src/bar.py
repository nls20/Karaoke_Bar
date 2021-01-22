class Bar():

    def __init__(self, name, entry_fee):
        self.name = name 
        self.entry_fee = entry_fee
        self.song_list = []

    def check_guests(self):
        return len(self.guests)

    def test_bar_has_entry_fee(self):
        return(15.00, self.bar.entry_fee)

    