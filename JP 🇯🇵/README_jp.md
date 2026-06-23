| [Français 🇫🇷](/FR%20🇨🇵/README_fr.md) | [Español 🇪🇸](/ES%20🇪🇸/README_es.md) | [Italiano 🇮🇹](/IT%20🇮🇹/README_it.md) | [Português 🇵🇹](/PT%20🇵🇹/README_pt.md) | [Deutsch 🇩🇪](/DE%20🇩🇪/README_de.md) | [Nederlands 🇳🇱](/NL%20🇳🇱/README_nl.md) | [Русский 🇷🇺](/RU%20🇷🇺/README_ru.md) | [English 🇬🇧](/README.md) | [中文 🇨🇳](/CN%20🇨🇳/README_cn.md) | [한국어 🇰🇷](/KR%20🇰🇷/README_kr.md) |
|-|-|-|-|-|-|-|-|-|-| 

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

- サイバーセキュリティ愛好家
- コンピュータサイエンス専攻の学生
- Dr. B.R. Ambedkar SoSE, Karol Bagh 卒業生

<p style="margin: 0; padding: 0;">
  <span style="font-weight: bold; font-size: 1.1em;">フォローはこちらから： </span>
  &nbsp;&nbsp;
  <a href="https://www.linkedin.com/in/kushagraaggarwal639/"
     target="_blank"
     style="display: inline-flex; align-items: center; vertical-align: middle; text-decoration: none;">
    <img src="https://raw.githubusercontent.com/Kushagra639/Magasin_Connect/main/LinkedIn%20Logo.png"
         alt="LinkedIn"
         width="20"
         style="display: block;">
  </a>
  &nbsp;&nbsp;
  <a href="https://www.instagram.com/kushagraaggarwal639/"
     target="_blank"
     style="display: inline-flex; align-items: center; vertical-align: middle; text-decoration: none;">
    <img src="https://raw.githubusercontent.com/Kushagra639/Magasin_Connect/main/Instagram_logo.png"
         alt="Instagram"
         width="20"
         style="display: block;">
  </a>
</p>

このプロジェクトは、コンピュータサイエンスとその実世界への応用への情熱をもって設計されました。

---

## 📜 ライセンス

このプロジェクトはMITライセンスの下でライセンスされています。

詳細については、LICENSEファイルを参照してください。

---

📌 注意事項:

- ⚠️ ショップの名前を **「shops」** にしないでください（予約済みのテーブルです）。
- 🎨 システムによっては、コード内のテーマパスを更新する必要がある場合があります。

---

このリポジトリが役に立ったと思われた場合は、お気軽に⭐を付けてください！
