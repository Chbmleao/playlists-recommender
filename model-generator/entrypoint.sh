#!/bin/bash

echo "Starting entrypoint"
git clone https://github.com/Chbmleao/playlists-recommender ./tmp/repo;

cp ./tmp/repo/data/spotify.csv ./data/spotify.csv;
echo "Dataset updated";

python3 app.py;
echo "Model updated";
