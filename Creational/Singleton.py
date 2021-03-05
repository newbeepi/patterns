class SingletonMeta(type):
    __instance = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls.__instance:
            instance = super().__call__(*args, **kwargs)
            cls.__instance[cls] = instance
        return cls.__instance[cls]


class Singleton(metaclass=SingletonMeta):
    def function(self):
        ...


if __name__ == '__main__':
    s1 = Singleton()
    s2 = Singleton()

    print(f"s1 id:{id(s1)}\n"
          f"s2 id:{id(s2)}")