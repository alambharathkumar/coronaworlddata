from bs4 import BeautifulSoup
from requests import get


def getcorornadata():
    url = 'https://www.worldometers.info/coronavirus/#countries'
    html_content = get(url).text
    html_soup = BeautifulSoup(html_content, "lxml")

    coronadata = dict()
    headerlist = []

    coronaTable = html_soup.find("table", attrs={"class": "table", "id": "main_table_countries_today"})
    corona_table_header = coronaTable.thead.find_all("th")
    corona_table_data = coronaTable.tbody.find_all("tr")

    for headers in corona_table_header:
        headerlist.append(headers.text.replace('\n', ''))

    for outerEnum, values in enumerate(corona_table_data, 1):
        for enum, inrValues in enumerate(values.find_all('td'), 0):
            if enum == 0:
                cntry_val = inrValues.text
                coronadata[cntry_val] = {}
            if enum != 0:
                coronadata[cntry_val][headerlist[enum]] = inrValues.text

    return coronadata


if __name__ == '__main__':
    print("Live Corona Data")
    print(getcorornadata())
