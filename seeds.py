from webcalc import app, mongo

def run():

    with app.app_context():

        mongo.db.operations.insert(
            dict(
                name="+",
                pattern="{{ a + b }}"
            )
        )

        mongo.db.operations.insert(
            dict(
                name="x",
                pattern="{{ a * b }}"
            )
        )

        mongo.db.operations.insert(
            dict(
                name="d",
                pattern="{{ a / b }}"
            )
        )

        mongo.db.operations.insert(
            dict(
                name="-",
                pattern="{{ a - b }}"
            )
        )

        mongo.db.operations.insert(
            dict(
                name="*",
                pattern="{{ a * b }}"
            )
        )

if __name__ == '__main__':
    run()
