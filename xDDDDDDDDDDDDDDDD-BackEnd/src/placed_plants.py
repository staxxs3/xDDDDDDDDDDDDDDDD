import json
from math import hypot, cos
from typing import Tuple, List, Union


class PlacedPlants:
    def __init__(self):
        with open("data.json", "r") as outfile:
            self.__placed_plants_data = json.load(outfile)

    def add_plant(self, name: str, position: Tuple[float, float]):
        plant = {"name": name, "positionX": position[0], "positionY": position[1]}
        if name:
            self.__placed_plants_data.append(plant)
        self.save_database()

    @staticmethod
    def is_plant_in_range(user_position: Tuple[float, float], plant_position: Tuple[float, float],
                          distance: float):
        if abs(user_position[0] - plant_position[0]) < distance:
            if abs(user_position[1] - plant_position[1]) < distance:
                return True

    def show_plants_in_range(self, user_position: Tuple[float, float], distance: float) -> Union[List, dict]:
        plants_to_return = []
        if distance == 0:
            return self.sort_plants(user_position, self.__placed_plants_data)

        for plant in self.__placed_plants_data:
            if self.is_plant_in_range(user_position, (plant["positionX"], plant["positionY"]), distance):
                plants_to_return.append(plant)

        return self.sort_plants(user_position, plants_to_return)

    @staticmethod
    def sort_plants(user_position: Tuple[float, float], plants: list):
        for plant in plants:
            plant["distance"] = hypot(110.574 * (plant["positionX"] - user_position[0]),
                                      111.32 * (plant["positionY"] - user_position[1])
                                      * cos(plant["positionX"]))
            # plant["distance"] = hypot(plant["positionX"] - user_position[0], plant["positionY"] - user_position[1])

        sorted_plants = sorted(plants, key=lambda plant: plant["distance"])
        return sorted_plants

    def save_database(self):
        with open("data.json", "w") as outfile:
            json.dump(self.__placed_plants_data, outfile)
