class ServiceQuote:
    def __init__(self,pc, lc, st):
        self.__parts_charges = pc
        self.__labor_charges = lc
        self.__sales_tax = st

    def get_parts_charges(self):
        return self.__parts_charges

    def get_labor_charges(self):
        return self.__labor_charges

    def get_sales_tax(self):
        totalcharge = self.__labor_charges + self.__parts_charges
        st = self.__sales_tax * totalcharge
        stround = round(st, 2)
        return stround
    
    def get_total_charges(self):
        totalcharge = self.__labor_charges + self.__parts_charges
        st = self.__sales_tax * totalcharge
        stround = round(st, 2)
        total  = totalcharge + stround
        return total
    
    def set_parts_charges(self, m1):
        self.__parts_charges = m1

    def set_labor_charges(self, mo1):
        self.__labor_charges = mo1



























