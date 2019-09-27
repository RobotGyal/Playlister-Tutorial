# Playlister
A web application for tracking playlists!

## Frameworks
Built with:
* MongoDB
* PyMongo
* Flask

For full list of dependencies, see `requirements.txt`

## Features

## Code Example
A snippet of heart of the framework setup.
```
...
from pymongo import MongoClient

client = MongoClient()
db = client.Playlister
playlists = db.playlists

app = Flask(__name__)

...

@app.route('/')
def playlists_index():
    """Show all playlists."""
    return render_template('playlists_index.html', playlists=playlists.find())
...
```

## Installation

## How to Use