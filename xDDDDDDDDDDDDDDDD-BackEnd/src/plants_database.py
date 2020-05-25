import pandas as pd


class Database:
    def __init__(self, database_file="../plants_database.csv"):
        self.database = pd.read_csv(database_file)

    def find_plant(self, name):
        for common_name, scientific_name in zip(self.database["Common Name"],
                                                self.database["Scientific Name with Author"]):
            if common_name == name:
                return scientific_name
