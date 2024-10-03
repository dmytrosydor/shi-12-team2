class WingConfiguration:
    def __init__(self, wingspan: float, wing_type: str):
        self._wingspan = wingspan
        self._wing_type = wing_type

    def get_wing_info(self):
        return f"Wingspan: {self._wingspan} meters, Wing Type: {self._wing_type}"
