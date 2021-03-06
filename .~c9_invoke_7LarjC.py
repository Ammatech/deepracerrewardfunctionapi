import urllib.request
import urllib.parse
import json

def reward_function(params):
    url = 'https://rz8tp0clzi.execute-api.us-east-1.amazonaws.com/Prod/reward/'
    query_string = urllib.parse.urlencode({"json":json.dumps(params)})  
    url = url + "?" + query_string  
    with urllib.request.urlopen( url ) as response:     
        response_text = response.read().decode('utf-8')
        result = json.loads(response_text)
        return float(result["reward"])