from faker import Faker
from data.data import Person

faker = Faker()


def generated_person():
    return Person(
        first_name=faker.first_name(),
        last_name=faker.last_name(),
        email=faker.email(),
        phone_number=faker.phone_number(),
        password=faker.password()
    )
