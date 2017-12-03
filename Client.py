#!/usr/bin/env python
# -*- coding: utf-8 -*-

import xmlrpc

from xmlrpc import client

def main():
    proxy = client.ServerProxy('http://localhost:8000')
    print('Client started')

    game = proxy.Game()
    print(game)
    final = "_"
    while True:
        if (final == "You Die"):
            print(final)
            break
        elif(final == "You Win"):
            print(final)
            break
        elif(final == "The two died"):
            print(final)
            break
        else:
            action = int(input("\nChoose Your Action: \n1- Kick\n2- SwordAttack\n3- Defend \n4- rests \n"))
            final = proxy.Fight(action)
            print(final)




if __name__ == "__main__":
    main()
