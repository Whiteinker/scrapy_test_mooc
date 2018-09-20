# -*- coding: utf-8 -*-
# @Time    : 2018/9/20 9:45
# @Author  : 李超
# @FileName: main.py
# @Software: PyCharm

from scrapy import cmdline
if __name__ == "__main__":
    cmdline.execute('scrapy crawl douban_spider --nolog'.split())
