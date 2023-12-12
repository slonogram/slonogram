from abc import ABCMeta, abstractmethod


class Statement(metaclass=ABCMeta):
    def __repr__(self) -> str:
        return self.generate()

    @abstractmethod
    def generate(self) -> str:
        raise NotImplementedError
