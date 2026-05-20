# Flaskアプリ開発環境の設定

以下、断りが無ければ、アプリのプロジェクトフォルダで操作することを想定する。

## 参考資料

https://github.com/ml-flaskbook/flaskbook


## WindowsでのPython仮想環境の作成

### 手動インストールしたPythonの場合

Windows PowerShellの設定
```
$ PowerShell Set-ExecutionPolicy RemoteSigned CurrentUser
```

"flask"という名前の仮想環境の作成
```
$ mkdir flask-app
$ cd flask-app
$ py -m venv flask
```

仮想環境の有効化
```
$ flask\Script\Activate.ps1
```

仮想環境の無効化
```
deactivate
```

### Anacondaの場合

"flask"という名前の仮想環境を作成

```
$ mkdir flask-app
$ cd flask-app
$ conda create -n flask anaconda
```

仮想環境の有効化
```
$ conda activate flask
```

仮想環境の無効化
```
$ conda deactivate
```


## flaskその他のインストール

```
(flask) $ pip install -r requirements.txt
```




## .env作成

.envがプロジェクトルートに存在しない場合は作成し、以下を書き込む
```
FLASK_APP=apps.app:create_app
FLASK_ENV=development
```

## データベース初期化

```
(flask) $ flask db init
(flask) flask db migrate -m "Initial migration."
(flask) flask db upgrade
```

## アプリ起動

```
(flask) $ flask run --host=0.0.0.0 --debug
```

## データベース削除

migrations と local.sqlite を削除してから初期化手順を再実行する．


--

