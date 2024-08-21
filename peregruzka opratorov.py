class Buiding:
    def __init__(self, numberOfFloors: int, buildingType: str):
        self.numberOfFloors = numberOfFloors
        self.buildingType = buildingType

    def __eq__(self, other):
        return self.numberOfFloors == self.buildingType


bu1 = Buiding(1, 'один')
bu2 = Buiding(1, 'один')
print(bu1 == bu2)
