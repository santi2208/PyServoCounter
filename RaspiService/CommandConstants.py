import json

def GetActionName(key):
	with open('ActionsConfig.json') as json_data_file:
		data = json.load(json_data_file)
		return data[key]['functionName']

def GetGpioPort(key):
	with open('GpioConfigs.json') as json_data_file:
		data = json.load(json_data_file)
		return data[key]['gpioPort']		
		
