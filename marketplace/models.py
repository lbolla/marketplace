from .application import db


class Product(db.Model):
    REQUIRED = ['name', 'price']
    EDITABLE = ['name', 'price']

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    price = db.Column(db.Numeric(scale=2), nullable=False)

    def as_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            # Note: postman tests seem to require price to be a
            # string, with 2 decimal places
            'price': '{:.2f}'.format(self.price),
        }
