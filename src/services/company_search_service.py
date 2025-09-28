import requests
import json


def company_search_service_provider():
    base_url = "https://www.naukri.com/companyapi/v1/search"

    query_params = {
        "seoKey": "/companies-hiring-in-india",
        "urltype": "search_by_company_general",
        "pageNo": 1,
        "qcount": 10000,
        "searchType": "companySearch"
    }

    headers = {
        'accept': 'application/json',
        'accept-language': 'en-US,en;q=0.9',
        'appid': '103',
        'cache-control': 'no-cache',
        'clientid': 'd3skt0p',
        'content-type': 'application/json',
        'priority': 'u=1, i',
        'referer': 'https://www.naukri.com/companies-hiring-in-india?src=gnbCompanies_homepage_srch',
        'sec-ch-ua': '"Chromium";v="140", "Not=A?Brand";v="24", "Google Chrome";v="140"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'systemid': 'js',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36',
    }

    response = requests.get(base_url, headers=headers, params=query_params)
    json_data = response.json()
    return json_data