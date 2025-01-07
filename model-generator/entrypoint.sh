#!/bin/bash

echo "Starting entrypoint"
git clone https://github.com/Chbmleao/playlists-recommender ./tmp/repo &&
if ! cmp -s ./tmp/repo/data/spotify.csv ./data/spotify.csv; then
  cp ./tmp/repo/data/spotify.csv ./data/spotify.csv;
  echo "Dataset updated";

  python3 app.py;
  echo "Model updated";
else
  echo "Dataset is already up-to-date";
fi

echo "Finishing entrypoint"