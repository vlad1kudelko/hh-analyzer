from db.engine import init_db
import requests

def main() -> None:
    init_db()
    #print( requests.get('https://api.hh.ru/vacancies').text )

if __name__ == "__main__":
    main()