class Coffee:

    all = []

    def __init__(self, name):
        if not isinstance(name, str) or len(name) < 3:
            raise ValueError("Name must be of type string and at least 3 characters")
        self._name = name
        Coffee.all.append(self)
        
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if hasattr(self, "_name"):
            raise AttributeError("Cannot modify name after instantiation.")
        self._name = value

    def orders(self):
        return [order for order in Order.all if order.coffee == self]
    
    def customers(self):
        return list({order.customer for order in self.orders()})
    
    def num_orders(self):
        return len(self.orders())
    
    def average_price(self):
        customer_average = [order.price for order in self.orders() if order.coffee == self]
        if not customer_average:
            return 0        
        return sum(customer_average) / len(customer_average)

class Customer:
    def __init__(self, name):
        if not isinstance(name, str) or not (1 <= len(name) <= 15):
            raise ValueError("Name must be of type string and between 1 and 15 characters long.")    
        self._name = name
    
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or not (1 <= len(value) <= 15):
            raise ValueError("Name must be of type string and between 1 and 15 characters long.")    
        self._name = value

    def orders(self):
        return [order for order in Order.all if order.customer == self]
    
    def coffees(self):
        return list({order.coffee for order in self.orders()})
    
    def create_order(self, coffee, price):
        if not isinstance(coffee, Coffee):
            raise ValueError("Coffee must be an instance of Coffee")
        if not isinstance(price, (int, float)) or price <= 0:
            raise ValueError("Price must be a positive number.")
        return Order(self, coffee, price)
    
class Order:

    all = []

    def __init__(self, customer, coffee, price):
        if not isinstance(customer, Customer):
            raise ValueError("Customer must be an instance of Customer")
        if not isinstance(coffee, Coffee):
            raise ValueError("Coffee must be an instance of Coffee.")
        if not isinstance(price, float) or not (1.0 < price < 10.0):
            raise ValueError("Price must be a float between 1.0 and 10.0")
        
        self._customer = customer
        self._coffee = coffee
        self._price = price
        Order.all.append(self)

    @property
    def customer(self):
        return self._customer
    
    @property
    def coffee(self):
        return self._coffee
    
    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if hasattr(self, "_price"):
            raise AttributeError("Cannot modify price after instantiation")
        self._price = value