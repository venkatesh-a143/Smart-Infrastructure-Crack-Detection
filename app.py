from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/test')
def test():
    return "Server is running!"

if __name__ == '__main__':
    print("=" * 60)
    print("🚀 CRACK DETECTION APP RUNNING")
    print("=" * 60)
    print("✅ Go to: http://localhost:5000")
    print("=" * 60)
    app.run(debug=True, host='127.0.0.1', port=5000)
