from setuptools import setup

setup(name='yahoo_fin_cheese',
      version='0.8.9.6',
      description="""Forked from yahoo_fin to update some outdated functions.
                     Download historical stock prices (daily / weekly / monthly),
                     realtime-prices, fundamentals data, income statements, 
                     cash flows, analyst info, current cryptocurrency prices,
                     option chains, earnings history, and more with yahoo_fin.
                    """,
      url='https://theautomatic.net/yahoo_fin-documentation/',
      author='Cheese Wong',
      author_email='cheese.javaee@gmail.com',
      license='MIT',
      packages=['yahoo_fin'],
      install_requires=[
          "requests_html",
          "feedparser",
          "requests",
          "pandas",
          "pycryptodome",
          "beautifulsoup4==4.11.1",
          "bs4==0.0.2"
      ],
      keywords=["yahoo finance", "stocks", "options", "fundamentals"],
      zip_safe=False)
