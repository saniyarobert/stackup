from flask import Flask, render_template
from datetime import datetime, timedelta

app = Flask(__name__)

@app.route('/')
def home():
    # Fetch the list of events here
    # For now, we will use some hardcoded data
    events = [
        {
            'name': 'Python Workshop',
            'date': datetime(2022, 5, 21),
            'time': '10:00 AM',
            'location': 'Online'
        },
        {
            'name': 'Web Development Meetup',
            'date': datetime(2022, 6, 5),
            'time': '6:00 PM',
            'location': 'Online'
        },
        {
            'name': 'AI and Machine Learning Event',
            'date': datetime(2022, 7, 10),
            'time': '4:00 PM',
            'location': 'Online'
        }
    ]

    # Sort the events by date and time
    events.sort(key=lambda x: (x['date'], x['time']))

    # Return the rendered HTML
    return render_template('index.html', events=events)

if __name__ == '__main__':
    app.run(debug=True)