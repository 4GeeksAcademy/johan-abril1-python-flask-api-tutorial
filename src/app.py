from flask import Flask, jsonify, request

app = Flask(__name__)

todos = [
    {
        "label": "Sample",
        "done": True
    }
]


@app.route('/todos', methods=['GET'])
def get_todos():
    return jsonify(todos), 200


@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.get_json()
    todos.append(request_body)
    return jsonify(todos), 200


@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    if position >= 0 and position < len(todos):
        todos.pop(position)

    return jsonify(todos), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3245, debug=True)