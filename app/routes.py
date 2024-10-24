from flask import Blueprint, render_template, request, redirect, jsonify, flash

# Create a Blueprint for the main routes
main = Blueprint('main', __name__)

@main.route('/', methods=['GET'])
def get_index():
    """Render the index.html template."""
    return render_template('index.html')

@main.route('/api/fileanalyse', methods=['POST'])
def upload_file():
    """Process the uploaded file."""
    if 'upfile' not in request.files:
        flash('No file part')
        return redirect(request.url)

    file = request.files['upfile']

    if file.filename == '':
        flash('No selected file')
        return redirect(request.url)
    
    file_info = {
        'name': file.filename,
        'type': file.content_type,
        'size': len(file.read())
    }

    return jsonify(file_info), 200
