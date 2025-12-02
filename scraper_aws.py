import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta

sutra = (datetime.now() + timedelta(days=1)).strftime('%d.%m.%Y')

url_danas = 'https://www.hep.hr/ods/bez-struje/19?dp=zabok&el=ZB'
url_sutra = 'https://www.hep.hr/ods/bez-struje/19?dp=zabok&el=ZB&datum=' + sutra

for url in (url_danas, url_sutra):
    response = requests.get(url)
    html_content = response.text

    soup = BeautifulSoup(html_content, 'html.parser')

    div_datum = soup.find('h3')

    poruka = "====================================="
    poruka += div_datum.text
    poruka += "====================================="

    div = soup.find('div', class_='radwrap')

    poruka += div.get_text()

return {
    'statusCode': 200,
    'body': json.dumps(poruka)
}