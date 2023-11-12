from flask import Blueprint, request, render_template, flash, redirect, url_for
from werkzeug.utils import secure_filename
import os
from .utils import pdf_to_text, summarize_paper

bp = Blueprint('chat', __name__, url_prefix='/')

@bp.route('/', methods=('GET', 'POST'))
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']

        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)

        if file and file.filename.endswith('.pdf'):
            filename = secure_filename(file.filename)
            upload_folder = 'uploads'
            if not os.path.exists(upload_folder):
                os.makedirs(upload_folder, exist_ok=True)  # uploads ディレクトリがなければ作成
            file_path = os.path.join(upload_folder, filename)
            file.save(file_path)

            paper_text = pdf_to_text(file_path)
            summary = summarize_paper(paper_text)

            return render_template('summary.html', summary=summary)

    return render_template('index.html')
