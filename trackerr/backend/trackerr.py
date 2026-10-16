from flask import Flask, render_template, request, redirect, url_for
import os
from tools.lookup import lookup
from tools.db import init_db, add_package, show_packages, delete_package

app = Flask(__name__, static_folder=os.path.join(os.path.dirname(__file__), '../frontend'),template_folder=os.path.join(os.path.dirname(__file__), '../templates'))

@app.route('/')
def home():
    return render_template("index.html", packages=show_packages())

@app.route('/api/lookup', methods=["POST"])
def lookup_api_endpoint():
    return lookup(request.form.get('tracking_reference'))

@app.route('/api/package/add', methods=["POST"])
def add_package_endpoint():
    add_package(request.form.get('tracking_reference'),request.form.get('description'))
    return redirect(url_for("home"), code="303")

@app.route('/api/delete', methods=["DELETE"])
def delete_package_endpoint():
    delete_package(request.form.get("id"))
    

if __name__ == '__main__':
    init_db()
    app.run(debug=True, host='0.0.0.0', port=5000)