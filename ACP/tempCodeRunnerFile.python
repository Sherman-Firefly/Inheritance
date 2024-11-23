class Bus:
    def __init__(self, pl):
        self.pl=pl

class price(Bus):
    def __init__(self, pl, basic_fare):
        super().__init__(pl)
        self.basic_fare=basic_fare

    def calcf(self):
        if self.pl < 20:
            tf=self.basic_fare * 1.0
        elif 20 < self.pl <= 50:
            tf=self.basic_fare * 1.2
        else:
            tf=self.basic_fare *2.0

        return tf
    
pl=int(input("Input passenger limit of bus"))
basic_fare=float(input("input base fare"))

busfare=price(pl,basic_fare)

print(f"The calculated bus fare is: ${busfare.calcf():.2f}")
