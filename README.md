 webeval

Popular datasets served as webpages for evaluating web crawlers.

webeval generates a static site — an `index.html` listing all documents, each rendered as its own HTML page. Point your crawler at it and you have a reproducible, web-oriented benchmark.

![license](https://img.shields.io/badge/license-MIT-blue)
![status](https://img.shields.io/badge/status-early%20dev-orange)
![python](https://img.shields.io/badge/python-3.10%2B-blue)

## How it works

```
dataset → index.html + one HTML page per document
```

Your crawler hits the index, follows the links, and scrapes the pages.

## License

MIT
