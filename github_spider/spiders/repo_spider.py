import re
import scrapy
from github_spider.items import RepoItem


class RepoSpiderSpider(scrapy.Spider):
    name = 'repo_spider'
    allowed_domains = ['github.com']
    start_urls = ['https://github.com/search?q=stars:>10000&type=Repositories']

    def parse(self, response):
        repo_li_list = response.xpath("//ul[@class='repo-list']/li")
        for li in repo_li_list:
            newurl = li.xpath(".//a[@class='v-align-middle']/@href").extract_first()
            yield response.follow(newurl, self.parse_repo)
        next_page = response.xpath("//a[@class='next_page']/@href").extract_first()
        if next_page is not None:
            yield response.follow(next_page, self.parse)

    
    def parse_repo(self, response):
        newItem = RepoItem()
        newItem["url"] = response.url
        newItem["star"] = response.xpath("//span[@id='repo-stars-counter-star']/@title").extract_first()
        newItem["fork"] = response.xpath("//span[@id='repo-network-counter']/@title").extract_first()
        yield newItem
