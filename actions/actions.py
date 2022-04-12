# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet

class ActionPredict(Action):

    def name(self) -> Text:
        return "action_predict"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        disease = tracker.get_slot("disease")
        print(disease)

        if disease=='Typhoid':
            dispatcher.utter_message(text="हमें लगता है की आपको टाइफाइड है")
        
        elif disease=='Dengue':
            dispatcher.utter_message(text="हमें लगता है कि आपको डेंगू है")
        
        elif disease=='Migrane':
            dispatcher.utter_message(text="हमें लगता है कि आपको माइग्रेन है")
        
        else:
            dispatcher.utter_message(text="हम अभी आप की बीमारी पहचान नहीं सकते")

        return []
