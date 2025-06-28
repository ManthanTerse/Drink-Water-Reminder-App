#Project 04 : Drink Water Reminder 

from flask import Flask, render_template
import time
from plyer import notification


while(True):
    print("Please sip some water!")
    notification.notify(title="Drink Water",
             message="You have to take a sip of water")
    time.sleep(60 * 60)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

