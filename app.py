from flask import Flask, jsonify, request
import pickle
import pandas as pd

app = Flask(__name__)

# Load the trained model
with open('model/recommendation_model.pkl', 'rb') as model_file:
    recommendation_model = pickle.load(model_file)

# Load the user-item interaction matrix
user_item_matrix = pd.read_pickle('model/user_item_matrix.pkl')

@app.route('/recommend', methods=['POST'])
def recommend():
    user_id = request.json.get('user_id')
    
    if user_id is None:
        return jsonify({'error': 'user_id is required'}), 400

    # Implement your recommendation logic here
    # Example logic (this is a placeholder; replace with your actual recommendation method):
    recommended_products = recommendation_model.recommend(user_id)  # Modify as needed
    
    return jsonify({'recommended_products': recommended_products})

if __name__ == '__main__':
    app.run(debug=True)
