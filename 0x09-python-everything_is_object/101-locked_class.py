#!/usr/bin/python3
class LockedClass:
    def __setattr__(self, name, value):
        if hasattr(self, 'first_name') or name == 'first_name':
            object.__setattr__(self, name, value)
        else:
            raise AttributeError("'LockedClass' object has no attribute '{}'".format(name))
