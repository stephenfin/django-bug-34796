from django.db import migrations


def generate_data(apps, schema_editor):
    Restaurant = apps.get_model("places", "Restaurant")
    PostOffice = apps.get_model("places", "PostOffice")

    restaurant = Restaurant(
        name="Bob's Cafe",
        address="1 High Street",
        serves_hot_dogs=False,
        serves_pizza=True,
    )
    restaurant.save()

    post_office = PostOffice(
        name="GPO",
        address="O'Connell Street",
        accepts_parcels=True,
        has_atm=True,
    )
    post_office.save()


class Migration(migrations.Migration):
    dependencies = [
        ("places", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(generate_data),
    ]
