from src.services.job_search_service import job_search_service_provider

query = {
    "noOfResults": 100,
    "urlType": "search_by_keyword",
    "searchType": "adv",
    "keyword": "developer, software developer, software engineer, software development",
    "sort": "f",
    "pageNo": 1,
    "jobAge": 3,
    "k": "developer, software developer, software engineer, software development",
    "seoKey": "developer-software-developer-software-engineer-software-development-jobs",
    "src": "sortby",
    "latLong": "13.0351104_80.232448",
    "sid": "17590433827875272_1"
}
data = job_search_service_provider(query)
print(data)