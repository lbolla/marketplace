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
            # Decimal is not JSON serializable
            'price': float(self.price),
        }
