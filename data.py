        

class Purchase(object):
    def __init__(self, id, product, total_price):
        self.id = id
        self.product = product
        self.total_price = total_price

    @property
    def price_str(self):
        return str(self.total_price) + "$"


class Customer(object):
    def __init__(self, uid, phone, email):
        self.u_id = uid
        self.phone = phone
        self.email = email

