from . import bp as shop
from app import db
from .models import Product
from flask import request, jsonify

@shop.route('/products', methods=['GET'])
def get_products():
    products = Product.query.all()
    return jsonify([p.to_dict() for p in products])

@shop.route('/products/<int:id>', methods=['GET'])
def get_product(id):
    product = Product.query.get(id)
    return jsonify([product.to_dict()])