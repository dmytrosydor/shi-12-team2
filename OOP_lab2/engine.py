class Engine:
    def __init__(self, engine_type: str, horsepower: int):
        self._engine_type = engine_type
        self._horsepower = horsepower

    def get_engine_info(self):
        return f"Engine Type: {self._engine_type}, Horsepower: {self._horsepower}"

