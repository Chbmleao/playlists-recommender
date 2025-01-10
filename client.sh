wget --server-response \
    --output-document response.json \
    --header='Content-Type: application/json' \
    --post-data '{"songs": ["HUMBLE.", "DNA.", "goosebumps"]}' \
    http://10.43.23.218:18485/api/recommend