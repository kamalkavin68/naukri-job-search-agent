from typing import Any
import requests
import json


def job_search_service_provider(query_params: dict[str,Any]):
    base_url = "https://www.naukri.com/jobapi/v3/search"
    headers = {
        'accept': 'application/json',
        'accept-language': 'en-US,en;q=0.9',
        'appid': '109',
        'clientid': 'd3skt0p',
        'content-type': 'application/json',
        'gid': 'LOCATION,INDUSTRY,EDUCATION,FAREA_ROLE',
        'nkparam': 'AuLl3jrpv5HFWDKbdc/AOoDMo40tmCZEY1jND9ZFTwm1Qryb9Ah9aGoX2N4QUGVNgvk3BMULKKgPT8YOsFKfog==',
        'priority': 'u=1, i',
        'referer': 'https://www.naukri.com/java-developer-full-stack-jobs-2?k=java+developer%2C+full+stack',
        'sec-ch-ua': '"Chromium";v="140", "Not=A?Brand";v="24", "Google Chrome";v="140"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'systemid': 'Naukri',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36',
       }
    response = requests.get(base_url, headers=headers, params=query_params)
    json_data = response.json()
    return {"jobDetails":json_data["jobDetails"], "noOfJobs":json_data["noOfJobs"]}
