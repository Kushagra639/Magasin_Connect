| [Français 🇫🇷](/FR%20🇨🇵/README_fr.md) | [Español 🇪🇸](/ES%20🇪🇸/README_es.md) | [Italiano 🇮🇹](/IT%20🇮🇹/README_it.md) | [Português 🇵🇹](/PT%20🇵🇹/README_pt.md) | [Deutsch 🇩🇪](/DE%20🇩🇪/README_de.md) | [Nederlands 🇳🇱](/NL%20🇳🇱/README_nl.md) | [Русский 🇷🇺](/RU%20🇷🇺/README_ru.md) | [日本語 🇯🇵](/JP%20🇯🇵/README_jp.md) | [中文 🇨🇳](/CN%20🇨🇳/README_cn.md) | [English 🇬🇧](/README.md)
|-|-|-|-|-|-|-|-|-|-| 

# 🛍️ Magasin Connect

**Magasin Connect**는 `CustomTkinter`를 사용하여 세련되고 현대적인 GUI를 구현한 파이썬 기반의 **매장 관리 시스템**입니다. 이 시스템을 통해 매장 운영자는 재고 관리, 구매 및 판매 거래 기록, 수익 추적 등의 업무를 수행할 수 있으며, 모든 데이터는 MySQL 데이터베이스에 안전하게 저장됩니다.

> 💡 12학년 컴퓨터 과학 프로젝트로 개발되었습니다.

---

## ✨ 기능

- 🔐 **안전한 쇼핑몰 로그인 및 회원가입** (`bcrypt` 비밀번호 해싱 적용)
- 📦 **재고 관리** – 품목 추가, 수정 및 조회
- 📊 **거래 기록** – 실시간 재고 업데이트와 함께 판매 및 구매 내역 기록
- 💰 **손익 계산** – 전체 또는 특정 두 날짜 사이의 손익
- 🎨 **테마 전환** – 커스텀 파스텔 UI가 적용된 라이트 및 다크 모드 지원
- 🛢️ **MySQL 데이터베이스 연동** – 모든 상점 데이터가 영구적으로 저장됩니다.
- 🧹 **데이터 검증 및 오류 처리** – 신뢰성과 사용자 경험 향상

---

## 🛠️ 사용된 기술

| 도구 / 라이브러리       | 목적                                           |
|----------------------|---------------------------------------------------|
| `Python 3`           | 핵심 프로그래밍 언어                         |
| `MySQL`              | 재고 및 거래를 저장하기 위한 데이터베이스      |
| `mysql-connector-python` | Python과 MySQL 연결하기                      |
| `bcrypt`             | 안전한 비밀번호 해싱                           |
| `CustomTkinter`      | Python용 최신 GUI 프레임워크 (테마 기능 포함)    |
| `tkinter.messagebox` | 오류/정보 알림 팝업                   |

---
## ⚙️ 설정
### 의존성 설치
*PowerShell*에서 다음 코드를 실행하여 의존성(dependencies)을 반드시 설치하세요:
```bash
pip install mysql-connector-python bcrypt customtkinter
```

### MySQL 설정
MySQL 서버가 설치되어 있고 실행 중인지 확인하세요.
다음 이름으로 데이터베이스를 생성하세요:
```MySQl
CREATE DATABASE magasin_connect;
```

### 코드를 수정하세요.
- MagasinConnectGUI.py 파일에서 MySQL *user* 이름과 *password*를 업데이트하세요.
```Python
MagasinConnect = SQL.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="magasin_connect"
)
```
- MagasinConnectGUI.py 파일에서 테마 경로를 사용자의 시스템에 맞는 경로로 **업데이트**하세요.
```Python
ctk.set_appearance_mode("system") # Sets the appearance mode to system default (light or dark based on system settings)
ctk.set_default_color_theme("C:/Users/username/Desktop/pastel_theme.json") # Sets the default color theme to a custom pastel theme (given alongside this code), please change the path to the theme file as per your system
```

### 앱을 실행하세요.
```bash
python MagasinConnectGUI.py
```
---

## 👨🏻‍💻 암호
위의 내용을 수정한 후, 코드를 **"VS Code"**나 **"Python IDLE"**에 복사하여 붙여넣고 실행하세요.

| [Code in English](/MagasinConnectGUI.py) 🇬🇧 | [Le Code en Français](FR%20🇨🇵/MagasinConnectGUI_fr.py) 🇫🇷 |
|-|-|

[Theme File](/pastel_theme.json) 🎨

---

## 🙋‍♂️ 작가 -  
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



- 학생, 12학년
- Dr. B. R. Ambedkar SoSE, Plot No. 1, Link Road, Karol Bagh
- Delhi Board of School Education (DBSE)

이 프로젝트는 컴퓨터 과학과 실질적인 응용에 대한 열정으로 만들어졌습니다.

---

## 📜 라이선스

이 프로젝트는 MIT 라이선스에 따라 배포됩니다.

자세한 내용은 LICENSE 파일을 참조하세요.

---

📌 참고 사항:

- ⚠️ 상점 이름을 **"shops"**로 지정하지 마세요(예약된 테이블 이름입니다).
- 🎨 시스템 환경에 따라 코드 내 테마 경로를 수정해야 할 수 있습니다.

---

유용하다고 생각되시면 자유롭게 저장소에 ⭐를 눌러주세요!
