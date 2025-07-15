from flask import Flask, request, render_template

app = Flask(__name__)

# Route to render the HTML form
@app.route('/')
def home():
    return render_template('my.html')

# Route to receive the form data
@app.route('/search', methods=['POST'])
def search():
    content = request.form['content']  # Get data from the form i phone 7
    cleaned = content.replace(" ", "")  # Remove spaces iphone7
    return render_template('my.html', result=cleaned)

if __name__ == '__main__':
    app.run(debug=True)
