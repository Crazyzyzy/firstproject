class Car:
    def __init__(self, brand, fool_level, engin_status):
        self.brand = brand
        self._fool_level = fool_level
        self.__engin_status = engin_status

    def start_engin(self):
        if self._fool_level > 0:
            engin_status = True
        else:
            engin_status = False
        return engin_status

    def stop_engin(self):
        if self._fool_level == 0:
            return False
    # def drive(self):
    #     while True:
    #         if self._fool_level > 0:
    #             self._fool_level -= 1
    #         else:
    #             return self._fool_level

    def drive(self):
        if self._fool_level > 0:
            distance = self._fool_level *0.1
            return distance
        else:
            return f"топлива не хватает"

Toyota = Car('Toyota', 10, "False")

print(Toyota.stop_engin())
print(Toyota.drive())