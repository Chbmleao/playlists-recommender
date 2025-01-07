import os
import pickle
from flask import Flask, request, jsonify
from datetime import datetime

class RecommendationRule:
  def __init__(self, songs, score):
    self.score = score
    self.songs = []
    for item in songs:
      self.songs.extend(list(item))
    self.songs = list(set(self.songs))

  def __len__(self):
    return len(self.songs)

  def __repr__(self): 
    return f"Rule(songs={self.songs}, score={self.score})"

def create_app():
  app = Flask(__name__, instance_relative_config=True)

  model_path = '/app/data/playlist_rules.pkl'
  raw_rules = []

  model_last_modified = datetime.fromtimestamp(os.path.getmtime(model_path)).strftime('%Y-%m-%d %H:%M:%S')
  image_version = os.getenv("IMAGE_VERSION", "unknown")

  with open(model_path, 'rb') as f:
    raw_rules = pickle.load(f)

  app.model = [RecommendationRule(rule[:-1], rule[-1]) for rule in raw_rules]
  print("Model loaded successfully")
  print(app.model[0])

  @app.route('/api/recommend', methods=['POST'])
  def recommend():
    if request.method != 'POST':
      return jsonify({"error": "Method not allowed"}), 405
    try: 
      data = request.get_json()
      if not data:
        return jsonify({"error": "No data provided"}), 400
      
      songs = data.get('songs')
      if not songs:
        return jsonify({"error": "No songs provided"}), 400

      recommended_songs = []
      maximum_recommendations = 15
      expected_matches = len(songs)

      # Keep track of already recommended songs to avoid duplicates
      already_recommended = set()


      while len(recommended_songs) < maximum_recommendations and expected_matches > 0:
        for rule in app.model:
          rule_songs = rule.songs

          # Count the number of matches between rule songs and input songs
          matched_songs = sum(1 for song in rule_songs if song in songs)

          # If the rule matches at least the expected number of songs, consider its recommendations
          if matched_songs >= expected_matches:
            for song in rule_songs:
              if song not in songs and song not in already_recommended:
                recommended_songs.append(song)
                already_recommended.add(song)

          # Stop if we already have enough recommendations
          if len(recommended_songs) >= maximum_recommendations:
            break

        expected_matches -= 1

      return jsonify({
        "songs": recommended_songs[:maximum_recommendations], 
        "version": "0.2",
        "model_date": model_last_modified
      }), 200
      
    except Exception as e:
      print(f"Error processing request: {e}")
      return jsonify({"error": "Invalid JSON data"}), 400 

  return app

if __name__ == "__main__":
  app = create_app()
  app.run(debug=False, host='0.0.0.0', port=5000)