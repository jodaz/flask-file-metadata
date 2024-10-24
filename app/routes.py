from flask import Blueprint, render_template, request, redirect, url_for, flash

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

    # Save the file or process it as needed
    # For example, you can save it to a specific directory
    # file.save(f'uploads/{file.filename}')

    flash('File successfully uploaded')
    return redirect(url_for('main.get_index'))
