import requests
import time
import json

# проверка ограничения частоты запросов на беке
#  запуск в терминале командой python test_rate_limit.py

# Настройки
url = "https://api.vezubr.dev/v1/api/order/35930/details"
headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJpYXQiOjE3NTc2NzM1NTMsImV4cCI6MTc2MTI3MzU1MywidXNlcm5hbWUiOiI2NmE0MTU0YmUwM2ZlOGI2ZmRmNDc3NTkzNDZkMmVkZmY2ZDA5ZDBmMDZjOTQxYzAyODlkMjMxNTZiZjAxZWRiIiwiY29udHJhY3RvcklkIjoxNjc0LCJjb250cmFjdG9yS2V5IjoiN2EyZDk5MmUiLCJpZCI6Mzk1OCwidXNlcklkIjozOTk5LCJ1c2VyS2V5IjoiNTY2Nzc5ZGIiLCJjZW50cmlmdWdvVG9rZW4iOiJleUowZVhBaU9pSktWMVFpTENKaGJHY2lPaUpJVXpJMU5pSjkuZXlKemRXSWlPaUl6T1RVNElpd2laWGh3SWpveE56VTNOelU1T1RVekxDSnBibVp2SWpwN0luVnpaWEp1WVcxbElqcHVkV3hzZlgwLnNZQzNZXzRvVXUySEg5b05kdUoxcElIb1lxVjktelVIWlp5dlpXVXBkTGsiLCJoZWxwRGVza0VkZHlUb2tlbiI6ImV5SjBlWEFpT2lKS1YxUWlMQ0poYkdjaU9pSklVekkxTmlKOS5leUpwWVhRaU9qRTNOVGMyTnpNMU5UTXNJbXAwYVNJNklqTTROakF4TjJaakxUSXlPRFl0TkRJeE5pMWhNelZpTFRsa09EUTRNRGhpWmpKaVpDSXNJbVZ0WVdsc0lqb2lkbVY2ZFdKeUxuQnliMlIxWTJWeVFHMWhhV3d1Y25VaUxDSnVZVzFsSWpvaVhIVXdOREkxWEhVd05ETmxYSFV3TkRRMVhIVXdORE5pWEhVd05ETmxYSFV3TkRNeVhIVXdORE13SUZ4MU1EUXhNRngxTURRellseDFNRFF6TlZ4MU1EUXpZVngxTURRME1WeDFNRFF6TUZ4MU1EUXpaRngxTURRek5GeDFNRFEwTUNCb2FHaG9NREF3TURJeElpd2liM0puWVc1cGVtRjBhVzl1SWpvaVhIVXdOREZsWEhVd05ERmxYSFV3TkRGbElGd2lYSFV3TkRGbVhIVXdOREZsWEhVd05ERTBYSFV3TkRJd1hIVXdOREptWEhVd05ERTBYSFV3TkRJM1hIVXdOREU0WEhVd05ERmhYQ0lpTENKd2FHOXVaU0k2Ym5Wc2JIMC41bm5TM1pjekRYYjVmQzhXRUhQWjRxX3lNSHFPdUtSOUdsS013RDJJTG9jIiwiZW1wbG95ZWVSb2xlcyI6WzIsMTMsMTRdfQ.So0j15XS5nkataaQRlrohcSLnEhH3KpkaioGxmCNbB6NCTEcRc2hP15hsW7YMsRcAWrAAhCmMBfEtbSmWdUh--vlJXJ8Kw57815Ic7dKZ6TowYFkPU8Z0mxj7sNxXlGfLgu2LXz372VQ_ztiweHxruu_OTUHHft6WbcPyXAmKwrAopBQobFaA4foJqzRnnWJk3Qk1PoYsKXrTJuYyUI5xGJFefJIkqWw6RCv5OGfysHZFM4DjCjUGnJ161rUdjS6t449fTp7I5UcaMiKkA0ov0EQZDWX4pfFMW774OAsZRzMlet5V4gD7iyD3yg7pNcsjSVolEadOZR82pl3okTbvSO2TxU0VXyYosBEaSHZ6QGR_nBwPJKUHkZ2TNAK-mgH_SMOdn-8U2BH8euJNK8qY7o10GRZO3Z1I6PDCss8KiGTHH0mcPXvw3anmyII3LVEy_70tONQRY_7JZ1wlw03gS5ZTlipjcTsVJFBLlLKMqfXBS3gMZ4_dSpw5CYKAw0IjhYOjArvL-SZ_pMTbmpaprJmCgk62er7n9zWsQdmT1yXj1WpiSixDmnSy4MnmOLCZwuvBPI7-LuO8PV7-VOnoORHfqqV6ABDKBA2OwRfTjnIQKaVlWGKdNUq9Rnp4IAre8eVZEs7-OE7htCCqkZ6oq_wwRbz28cLmhrboa5fMQU',
    'content-type': 'application/json',
    'origin': 'https://producer.vezubr.dev',
    'referer': 'https://producer.vezubr.dev/',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Chromium";v="140", "Not=A?Brand";v="24", "Google Chrome";v="140"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
}

# Параметры цикла
delay_between_requests = 1  # Задержка между запросами в секундах
max_requests = 50  # Сколько раз отправить запрос

print(f"Начинаем отправку {max_requests} запросов с интервалом {delay_between_requests} сек.\n")

for i in range(1, max_requests + 1):
    try:
        print(f"[{i}] Отправляю запрос...")
        response = requests.get(url, headers=headers)

        status = response.status_code
        try:
            body = response.json()
        except json.JSONDecodeError:
            body = response.text[:200]  # первые 200 символов, если не JSON

        print(f"Статус: {status}")
        if status == 429:
            print("⚠️ ВНИМАНИЕ: Получен статус 429 — Rate Limit Exceeded!")
            print("Бэкенд действительно ограничивает частоту запросов.")
            break  # можно убрать, если хочешь продолжать
        elif status >= 500:
            print(f"❌ Ошибка сервера: {status}")
        elif status >= 400:
            print(f"❌ Клиентская ошибка: {status}")

        print(f"Ответ: {body}\n")

    except requests.exceptions.RequestException as e:
        print(f"Ошибка сети: {e}\n")

    # Задержка перед следующим запросом
    time.sleep(delay_between_requests)

print("Тест завершён.")