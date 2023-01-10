# パスワードをコピーするやつ
## 概要
学校の共用PCでポータルサイトに接続しようとすると、毎回手動で情報を入力する必要がある。<br>
少しでも楽をするためのプログラムです。

## 動作環境

* Windows10で作成
  * Windows10でのみ動作検証
* Python3.10
    * [Tkinter](https://docs.python.org/ja/3/library/tkinter.html)
    * [OS](https://docs.python.org/ja/3/library/os.html)
    * [Subprocess](https://docs.python.org/ja/3/library/subprocess.html)
    * [JSON](https://docs.python.org/ja/3/library/json.html) 

## 使い方
1. JSONファイルの確認
    1. 同梱のJSONファイルをダウンロードする
    2. `StudentID`・`PassWord`・`MailAddress`を入力し保存
2. Cliper.pyの起動
3. `1・選択`ボタンから上記のJSONファイルを選択
4. `2・設定読み込み`をクリックし、状態が`準備完了`に変化したのを確認する
5. コピーしたい項目をクリックする

## 変数の管理


## 参考
[【コマンドプロンプト】クリップボードの読み込みと書き出し](https://syutaku.blog/win-cmd-clipboard/)（閲覧日2023年1月10日）<br>
[(tkinter)ボタンをクリックすると、ラベルの文字が変わる](https://takajaramin.com/2020/02/button_click_label_change/#i-9)（閲覧日2023年1月10日）<br>
[Pythonでtry exceptの書き方と、エラー内容の取得方法](https://symfoware.blog.fc2.com/blog-entry-873.html)（閲覧日2023年1月10日）<br>
