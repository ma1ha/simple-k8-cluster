from flask import Flask, jsonify
app = Flask(__name__)
@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status":"ok"}), 200
@app.route('/users', methods=['GET'])
def get_users():    
    users=[
        {"id":1, "name":"Hisoka"},
        {"id":2, "name":"Gon"},
        {"id":1, "name":"Gojo"},
        
    ]
    return jsonify(users), 200
if __name__ == '__main__':
    app.run(port=5000, host='0.0.0.0')   