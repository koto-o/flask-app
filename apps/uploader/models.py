import os
from datetime import datetime
from ..app import db
from flask_login import current_user


class Image(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(255), nullable=False)  # オリジナルファイル名
    filepath = db.Column(db.String(500), nullable=False)  # 保存パス（例: uploads/uuid_filename.jpg）
    upload_date = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)  # ユーザー関連付け

    user = db.relationship('User', backref=db.backref('images', lazy=True))

    def __repr__(self):
        return f'<Image {self.filename}>'
