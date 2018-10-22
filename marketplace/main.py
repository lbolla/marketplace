from .application import app, db
from . import models


def fill_data():
    db.create_all()
    for (pid, name, price) in [
            (1, 'Lavender heart', 9.25),
            (2, 'Personalised cufflinks', 45),
            (3, 'Kids T-shirt', 19.95),
    ]:
        p = models.Product(
            id=pid,
            name=name,
            price=price)
        db.session.add(p)
    db.session.commit()


def main():
    fill_data()
    app.run(debug=True)


if __name__ == '__main__':
    main()
