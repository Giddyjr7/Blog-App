from website import create_app, db
from website.models import Category

app = create_app()

with app.app_context():
    # Create initial categories
    cat1 = Category(name="Technology")
    cat2 = Category(name="Travel")
    cat3 = Category(name="Food & Cooking")
    cat4 = Category(name="Lifestyle")
    cat5 = Category(name="Health & Fitness")
    cat6 = Category(name="Arts & Culture")
    cat7 = Category(name="Science")
    cat8 = Category(name="News & Opinion")
    cat9 = Category(name="DIY & Crafts")
    cat10 = Category(name="Finance")

    db.session.add(cat1)
    db.session.add(cat2)
    db.session.add(cat1)
    db.session.add(cat2)
    db.session.add(cat1)
    db.session.add(cat2)
    db.session.add(cat1)
    db.session.add(cat2)
    db.session.add(cat1)
    db.session.add(cat2)


    print("Categories added successfully!")
