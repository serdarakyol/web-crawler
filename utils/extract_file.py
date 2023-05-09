import csv
from os import getcwd

class JsonToCsv:
    def __init__(self, json_object:dict, output_dir:str, filename:str = "output.csv") -> None:
        self.json_object = json_object
        self.output_dir = output_dir
        self.filename = filename
        if output_dir is None:
            self.output_dir = getcwd()

    def generate_csv(self) -> None:
        print(self.filename)
        field_names = list(self.json_object.keys())
        rows = zip(self.json_object["Title"], self.json_object["Point"], self.json_object["Rank"], self.json_object["Total Command"])
        with open(f"{self.output_dir}/{self.filename}", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(field_names)
            writer.writerows(rows)
        print(f"Data has been generated successfully and saved to {self.output_dir}/{self.filename}")
