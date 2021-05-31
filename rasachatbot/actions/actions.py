# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


from typing import Any, Text, Dict, List
import datetime as dt
import requests
import os

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionShowTime(Action):

    def name(self) -> Text:
        return "action_show_time"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text=f"It is {dt.datetime.now()}")

        return []

class ActionCheckAndPrint(Action):

    def name(self):
        return "action_check_and_print"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        csn = tracker.get_slot('cuisine')
        ispn = tracker.get_slot('is_open')
        srtng = '_'.join(tracker.get_slot('sorting').split(" "))
        whlchr = 'wheelchair_accessible' if tracker.get_slot('wheelchair_accessible') else ''

        if not is_cuisine_valid(csn):
            dispatcher.utter_message(text="Sorry, the cuisine is invalid. Please try something else.")
            return []

        if not is_sorting_valid(srtng):
            dispatcher.utter_message(text="Sorry, but you entered an invalid sorting. Please try something else.")
            return []
        try:
            suggestions = make_api_request(csn,ispn,srtng,whlchr)        
            for n in suggestions:
                dispatcher.utter_message(n)
        except:
            dispatcher.utter_message("An error occurred, please try again.")
            return []
        return[]


def is_cuisine_valid(cuisine):
    cuisines = ['czech','chinese','mexican','italian','vegan','french','german','greek','indian','japanese','korean','turkish','georgian']
    if cuisine.lower() not in cuisines:
        return False
    return True

def is_sorting_valid(sorting):
    sortings = ['rating','best_match','review_count']
    if sorting.lower() not in sortings:
        return False
    return True    

def make_api_request(cuisine, is_open,sorting,wheelchair_accessible):
    api_key = os.environ.get("BOT_API_KEY")
    ENDPOINT1 = 'https://api.yelp.com/v3/businesses/search'
    HEADERS = {'Authorization': 'bearer ' + str(api_key)}
    PARAMETERS = {
        'term': 'restaurants',
        'limit': 5,
        'price':"1,2,3,4",
        'location': 'Prague',
        'zip_code': '12000',
        'sort_by': sorting,
        'categories': cuisine,
        'is_open': is_open,
        'attributes': wheelchair_accessible
    }

    response = requests.get(url=ENDPOINT1, params=PARAMETERS, headers=HEADERS)

    business_data = response.json()

    suggestions_list = []
    for i in business_data['businesses']:
        suggestions_list.append(
            "Restaurant " + i['name'] + " with rating " + str(i['rating']) + " and price range " + i['price'] if wheelchair_accessible=="" else
            "Restaurant " + i['name'] + " with rating " + str(i['rating']) + " and price range " + i['price'] + " is wheelchair accessible")

    return suggestions_list












