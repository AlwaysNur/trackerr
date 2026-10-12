from flask import Flask, request, send_file
import os
from tools.lookup import lookup

app = Flask(__name__, static_folder=os.path.join(os.path.dirname(__file__), '../frontend'))

@app.route('/')
def main():
    return send_file(os.path.join(app.static_folder, 'html/index.html'))

@app.route('/lookup', methods=["POST"])
def lookup_endpoint():
    return lookup(request.form.get('tracking_reference'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)