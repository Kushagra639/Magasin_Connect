| [Français 🇫🇷](/FR%20🇨🇵/README_fr.md) | [Español 🇪🇸](/ES%20🇪🇸/README_es.md) | [Italiano 🇮🇹](/IT%20🇮🇹/README_it.md) | [Deutsch 🇩🇪](/DE%20🇩🇪/README_de.md) | [Nederlands 🇳🇱](/NL%20🇳🇱/README_nl.md) | [Русский 🇷🇺](/RU%20🇷🇺/README_ru.md) | [English 🇬🇧](/README.md) |
|-|-|-|-|-|-|-| 
# 🛍️ Magasin Connect

**Magasin Connect** は、`CustomTkinter` で開発された、洗練されたモダンなグラフィカルユーザーインターフェースを備えた Python ベースの **店舗管理システム** です。店舗は在庫管理、売買取引の記録、利益の追跡が可能で、データは MySQL データベースに安全に保存されます。

> 💡 最終学年の IT プロジェクトの一環として開発されました。

---

## ✨ 機能

- 🔐 **セキュアなストアログインと登録** (`bcrypt` パスワードハッシュを使用)
- 📦 **在庫管理** – 商品の追加、編集、表示
- 📊 **取引記録** – リアルタイムの在庫更新で売上/購入を記録
- 💰 **損益計算** – 合計または2つの日付間の計算
- 🎨 **テーマ切り替え** – カスタムパステルUIでライトモードとダークモードをサポート
- 🛢️ **MySQLデータベース統合** – すべてのストアデータは永続的に保存されます
- 🧹 **データ検証とエラー処理** – 最適な信頼性とユーザーエクスペリエンスを実現

---

## 🛠️ 使用技術

| ツール / ライブラリ | 目的 |
|-------------------------|---------------------------------------------------------------|
| `Python 3` | 主要プログラミング言語 |
| `MySQL` | 在庫と取引を保存するためのデータベース |
| `mysql-connector-python` | Python から MySQL への接続 |
| `bcrypt` | 安全なパスワードハッシュ |
| `CustomTkinter` | 最新の Python GUI (テーマ付き) |
| `tkinter.messagebox` | エラー / 情報ポップアップメッセージ |

---
## ⚙️ 設定
### 依存関係のインストール
*powershell* で次のコードを実行して、依存関係がインストールされていることを確認してください。
```bash
pip install mysql-connector-python bcrypt customtkinter
```

### MySQL の設定
MySQL Server がインストールされ、実行されていることを確認してください。次の名前のデータベースを作成します:
```MySQL
CREATE DATABASE magasin_connect;
```

### コードを変更します
- MagasinConnectGUI.py ファイル内の MySQL の *ユーザー名* と *パスワード* を**更新**してください。
```Python
MagasinConnect = SQL.connect(
    host="localhost",
    user="root",
    password="your password",
    database="magasin_connect"
)
```

- MagasinConnectGUI.py ファイル内のテーマパスをシステムのパスに**更新**してください。
```Python
ctk.set_appearance_mode("system") # 外観モードをシステムのデフォルト（システム設定に基づいてライトまたはダーク）に設定します。
ctk.set_default_color_theme("C:/Users/username/Desktop/pastel_theme.json") # デフォルトのカラーテーマを、このコードと一緒に指定されたカスタムパステルテーマに設定します。システムに合わせてテーマファイルへのパスを変更してください。
```

### アプリケーションを実行する
```bash
python MagasinConnectGUI.py
```
---

## 👨🏻‍💻 コード
上記の変更を行った後、コードをコピーして **「VS Code」** または **「Python IDLE」** に貼り付け、実行するだけです。
| [Code in English](/MagasinConnectGUI.py) 🇬🇧 | [Le Code en Français](FR%20🇨🇵/MagasinConnectGUI_fr.py) 🇫🇷 |
|-|-|

[テーマファイル](/pastel_theme.json) 🎨

---

## 🙋‍♂️ 作者 - 
Kushagra Aggarwal (クシャグラ・アガーワル)
- 12年生
- Dr. B. R. Ambedkar SoSE、Plot no. 1、Link Road、Karol Bagh
- Delhi Board of School Education (DBSE)

このプロジェクトは、コンピュータサイエンスとその実世界への応用への情熱をもって設計されました。

---

📄 ライセンス:

このプロジェクトは教育目的での使用にオープンです。

その他の用途については、作者までご連絡ください。

---

📌 注意事項:

- ⚠️ ショップの名前を「shops」にしないでください（予約済みのテーブルです）。
- 🎨 システムによっては、コード内のテーマパスを更新する必要がある場合があります。

---

このリポジトリが役に立ったと思われた場合は、お気軽に⭐を付けてください！
