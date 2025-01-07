import pickle
import pandas as pd
from fpgrowth_py import fpgrowth

def create_model():
  print("Importing dataset...")
  dataset_path = '/app/data/spotify.csv'
  data = pd.read_csv(dataset_path)
  print("Shape:")
  print(data.shape)
  print()

  print("Columns:")
  print(data.columns)
  print()

  print("Info:")
  print(data.info())
  print()

  playlists_dict = data.groupby('pid')['track_name'].apply(list).to_dict()
  playlists = list(playlists_dict.values())
  print(len(playlists))
  print(playlists[0])

  freq_item_set, rules = fpgrowth(playlists, minSupRatio=0.05, minConf=0.1)
  print(len(rules))

  with open('/app/data/playlist_rules.pkl', 'wb') as file:
    pickle.dump(rules, file)

if __name__ == "__main__":
  print("Starting script...")
  create_model()