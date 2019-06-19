import configparser

from flask import Flask
from Combination import Combination

app = Flask(__name__)
comb = None
@app.route('/CrossInfra/Combinations',methods=['GET'])
def GetCombinations():
    global comb
    if comb is None:
        comb = Combination()
    return str(comb.InitCombinations())


if __name__ == '__main__':
    config = configparser.ConfigParser()
    config.read('config.ini')
    configDef = config['DEFAULT']
    app.config['SERVER_NAME'] = configDef['url']
    app.run(debug=True)