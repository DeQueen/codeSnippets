"""
参考网址
https://www.cnblogs.com/xieqiankun/p/know_middleware_of_scrapy_2.html
"""

import random
from scrapy.conf import settings

class ProxyMiddleware(object):
    """
    一个自动更换代理IP的中间件
    """

    def process_request(self, request, spider):
        proxy = random.choice(settings['PROXIES'])
        request.meta['proxy'] = proxy


class UAMiddleware(object):
    """
    一个自动更换User-Agent的中间件
    """
    def process_request(self, request, spider):
        ua = random.choice(settings['USER_AGENT_LIST'])
        request.headers['User-Agent'] = ua


class LoginMiddleware(object):
    """
    一个自动更换Cookies，保持登录状态的中间件
    """
    def __init__(self):
        self.client = redis.StrictRedis()

    def process_request(self, request, spider):
        if spider.name == 'loginSpider':
            cookies = json.loads(self.client.lpop('cookies').decode())
            request.cookies = cookies

from scrapy.http import HtmlResponse
class SeleniumMiddleware(object):
    """
    一个使用Selenium和ChromeDriver或者Selenium和PhantomJS来实现渲染网页的中间件
    """
    def __init__(self):
        self.driver = webdriver.Chrome('./chromedriver')

    def process_request(self, request, spider):
        if spider.name == 'seleniumSpider':
            self.driver.get(request.url)
            time.sleep(2)
            body = self.driver.page_source
        return HtmlResponse(self.driver.current_url,
                            body=body,
                            encoding='utf-8',
                            request=request)