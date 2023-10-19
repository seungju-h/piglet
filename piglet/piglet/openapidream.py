import requests

api_url = "https://www.safe182.go.kr/api/lcm/amberList.do"

params = {
    "esntlId": "10000592",
    "authKey": "91c69af6242a4f12",
    "rowSize": 10,
    # "page": 11,
}

try:
    response = requests.post(api_url, data=params)

    # 성공했을 때
    line_number = 1
    if response.status_code == 200:
        data = response.json()
        items = data.get('list', [])
        for item in items:
            nm = item.get('nm')
            occrAdres = item.get('occrAdres')
            sexdstnDscd = item.get('sexdstnDscd')
            occrde = item.get('occrde')
            age = item.get('age')
            ageNow = item.get('ageNow')

            print(f"{line_number} 이름: {nm}, 성별: {sexdstnDscd}, 발생장소: {occrAdres}, 발생일시: {occrde}, 당시 나이: {age}, 현재 나이: {ageNow}")
            line_number += 1
            
        # print(items)
    else:
        print(f"API request failed with status code: {response.status_code}")
except requests.exceptions.RequestException as e:
    print(f"API request failed: {e}")
