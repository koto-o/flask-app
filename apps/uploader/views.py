import os
import uuid
from flask import Blueprint, render_template, request, redirect, url_for, flash, send_from_directory, current_app
from flask_login import login_required, current_user
from werkzeug.utils import secure_filename
from ..app import db
from .models import Image
from .forms import UploadForm


uploader = Blueprint('uploader', __name__, template_folder='templates/uploader', static_folder='static')

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
MAX_FILE_SIZE = 5 * 1024 * 1024  # 5MB


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@uploader.route('/upload', methods=['GET', 'POST'])
@login_required
def upload():
    form = UploadForm()  # フォームインスタンスを作成
    if form.validate_on_submit():  # POSTかつバリデーション成功時
        file = form.file.data
        if file and allowed_file(file.filename):
            if file.content_length > MAX_FILE_SIZE:
                flash('ファイルサイズが大きすぎます（5MB以下）', 'error')
                return redirect(request.url)
            filename = secure_filename(file.filename)
            unique_filename = f"{uuid.uuid4()}_{filename}"
            filepath = os.path.join(current_app.root_path, 'static', 'uploads', unique_filename)
            os.makedirs(os.path.dirname(filepath), exist_ok=True)
            file.save(filepath)

            # DB保存
            image = Image(filename=filename, filepath=f'uploads/{unique_filename}', user_id=current_user.id)
            db.session.add(image)
            db.session.commit()
            flash('画像をアップロードしました', 'success')
            return redirect(url_for('uploader.list_images'))
        else:
            flash('許可されていないファイルタイプです', 'error')
    return render_template('upload.html', form=form)


@uploader.route('/list')
@login_required
def list_images():
    images = Image.query.filter_by(user_id=current_user.id).order_by(Image.upload_date.desc()).all()
    return render_template('list.html', images=images)


@uploader.route('/view/<int:image_id>')
@login_required
def view_image(image_id):
    image = Image.query.filter_by(id=image_id, user_id=current_user.id).first_or_404()
    return render_template('view.html', image=image)


# 画像ファイルの直接アクセス（静的ファイルとして）
@uploader.route('/uploads/<filename>')
@login_required
def uploaded_file(filename):
    return send_from_directory(os.path.join(current_app.root_path, 'static', 'uploads'), filename)
