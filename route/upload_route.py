from flask import request, jsonify
import server
import os


@server.app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify(
            status="failed1"
        )
    file = request.files['file']

    if file.filename == '':
        return jsonify(
            status="failed2"
        )
    else:
        archivo = file.filename
        file.save(os.path.join(server.app.config['UPLOAD_FOLDER'], archivo))
        return jsonify(
            status='Success'
        )
