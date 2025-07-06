from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    """
    トップページを表示します。
    """
    return render_template('index.html')

@app.route('/about') # 新しいルートを追加
def about():
    """
    概要ページを表示します。
    """
    return render_template('about.html')

if __name__ == '__main__':
    # ポート5001でアプリケーションを起動します
    # debug=True は開発用です。本番環境ではFalseに設定してください。
    app.run(host="0.0.0.0",debug=False, port=5001)
