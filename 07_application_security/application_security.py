from flask import Flask, request, render_template_string
import html

app = Flask(__name__)

@app.route('/')
def index():
    return '''
    <form method="post" action="/submit">
    <input type="text" name="user_input">
    <input type="submit"value=”Submit”>
    </form>
    '''
    
@app.route('/submit', methods=['POST'])
def submit():
    user_input = request.form['user_input']
    sanitized_input = html.escape(user_input) # Sanitize user input
    return render_template_string('<p>Your input: {{ input }}</p>', input=sanitized_input)
 
 
if __name__ == '__main__':
    app.run(debug=True)
