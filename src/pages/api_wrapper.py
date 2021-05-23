#!/usr/bin/env python

import os
from yelpapi import YelpAPI

def api_wrapper():
    api_key = os.environ['YELP_API']
    yelp_api = YelpAPI(api_key)

    #response = yelp_api.search_query(term, latitude, longitude, limit, sort_by)
    response = yelp_api.search_query(categories ='restaurants', latitude=50.07851691127118, longitude=14.439893669268018, limit=25, sort_by='distance')
    return response