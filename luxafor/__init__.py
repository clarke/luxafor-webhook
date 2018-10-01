# https://pro.luxafor.com/webhook-api/

import requests, json, pprint, configparser, os

class Luxafor:
    webhookHost = "https://api.luxafor.com"
    webhookUrls = {
            'color':   webhookHost + "/webhook/v1/actions/solid_color",
            'blink':   webhookHost + "/webhook/v1/actions/blink",
            'pattern': webhookHost + "/webhook/v1/actions/pattern"
    }
    debug = False

    def __init__(self):
        config = configparser.ConfigParser()
        configFile = os.path.join(os.path.expanduser('~'), '.config', 'luxafor.ini')
        config.read(configFile)
        if Luxafor.debug:
            pprint.pprint(configFile)
            pprint.pprint(config.sections())
        self.userId = config['webhook']['userId']

    def sendAction(self, action, params):
        r = requests.post(Luxafor.webhookUrls[action], json=params)
        if Luxafor.debug:
            pprint.pprint(r)
            print("Response: ")
            print(r.json())

    def setColor(self, color):
        # Accepted colors: 'red', 'green', 'yellow', 'blue', 'white', 'cyan', 'magenta', 'custom'
        # params = { 'userId': self.userId, 'actionFields': { 'color': 'custom', 'custom_color': "FF0000" } }
        params = { 'userId': self.userId, 'actionFields': { 'color': color } }
        self.sendAction('color', params)

    def blinkColor(self, color):
        # Accepted colors: 'red', 'green', 'yellow', 'blue', 'white', 'cyan', 'magenta'.
        params = { 'userId': self.userId, 'actionFields': { 'color': 'red' } }
        self.sendAction('blink', params)

    def setPattern(self, pattern):
        # Accepted patterns: 'police', 'traffic lights', 'random 1', 'random 2', 'random 3', 'random 4', 'random 5'.
        # Additional patterns accepted on Windows only: 'rainbow', 'sea', 'white wave', 'synthetic'.
        params = { 'userId': self.userId, 'actionFields': { 'pattern': pattern } }
        self.sendAction('pattern', params)

def main():
    l = Luxafor()
    #l.blinkColor("red")
    # l.setColor("red")
    l.setPattern("police")

if __name__ == "__main__":
    main()
