#!/usr/bin/python3

class K:
    # kernel

    _INSTANCE = None

    def __init__(self):
        super().__init__()

    def getInstance():
        if not K._INSTANCE:
            K._INSTANCE = K()
        return K._INSTANCE

    def proccess(self):
        pass