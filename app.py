from flask import Flask

# Create an instance of the Flask class
app = Flask(__name__)

# Define a route for the root URL '/'
@app.route('/')
def hello():
    return 'Hello, World 2!'

# Define a route for '/about'
@app.route('/about')
def about():
    return 'This is a simple Flask web application.'

# Run the application if the script is executed directly
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)

