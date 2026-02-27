from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory storage
students = []
next_id = 1


# ── CREATE ──────────────────────────────────────────────────────────────────
@app.route('/students', methods=['POST'])
def create_student():
    global next_id
    data = request.get_json()

    if not data or 'name' not in data or 'age' not in data or 'course' not in data:
        return jsonify({'error': 'name, age, and course are required'}), 400

    student = {
        'id': next_id,
        'name': data['name'],
        'age': data['age'],
        'course': data['course']
    }
    students.append(student)
    next_id += 1
    return jsonify(student), 201


# ── READ ALL ────────────────────────────────────────────────────────────────
@app.route('/students', methods=['GET'])
def get_students():
    return jsonify(students), 200


# ── READ ONE ────────────────────────────────────────────────────────────────
@app.route('/students/<int:student_id>', methods=['GET'])
def get_student(student_id):
    student = next((s for s in students if s['id'] == student_id), None)
    if student is None:
        return jsonify({'error': 'Student not found'}), 404
    return jsonify(student), 200


# ── UPDATE ──────────────────────────────────────────────────────────────────
@app.route('/students/<int:student_id>', methods=['PUT'])
def update_student(student_id):
    student = next((s for s in students if s['id'] == student_id), None)
    if student is None:
        return jsonify({'error': 'Student not found'}), 404

    data = request.get_json()
    student['name']   = data.get('name',   student['name'])
    student['age']    = data.get('age',    student['age'])
    student['course'] = data.get('course', student['course'])
    return jsonify(student), 200


# ── DELETE ──────────────────────────────────────────────────────────────────
@app.route('/students/<int:student_id>', methods=['DELETE'])
def delete_student(student_id):
    global students
    student = next((s for s in students if s['id'] == student_id), None)
    if student is None:
        return jsonify({'error': 'Student not found'}), 404

    students = [s for s in students if s['id'] != student_id]
    return jsonify({'message': f'Student {student_id} deleted successfully'}), 200


if __name__ == '__main__':
    app.run(debug=True, port=5000)