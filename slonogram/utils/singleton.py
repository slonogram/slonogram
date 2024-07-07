# This code was copied from the adaptix source

def _singleton_repr(self):
    return f"{type(self).__name__}()"


def _singleton_hash(self) -> int:
    return hash(type(self))


def _singleton_copy(self):
    return self


def _singleton_deepcopy(self, memo):
    return self


def _singleton_new(cls):
    return cls._instance


class SingletonMeta(type):
    def __new__(mcs, name, bases, namespace, **kwargs):
        namespace.setdefault("__repr__", _singleton_repr)
        namespace.setdefault("__str__", _singleton_repr)
        namespace.setdefault("__hash__", _singleton_hash)
        namespace.setdefault("__copy__", _singleton_copy)
        namespace.setdefault("__deepcopy__", _singleton_deepcopy)
        namespace.setdefault("__slots__", ())
        cls = super().__new__(mcs, name, bases, namespace, **kwargs)

        instance = super().__call__(cls)
        cls._instance = instance
        if "__new__" not in cls.__dict__:
            cls.__new__ = _singleton_new
        return cls

    def __call__(cls):
        return cls._instance


__all__ = ["SingletonMeta"]

