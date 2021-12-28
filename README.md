# MTG Price Scraper

This script scrapes the price of specific cards on the LigaMagic website. Since it's a brazilian website, the prices are shown in reais.

## What can it do?

For now it'll try to fetch the lowest price of the desired card. Since cards has multiple editions, sometimes it's price will be displayed as R$ 0,00, so the scraper will try to fetch the next best thing. 

## Some issues still stands

As of now if the _lowest price_ is displaying R$ 0,00, it can only fetch a price that has a discount since it's text is explicitly written on the HTML of the page. Any other price is more complicated to fetch for now.
