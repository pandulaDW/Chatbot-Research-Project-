from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

import logging

from rasa_core.agent import Agent
from rasa_core.policies.keras_policy import KerasPolicy
from rasa_core.policies.memoization import MemoizationPolicy
from rasa_core.policies.fallback import FallbackPolicy

if __name__ == '__main__':
	logging.basicConfig(level='INFO')
	
	training_data_file = './Data/stories.md'
	model_path = './models/dialogue'
	
	fallback = FallbackPolicy(nlu_threshold=0.3, core_threshold=0.3, 
                          	fallback_action_name='action_default_fallback')

	agent = Agent('domain.yml', policies = [MemoizationPolicy(max_history = 2), KerasPolicy(), fallback])
	
	agent.train(
			training_data_file,
			epochs = 500,
			batch_size = 10,
			validation_split = 0.2)
			
	# saving the dialogue models 
	agent.persist(model_path)
