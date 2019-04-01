from rasa_core.channels import HttpInputChannel
from rasa_core.agent import Agent
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_slack_connector import SlackInput


nlu_interpreter = RasaNLUInterpreter('./models/nlu/default/stacynlu')
agent = Agent.load('./models/dialogue', interpreter = nlu_interpreter)

input_channel = SlackInput('xoxp-418508201168-419094136963-486915435111-2101dbed1aa6011e87935b37da9f4d21',
							'xoxb-418508201168-486915436823-k9XjKIxfbmKoDHMROyWHyD0c',
							'cAv3MW2NqzPTy6HlMPCAmDJc',
							True)

agent.handle_channel(HttpInputChannel(5004, '/', input_channel))
