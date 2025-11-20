class RPGclass:
    def __init__(self, weptype, physdam, spelldam, health):
        self.weptype = weptype
        self.physdam = physdam
        self.spelldam = spelldam
        self.health = health
    def warrior(self):
        self.weptype = "Blunt"
        self.physdam = 10
        self.selldam = 0
        self.health = 100
    def mage(self):
        self.weptype = "Staff"
        self.physdam = 0
        self.spelldam = 10
        self.health = 100
    def assassin(self):
        self.weptype = "Small blade"
        self.physdam = 
    def __str__(self):
        return f"Stats : WT: {weptype} ; PD: {physdam} ; SD: {spelldam} ; health : {health}"




w1 = RPGclass(
