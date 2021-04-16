#!/usr/bin/env python

"""
    Example call:
        python ./test_output.py "[API Key]"
"""

from yelpapi import YelpAPI
import argparse
from pprint import pprint

argparser = argparse.ArgumentParser(description='Yelp API wrapper output testing.')
argparser.add_argument('api_key', type=str, help='Yelp Fusion API Key')
args = argparser.parse_args()

yelp_api = YelpAPI(args.api_key)

"""
    Search by Prague College GPS coordinates and restaurants category.
    
    All Yelp categories: https://www.yelp.com/developers/documentation/v3/all_category_list
"""
print('***** 10 restaurants in the are of Prague College (Polská 1184, 120 00 Vinohrady) *****\n{}\n'.format("yelp_api.search_query(categories='restaurants', longitude=50.07872975105178, latitude=14.440095898104449, limit=5)"))
response = yelp_api.search_query(categories='restaurants', longitude=14.440095898104449, latitude=50.07872975105178, limit=10)
pprint(response)
print('\n-------------------------------------------------------------------------\n')