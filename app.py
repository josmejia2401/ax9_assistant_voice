#!/usr/bin/python3
from src.main import Main
if __name__ == '__main__':
    try:
        main = Main()
        main.init()
    except Exception as e:
        print(e)
