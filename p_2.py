"""Write a Python class,

MedPlus, that has three instance variables of type str, int, and float, that respectively represent the name of the medicine, batch number, and its price.

Your class must include a constructor method that initializes each variable to an appropriate value, and your class should include methods for setting the value of each type, and retrieving the value of each type

If the user passes invalid parameters to the constructor method in that case raise an appropriate error to the user of your class

"""
class MedPlus:
    def __init__(self, name: str, batch_num: int, price: float):
        if not isinstance(name, str):
            raise TypeError("name must be a string")
        if not isinstance(batch_num, int):
            raise TypeError("batch_num must be an integer")
        if not isinstance(price, float):
            raise TypeError("price must be a float")
        self.name = name
        self.batch_num = batch_num
        self.price = price
    
    def set_name(self, name: str):
        if not isinstance(name, str):
            raise TypeError("name must be a string")
        self.name = name
    
    def set_batch_num(self, batch_num: int):
        if not isinstance(batch_num, int):
            raise TypeError("batch_num must be an integer")
        self.batch_num = batch_num
    
    def set_price(self, price: float):
        if not isinstance(price, float):
            raise TypeError("price must be a float")
        self.price = price
    
    def get_name(self) -> str:
        return self.name
    
    def get_batch_num(self) -> int:
        return self.batch_num
    
    def get_price(self) -> float:
        return self.price