from src.gateways.storage.postgres import Postgres
from src.usecases import person_usecase
from src.settings import settings


postgres = Postgres(settings.PG_DSN)


if __name__ == "__main__":
    count = person_usecase.count_persons(postgres)
    print(count)
