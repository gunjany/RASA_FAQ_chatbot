from rasa_sdk.forms import FormAction
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from typing import Any, Text, Dict, List
from rasa_sdk.events import SlotSet

class SalesForm(FormAction):
	"""Collects sales information and adds it to the spreadsheet"""

	def name(self):
		return "sales_form"

	@staticmethod
	def required_slots(tracker):
		return ["job",
				"use case",
				"name",
				"email",
				"budget",
				"company",]

	def submit(
		self,
		dispatcher: CollectingDispatcher,
		tracker: Tracker,
		domain: Dict[Text, Any],
	) -> List[Dict]:

		dispatcher.utter_message("Thanks for getting in touch, we’ll contact you soon")
		return []