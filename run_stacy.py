from rasa_core.agent import Agent
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_core.channels.console import ConsoleInputChannel

# Load Dialogue model into agent

def run_stacy_bot(serve_forever = True):
	nlu_interpreter = RasaNLUInterpreter('./models/nlu/default/stacynlu')
	agent = Agent.load('./models/dialogue', interpreter = nlu_interpreter)

	print("Please enter your messages")

	if serve_forever:
		agent.handle_channel(ConsoleInputChannel())

	return agent 

if __name__ == '__main__':
	run_stacy_bot()
