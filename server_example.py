from flask import Flask,render_template
from flask import request

app = Flask(__name__)

@app.route('/login', methods=['GET','POST','DELETE'])
def login():
    if request.method == 'POST':
        return "POST Request ✓"
    elif request.method == 'DELETE':
        return "DELETE Request ✓"
    else:
        return "GET Request ✓"

  if __name__ == "__main__":
    app.run(debug=True)
