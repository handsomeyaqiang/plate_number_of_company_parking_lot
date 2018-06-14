from abc import ABCMeta, abstractmethod


class RecongiseDao:
    __metaclass__ = ABCMeta

    @abstractmethod
    def recongise(self):
        pass
