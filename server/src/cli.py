import datetime
from urllib3.util import url
from db.engine import init_db, session_factory
from db.models import Area, Vacancy
import requests


def pars(inp_text: str = '', inp_page: int = 0) -> None:
    ret = requests.get(f'https://api.hh.ru/vacancies?text={inp_text}&page={inp_page}').json()
    for item in ret['items']:
        with session_factory() as session:
            vacancy_id: int = int(item['id'])
            area_id: int = int(item['area']['id'])
            query = session.query(Area).filter(Area.area_id == area_id)
            area_exists = query.first()
            if area_exists is None:
                area = Area(
                    area_id = area_id,
                    name    = item['area']['name'],
                    url     = item['area']['url']
                )
                session.add(area)

            query = session.query(Vacancy).filter(Vacancy.vacancy_id == vacancy_id)
            vacancy_exists = query.first()
            if vacancy_exists is None:
                #print(item)
                vacancy = Vacancy(
                    vacancy_id      = vacancy_id,
                    url             = item['alternate_url'],
                    name            = item['name'],
                    area_id         = area_id,
                    salary_from     = (item.get('salary_range', {}) or {}).get('from'),
                    salary_to       = (item.get('salary_range', {}) or {}).get('to'),
                    salary_currency = (item.get('salary_range', {}) or {}).get('currency'),
                    salary_gross    = (item.get('salary_range', {}) or {}).get('gross'),
                    salary_mode     = (item.get('salary_range', {}) or {}).get('mode', {}).get('id'),
                    published_at    = datetime.datetime.fromisoformat(item['published_at']),
                    created_at      = datetime.datetime.fromisoformat(item['created_at']),
                    benefits        = item.get('benefits'),
                    archived        = item['archived'],
                    requirement     = item.get('snippet', {}).get('requirement'),
                    responsibility  = item.get('snippet', {}).get('responsibility'),
                )
                session.add(vacancy)
                session.commit()
    print([
        inp_text,
        ret['found'],
        ret['page'],
        ret['pages'],
        ret['per_page'],
    ])
    if ret['page'] + 1 < ret['pages']:
        pars(inp_text, ret['page']+1)


def main() -> None:
    init_db()
    for item in ['python', 'fastapi', 'postgresql']:
        pars(item)


if __name__ == "__main__":
    main()