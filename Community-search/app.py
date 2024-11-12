from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

# Sample community data
communities = [
    {"id": 1, "name": "Anxiety Support Group", "description": "A safe space for those dealing with anxiety."},
    {"id": 2, "name": "Depression Recovery", "description": "Join us to share experiences and support one another."},
    {"id": 3, "name": "Stress Management Community", "description": "Learn strategies to manage stress effectively."},
    {"id": 4, "name": "Bipolar Support Network", "description": "Connect with others facing bipolar challenges."},
    {"id": 5, "name": "PTSD Survivors Group", "description": "A community for those healing from trauma."},
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/communities', methods=['GET'])
def get_communities():
    query = request.args.get('query', '').lower()
    filtered_communities = [community for community in communities if query in community['name'].lower()]
    return jsonify(filtered_communities)

@app.route('/join_community', methods=['POST'])
def join_community():
    community_id = request.json.get('community_id')
    # Here you would typically handle the logic for joining the community
    return jsonify({"message": f"You have joined the community with ID: {community_id}"}), 200

if __name__ == '__main__':
    app.run(debug=True)