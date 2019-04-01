from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_core.actions.action import Action
from rasa_core.events import SlotSet
from rasa_core.trackers import DialogueStateTracker
from rasa_core.slots import TextSlot
from rasa_core.actions.action import ActionDefaultFallback

class ActionWiki(Action):
	def name(self):
		return 'action_general_stat'

	def run(self, dispatcher, tracker, domain):
		import wikipedia
		slot = tracker.get_slot('statTerm')
		summary = wikipedia.summary(slot, sentences = 3)

		dispatcher.utter_message(summary)
		return [SlotSet('statTerm', slot)]

class ActionDefaultFallback(Action):
	"""Executes the fallback action and goes back to the previous state
	of the dialogue"""    
	def name(self):
		return 'action_default_fallback'
	
	def run(self, dispatcher, tracker, domain):
		from rasa_core.events import UserUtteranceReverted
		
		dispatcher.utter_template("utter_default", tracker,
								  silent_fail=True)

		return [UserUtteranceReverted()]

class ActiongetObs(Action):
	def name(self):
		return "action_get_obs"

	def run(self, dispatcher, tracker, domain):

		print("Will you help me with some information regarding the dataset\n")

		obs = None
		while type(obs) is not int:
			try:
				obs = input("Please enter the number of observations : ")
				obs = int(obs)
				print("The number of observations are: ",obs)
			except ValueError:
				print(obs, "Please enter an integer..\n")
		
		return [SlotSet("num_observations", obs)]

class ActiongetVar(Action):
	def name(self):
		return "action_get_var"

	def run(self, dispatcher, tracker, domain):

		var = None
		while type(var) is not int:
			try:
				var = input("Please enter the number of variables : ")
				var = int(var)
				print("The number of variables are: ", var)
			except ValueError:
				print(var, "Please enter an integer.\n")
		
		return [SlotSet("num_variables", var)]


class ActiongetAnalysisType:
	def name(self):
		return "action_get_analysis_type" 

	def run(self, dispatcher, tracker, domain):

		if tracker.get_slot('num_variables') > tracker.get_slot('num_observations'):
			print("""I suggest you to do a principal component analysis to reduce the dimension of your 
				     dataset, I can help you with that""")
			return [SlotSet("default_ml_type", "principal ca")]
		else:
			typee_an = None
			while type(typee_an) is not int:
				try:
					typee_an = input("""Please tell me the type of the analysis that you want to do, 
									Press 1 for regression, 2 for classification, 3 for clustering\n""")
					typee_an = int(typee_an)
				except ValueError:
					print(typee_an, "is not 1, 2, 3 or 4.\n")
								
			if int(typee_an) == 1 :
				print('The best Machine learning algorithm that I recommend is Multiple_regression')
				return [SlotSet("default_ml_type", "multiple regression")]
			elif int(typee_an) == 2:
				response_type = input("""Please tell me the number of levels in your response variable, 
									     Press 1 for two-level(binary), 2 for multi-level\n""")
				if int(response_type) == 1:
					print('The best Machine learning algorithm that I recommend is Logistic regression')
					return [SlotSet("default_ml_type", "logistic regression")]
				else :
					preferred_classification = input("""Please tell me whether you require a model or only looking 
														for improved accuracy, Press 1 for accuracy, 2 for an intepretable model\n""")
					if int(preferred_classification) == 1:
						print('The best Machine learning algorithm that I recommend is a random forest')
						return [SlotSet("default_ml_type", "random forest")]
					else :
						print('The best Machine learning algorithm that I recommend is a decision tree')
						return [SlotSet("default_ml_type", "decision tree")]
			elif int(typee_an) == 3:
				cluster_type = input("""Please tell me if you have already selected the number of clusters to be in the dataset, 
									    Press 1 for known, 2 for unknown\n""")
				if cluster_type == 1:
					print('The best Machine learning algorithm that I recommend is K-Means clustering')
					return [SlotSet("default_ml_type", "kmeans clustering")]
				else:
					print('The best Machine learning algorithm that I recommend is Hierachical clustering')
					return [SlotSet("default_ml_type", "hierachical clustering")]
			

class ActionAccessDB:
	def name(self):
		return "action_access_db"

	def run(self, dispatcher, tracker, domain):

		import sqlite3
		conn = sqlite3.connect('qaCheck.db')
		c = conn.cursor()
		
		given_ml = tracker.get_slot('given_ml')
		default_ml = tracker.get_slot('default_ml_type')
		intent = tracker.latest_message.intent["name"]

		if given_ml is None:
			question_model = intent + " " + default_ml
		else:
			question_model = intent + " " + given_ml

		c.execute('SELECT * FROM q_a WHERE question = :question',{'question':question_model})

		answer = c.fetchall()[0][2]	

		print(answer)

		return [SlotSet('given_ml', None)]

class ActionAcessDataScience:
	def name(self):
		return 'action_access_data_science'

	def run(self, dispatcher, tracker, domain):
		import sqlite3
		conn = sqlite3.connect('qaCheck_data.db')
		c = conn.cursor()

		intent = tracker.latest_message.intent["name"]

		c.execute('SELECT * FROM q_a_data WHERE question = :question',{'question':intent})

		answer = c.fetchall()[0][1]

		print(answer)


		


