from flask import abort, Flask, jsonify, make_response
from flask_pymongo import PyMongo

app = Flask(__name__)
music_data = PyMongo(app, uri="mongodb://localhost:27017/music_data")
music_metadata = music_data.db.music_metadata

@app.route('/api/<string:music_iswc>', methods=['GET'])
def get_music_right_owners(music_iswc):
    if music_iswc[1] == '-':
        music_iswc = ''.join((music_iswc[0], music_iswc[2:-2], music_iswc[-1]))
    right_owners = music_metadata.find_one({'iswc':music_iswc})
    if not bool(right_owners):
        abort(404)
    return jsonify({'right_owners' : right_owners['right_owners']})


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}))

if __name__ == '__main__':
    app.run(debug=True)
