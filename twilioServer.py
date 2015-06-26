from flask import Flask, request, redirect
import twilio.twiml
import os
 
app = Flask(__name__)

callers = {
	"+12484210373": "Michael",
	"+12489122122": "Sean",
	"+12484106895": "Evan",
	"+12318841844": "Kyle",
	"+15866046301": "Max",
	"+19062215732": "Gianna",
}
 
@app.route("/", methods=['GET', 'POST'])
def received_text():
    """Respond to incoming calls with a simple text message."""
    
    from_number = request.values.get('From', None)
    content = request.values.get('Body', None)
    os.system("sudo python ./youtubeParser.py '" + content + "'")

    if from_number in callers:
	message = "Thanks " + callers[from_number] + "! Song: " + content + " has been queued!"
    else:
	message = "Thanks! Song: " + content + " has been queued!"
    resp = twilio.twiml.Response()
    resp.message(message)
    return str(resp)
 
if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')
