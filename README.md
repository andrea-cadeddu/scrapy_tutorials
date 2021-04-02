# scrapy_tutorials

Scrapy tutorials for the [master tag data science](https://talentgarden.org/it/innovation-school/online/data-science-artificial-intelligence-master/) spring 2021 edition.


## Description

This Scrapy project allows to scrape data of the following websites:
* http://books.toscrape.com
* http://quotes.toscrape.com


## Installation

Install the [Scrapy](https://scrapy.org/) library in your environment

```shell
# PyPI
pip install scrapy
```

```shell
# conda
conda install -c conda-forge scrapy
```

To make sure you have installed the library correctly, run the ```scrapy``` command on the shell.


## Usage

Scrape the data and save the results to json data
* ```spider_name```: [*books*, *quotes*] 
* ```filename```: any value

```shell
scrapy crawl <spider_name> -o data/<filename>.json
```






