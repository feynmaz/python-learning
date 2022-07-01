
from src.entities.person import Person
from src.usecases.interfaces import IStorage


def multiply_age(person: Person, multiplier: int) -> Person:
    new_age = person.age * multiplier
    person.age = new_age
    return person


def count_persons(storage: IStorage) -> int:
    persons = storage.get_persons_all()
    return len(persons)
