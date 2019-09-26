from flask import Flask, render_template

app = Flask(__name__)

# #HOME
# @app.route('/')
# def index():
#     return render_template("home.html", msg="Flask is cool")

#MOCK ARRAY OF PROJECT
playlists = [
    { 'title': 'Cat Videos', 'description': 'Cats acting weird' },
    { 'title': '80\'s Music', 'description': 'Don\'t stop believing!' },
    { 'title': 'Jazz Music', 'description': 'Trumpets, Horns, and Swag!'}
]

#ROOT
@app.route('/')
def playlists_index():
    """Show all playlists."""
    return render_template('playlists_index.html', playlists=playlists)

if __name__ == '__main__':
    app.run(debug=True)