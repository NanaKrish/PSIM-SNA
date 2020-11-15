import csv
from pathlib import Path

from psim.agents.entity import Person, Location


def load_user_data(file_name):
    path = Path(file_name).absolute()
    with open(path, 'r') as f:
        reader = csv.reader(f)
        for data in reader:
            yield Person(data[0], int(data[1]), Location(float(data[2]), float(data[3])))
