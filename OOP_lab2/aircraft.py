from constants import CURRENT_YEAR
from engine import Engine
from wingConfiguration import WingConfiguration


def log_class(cls):
    original_init = cls.__init__

    def new_init(self, *args, **kwargs):
        print(f"Creating instance of {cls.__name__} with arguments: {args}, {kwargs}")
        original_init(self, *args, **kwargs)

    cls.__init__ = new_init
    return cls
@log_class
class Aircraft(Engine , WingConfiguration):
    def __init__(self, model: str, engine_type: str, horsepower: int, wingspan: float, wing_type: str):
        Engine.__init__(self, engine_type, horsepower)
        WingConfiguration.__init__(self, wingspan, wing_type)
        self._model = model

    def get_aircraft_info(self):
        return (f"Aircraft Model: {self._model}\n"
                f"{self.get_engine_info()}\n"
                f"{self.get_wing_info()}")

    def __str__(self):
        return self.get_aircraft_info()

    @property
    def model(self):
        return self._model

    @property
    def capacity(self):
        return self._capacity

    @property
    def age(self) -> int:
        return CURRENT_YEAR - self._year

    def update_capacity(self, new_capacity: int):
        self._capacity = new_capacity
