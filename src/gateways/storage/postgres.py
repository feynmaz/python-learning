
from typing import Iterable
import psycopg2
import psycopg2.extras


from pydantic import PostgresDsn
from src.entities.person import Person
from src.usecases.interfaces import IStorage


class Postgres(IStorage):
    def __init__(self, postgres_dsn: PostgresDsn):
        self.connection = psycopg2.connect(postgres_dsn)
        self.connection.autocommit = True

    def execute(self, query: str, do_return=True):
        with self.connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cursor:
            cursor.execute(query)
            if do_return:
                return cursor.fetchall()

    def get_persons_all(self) -> Iterable[Person]:
        query = """
            select 
                first_name,
                last_name,
                salary
            from hr.employees
        """
        rows: list[dict] = self.execute(query)
        persons = [Person(
            name=row['first_name'],
            surname=row['last_name'],
            salary=row['salary']
        ) for row in rows]
        return persons
        
