from src.services.job_search_service import job_search_service_provider
from src.utils.url_query_to_dict_convertor import url_query_to_dict


query = """noOfResults=100&urlType=search_by_keyword&searchType=adv&keyword=developer%2C%20software%20developer%2C%20software%20engineer%2C%20software%20development&sort=f&pageNo=1&jobAge=1&jobPostType=1&k=developer%2C%20software%20developer%2C%20software%20engineer%2C%20software%20development&jobAge=1&jobPostType=1&seoKey=developer-software-developer-software-engineer-software-development-jobs&src=cluster&latLong=13.0351104_80.232448&sid=17590449057226043_6"""
print(url_query_to_dict(query=query))