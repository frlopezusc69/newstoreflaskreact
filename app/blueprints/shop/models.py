from app import db

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sku = db.Column(db.String(15), nullable=False)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    image = db.Column(db.String(255), nullable=False)
    amount = db.Column(db.Numeric(5,2), nullable=False)

    def __init__(self, sku, name, description, image, amount):
        self.sku = sku
        self.name = name
        self.description = description
        self.image = image
        self.amount = amount

    def __repr__(self):
        return f'<Product | {self.name}>'

    def to_dict(self):
        return {
            'id': self.id,
            'sku': self.sku,
            'name': self.name,
            'description': self.description,
            'image': self.image,
            'amount': str(self.amount)
        }