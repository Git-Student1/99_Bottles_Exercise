
class Bottles():
    def __init__(self):
        pass
    def verse(self, number:int):
        return (f'{self.numberOrNoMore(number, True)} {self.bottleOrBottles(number)} of beer on the wall, '
        f'{self.numberOrNoMore(number)} {self.bottleOrBottles(number)} of beer.\n'
        f'Take {self.oneOrIt(number)} down and pass it around, '
        f'{self.numberOrNoMore(number-1)} {self.bottleOrBottles(number-1)} of beer on the wall.\n')

    def oneOrIt(self, number):
        if number == 1: return "it"
        else: return "one"
    def bottleOrBottles(self, number):
        if number == 1:
            return "bottle"
        else:
            return "bottles"

    def numberOrNoMore(self, number, capital=False):

        if number == 0 and  capital:
            return "No more"
        elif number == 0:
            return "no more"
        else: return f"{number}"
