from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired
from wtforms import SubmitField


class UploadForm(FlaskForm):
    file = FileField('画像ファイル', validators=[FileRequired()])
    submit = SubmitField('アップロード')
