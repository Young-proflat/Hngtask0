#import libraries
from flask import Flask, jsonify
from datetime import datetime
from flask_cors import CORS

# initialize the Flask app and enable CORS for all routes  
app = Flask(__name__)
CORS(app)  

# define the API endpoint with GET method
@app.route('/api', methods=['GET'])
def api():
   resp = {
       "email": "olatunbosunlateef6@gmail.com",
       "current_datetime": datetime.now().isoformat(),
       "github_url": "https://github.com/Young-proflat/HNGTask-0"
   }
   return jsonify(resp)

if __name__ == '__main__':
   app.run(debug=True)
