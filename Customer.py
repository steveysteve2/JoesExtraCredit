class Customer:
    def __init__(self,n, add, t):
        self.__name = n
        self.__address = add
        self.__phone = t

    def get_name(self):
        return self.__name

    def get_address(self):
        return self.__address

    def get_phone(self):
        return self.__phone
    
    def set_name(self, n1):
        self.__name = n1

    def set_address(self, add1):
        self.__address = add1

    def set_phone(self, t1):
        self.__phone = t1

    def print_person(self):
        print(f"Name: {self.get_name()}")
        print(f"Address: {self.get_address()}")
        print(f"Phone: {self.get_phone()}")











































