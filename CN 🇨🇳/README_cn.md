| [Français 🇫🇷](/FR%20🇨🇵/README_fr.md) | [Español 🇪🇸](/ES%20🇪🇸/README_es.md) | [Italiano 🇮🇹](/IT%20🇮🇹/README_it.md) | [Português 🇵🇹](/PT%20🇵🇹/README_pt.md) | [Deutsch 🇩🇪](/DE%20🇩🇪/README_de.md) | [Nederlands 🇳🇱](/NL%20🇳🇱/README_nl.md) | [Русский 🇷🇺](/RU%20🇷🇺/README_ru.md) | [日本語 🇯🇵](/JP%20🇯🇵/README_jp.md) | [English 🇬🇧](/README.md) |  [한국어 🇰🇷](/KR%20🇰🇷/README_kr.md) |
|-|-|-|-|-|-|-|-|-|-| 

# 🛍️ Magasin Connect

**Magasin Connect** 是一款基於 Python 的**店鋪管理系統**，採用 `CustomTkinter` 建構了美觀且現代的圖形使用者介面（GUI）。它支援店主管理庫存、記錄進銷交易並追蹤利潤，同時將資料安全地儲存在 MySQL 資料庫中。

> 💡 作為高二（12年級）電腦科學專案開發。

---

## ✨ 功能

- 🔐 **安全的商店登入與註冊**（使用 `bcrypt` 密碼雜湊）
- 📦 **庫存管理** – 新增、編輯和查看商品
- 📊 **交易記錄** – 記錄銷售/採購，並即時更新庫存
- 💰 **盈虧計算** – 總計或任兩個日期之間
- 🎨 **主題切換** – 支援淺色與深色模式，採用客製化的柔和色調（Pastel）UI
- 🛢️ **MySQL 資料庫整合** – 所有商店資料均實現持久化存儲
- 🧹 **資料驗證與錯誤處理** – 提升系統可靠性與使用者體驗

---

## 🛠️ 使用的技術

| 工具 / 庫       | 目的                                           |
|----------------------|---------------------------------------------------|
| `Python 3`           | 核心程式語言                         |
| `MySQL`              | 用於儲存庫存和交易資料的資料庫      |
| `mysql-connector-python` | 連結 Python 與 MySQL                      |
| `bcrypt`             | 安全的密碼哈希處理                           |
| `CustomTkinter`      | 適用於 Python 的現代 GUI 框架（支援主題功能）    |
| `tkinter.messagebox` | 錯誤/訊息彈出提示                   |

---
## ⚙️ 設定流程
### 安裝依賴項
請務必在 *PowerShell* 中執行以下程式碼來安裝相依性：
```bash
pip install mysql-connector-python bcrypt customtkinter
```

### 設定 MySQL
請確保已安裝並執行 MySQL Server。
建立一個名為…的資料庫：
```MySQl
CREATE DATABASE magasin_connect;
```

### 修改程式碼
- 在 `MagasinConnectGUI.py` 檔案中更新您的 MySQL *user* 名稱和 *password*。
```Python
MagasinConnect = SQL.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="magasin_connect"
)
```
- 在 `MagasinConnectGUI.py` 檔案中，將主題路徑**更新**為您系統中的實際路徑。
```Python
ctk.set_appearance_mode("system") # Sets the appearance mode to system default (light or dark based on system settings)
ctk.set_default_color_theme("C:/Users/username/Desktop/pastel_theme.json") # Sets the default color theme to a custom pastel theme (given alongside this code), please change the path to the theme file as per your system
```

### 運行應用程式
```bash
python MagasinConnectGUI.py
```
---

## 👨🏻‍💻 程式碼
將程式碼**複製**並**貼上**到 **VS Code** 或 **Python IDLE** 中，在進行上述修改後運行它。

| [Code in English](/MagasinConnectGUI.py) 🇬🇧 | [Le Code en Français](FR%20🇨🇵/MagasinConnectGUI_fr.py) 🇫🇷 |
|-|-|

[Theme File](/pastel_theme.json) 🎨

---

## 🙋‍♂️ Author -  
<p style="margin: 0; padding: 0;">
  <span style="font-weight: bold; font-size: 1.1em;">Kushagra Aggarwal</span>
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



- 學生，12年級
- Dr. B. R. Ambedkar SoSE, Plot No. 1, Link Road, Karol Bagh
- Delhi Board of School Education (DBSE)

該項目是出於對計算機科學及實際應用的熱情而構建的。

---

## 📜 執照

本專案採用 MIT 許可證。

詳情請參閱 LICENSE 文件。

---

📌 筆記 :

- ⚠️ 請勿將您的商店命名為 **"shops"**（這是一個保留的資料庫表名）。
- 🎨 程式碼中的主題路徑可能需要根據您的系統進行更新。

---

如果您覺得這個倉庫有用，歡迎給它點個 ⭐！
