from flask import Flask, render_template, redirect

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    posts = [
        {
            'deal': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer placerat velit ac ex sagittis, id placerat nunc luctus. Fusce placerat nibh id tellus ultrices, ac blandit purus sollicitudin. Pellentesque iaculis est vel diam tempor accumsan. Nam tempor nunc ac sapien fermentum porta.'
        },
        {
            'deal': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer placerat velit ac ex sagittis, id placerat nunc luctus. Fusce placerat nibh id tellus ultrices, ac blandit purus sollicitudin. Pellentesque iaculis est vel diam tempor accumsan. Nam tempor nunc ac sapien fermentum porta.'
        },
        {
            'deal': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer placerat velit ac ex sagittis, id placerat nunc luctus. Fusce placerat nibh id tellus ultrices, ac blandit purus sollicitudin. Pellentesque iaculis est vel diam tempor accumsan. Nam tempor nunc ac sapien fermentum porta.'
        },
        {
            'deal': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer placerat velit ac ex sagittis, id placerat nunc luctus. Fusce placerat nibh id tellus ultrices, ac blandit purus sollicitudin. Pellentesque iaculis est vel diam tempor accumsan. Nam tempor nunc ac sapien fermentum porta.'
        }
    ]
    return render_template('index.html', title='Home', posts=posts)

@app.route('/destinations')
def destinations():
    return

@app.route('/packageDeals')
def packageDeals():
    return

@app.route('/aboutUs')
def aboutUs():
    return

if __name__ == "__main__":
    app.run(debug=True)
