# pylint: disable=no-self-use
from flask import redirect, request, url_for
from flask_restplus import Resource

from .application import api, db
from . import models


@api.route('/products')
class Products(Resource):

    def get(self):
        products = models.Product.query.all()
        return [p.as_dict() for p in products]

    def post(self):
        params = {}
        for f in models.Product.REQUIRED:
            params[f] = request.form[f]
        p = models.Product(**params)
        db.session.add(p)
        db.session.commit()
        return redirect(url_for('product', pid=p.id))


@api.route('/product/<int:pid>')
class Product(Resource):

    def get(self, pid):
        p = models.Product.query.get_or_404(pid)
        return p.as_dict()

    def put(self, pid):
        p = models.Product.query.get_or_404(pid)
        for f in p.EDITABLE:
            if f in request.form:
                setattr(p, f, request.form[f])
        db.session.commit()
        return p.as_dict()

    def delete(self, pid):
        p = models.Product.query.get_or_404(pid)
        db.session.delete(p)
        db.session.commit()
        return None, 201
