Easy project to learn about how Scrapy works.

Reference https://www.scrapingbee.com/blog/web-scraping-with-scrapy/#scrapy-shell for setup steps.

To set up a python environment to play around with easily, you can use the following commands from cmd prompt (for Windows):
    
    python3 -m venv tutorial-env
    
    source tutorial-env/bin/activate

Try the following to start:

    scrapy runspider ecom_spider.py -o product.json
    scrapy runspider sitemap_spider.py -o sitemap_output.csv
    scrapy runspider crawl_spider.py -o crawl_output.csv
