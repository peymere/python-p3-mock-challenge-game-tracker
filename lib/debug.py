#!/usr/bin/env python3
import ipdb

from classes.many_to_many import Player
from classes.many_to_many import Game
from classes.many_to_many import Result

if __name__ == '__main__':
    print("HELLO! :) let's debug :vibing_potato:")

    g1 = Game("Monopoly")
    g2 = Game("Settlers of Catan")
    g3 = Game("Risk")
    g4 = Game("Werewolf")

    p1 = Player("nymeria")
    p2 = Player("tony.two.hands")
    p3 = Player("otto.hands")

    r1 = Result(p1, g1, 350)
    r2 = Result(p1, g2, 2000)
    r3 = Result(p1, g4, 1500)
    r4 = Result(p2, g3, 5000)
    r5 = Result(p2, g1, 700)
    r6 = Result(p2, g4, 700)
    r7 = Result(p3, g1, 1900)
    r8 = Result(p3, g3, 4500)
    r9 = Result(p3, g2, 1450)
    r10 = Result(p3, g4, 3500)
    r11 = Result(p1, g1, 3800)

    ipdb.set_trace()

