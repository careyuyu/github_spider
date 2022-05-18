from scrapy import signals

from time import sleep
from itemadapter import is_item, ItemAdapter
import random

# Two middlewares were set, one for mock User-Agent one for changing proxy ip when current ip is blocked by the site.
class GithubSpiderDownloaderMiddleware:
    # A list of user-agents for spoofing.
    user_agent_list = [
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36',
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.111 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9',
        'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:15.0) Gecko/20100101 Firefox/15.0.1',
        'Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36'
    ]
    # this method is modified to set random mock user-agent for each request. 
    def process_request(self, request, spider):
        request.headers['User-Agent'] = random.choice(self.user_agent_list)
        return None

    def process_exception(self, request, exception, spider):
        return request
    
    def process_response(self, request, response, spider):
        if response.status == 429:
            print("sleeping for 429 @"+request.url)
            sleep(int(response.headers['Retry-After'].decode()))
            return request
        return response
        
