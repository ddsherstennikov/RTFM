import sys
import backend.gateway

class Gate(object):
    _instance = None
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Gate, cls).__new__(
                                cls, *args, **kwargs)
        return cls._instance
    def hello(self):
        return backend.gateway.hello()

def main():
    g = Gate()
    s = g.hello()
    print s

if __name__ == '__main__':
    main()
