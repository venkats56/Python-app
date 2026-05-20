# '/api/v1/details'
# '/api/v1/healthz'
from flask import Flask,jsonify
import datetime
import socket
app = Flask(__name__)

@app.route('/api/v1/details')

def details():
    return jsonify({'host': socket.gethostname(),
                    'timestamp': datetime.datetime.now().isoformat(),
                    'message': 'Hello, World!'
    })

@app.route('/api/v1/healthz')
def healthz():
    return jsonify({'status': 'healthy'}),200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)