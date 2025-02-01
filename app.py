#import libraries
from flask import Flask, jsonify
from datetime import datetime 
from flask_cors import CORS

#initialize the flask instance
app = Flask(__name__)
CORS(app)

email = "olatunbosunlateef6@gmail.com"
github_url = "https://github.com/Young-proflat/Hngtask0/"

@app.route('/', methods=['GET'])
@app.route('/api', methods=['GET'])

def res ():
    response = {
        "email": email,
        "current_date": datetime.now().isoformat(),
        "github_url": github_url
            }
    return jsonify(response)


if __name__ == "__main__":
    app.run(debug=True)
