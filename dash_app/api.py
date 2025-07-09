from datetime import date, timedelta
from pprint import pprint
import requests


def get_devise_data(list_devise, days=30):
    end_days = date.today()
    start_days = end_days - timedelta(days=days)

    r = requests.get(f"https://www.docstring.fr/api/rates/history/?start_at={start_days}&end_at={end_days}&symbols={','.join(list_devise)}")
    if not r and not r.json():
        return False,

    each_devise_dic = { each_devise:[] for each_devise in list_devise}
    dic_devise_data = r.json().get("rates")
    all_days = sorted(dic_devise_data.keys())

    for each_days in all_days:
       [each_devise_dic[dates].append(valeur) for dates, valeur in dic_devise_data[each_days].items()]
    pprint(all_days)
    pprint(each_devise_dic)

    return all_days, each_devise_dic

if __name__ == '__main__':
    days, devise = get_devise_data(["USD", "EUR"], days=30)



