| [Français 🇫🇷](/FR%20🇨🇵/README_fr.md) | [Español 🇪🇸](/ES%20🇪🇸/README_es.md) | [Italiano 🇮🇹](/IT%20🇮🇹/README_it.md) | [English 🇬🇧](/README.md) | [Deutsch 🇩🇪](/DE%20🇩🇪/README_de.md) | [Nederlands 🇳🇱](/NL%20🇳🇱/README_nl.md) | [Русский 🇷🇺](/RU%20🇷🇺/README_ru.md) | [日本語 🇯🇵](/JP%20🇯🇵/README_jp.md) |
|-|-|-|-|-|-|-|-| 

# 🛍️ Magasin Connect

O **Magasin Connect** é um **sistema de gestão de lojas** desenvolvido em Python, com uma interface gráfica (GUI) moderna e atraente criada com `CustomTkinter`. Permite aos comerciantes gerir o stock, registar transações de compra e venda e acompanhar os lucros — tudo isto armazenando os dados de forma segura numa base de dados MySQL.

> 💡 Desenvolvido como um projeto de Ciência da Computação para o 12º ano.

---

## ✨ Funcionalidades

- 🔐 **Login e Registo Seguro na Loja** (com hash de password via `bcrypt`)
- 📦 **Gestão de Stocks** – Adicione, edite e visualize artigos
- 📊 **Registo de Transações** – Registe as vendas/compras com atualização de stock em tempo real.
- 💰 **Cálculo de Resultados** – Total ou entre duas datas quaisquer
- 🎨 **Alternância de Tema** – Suporte aos modos claro e escuro com uma interface personalizada em tons pastel.
- 🛢️ **Integração com Base de Dados MySQL** – Todos os dados da loja são armazenados de forma persistente.
- 🧹 **Validação de Dados e Tratamento de Erros** – Para maior fiabilidade e melhor experiência de utilização

---

## 🛠️ Tecnologias Utilizadas

| Ferramenta / Biblioteca  | Finalidade                                               |
|--------------------------|----------------------------------------------------------|
| `Python 3`               | Linguagem de programação principal                       |
| `MySQL`                  | Base de dados para armazenar stock e transações          |
| `mysql-connector-python` | Ligue o Python ao MySQL                                  |
| `bcrypt`                 | Hashing de palavra-passe seguro                          |
| `CustomTkinter`          | Framework GUI moderno para Python (com suporte de temas) |
| `tkinter.messagebox`     | Mensagens de erro/informação pop-up                      |

---
## ⚙️ Configurar
### Instalar dependências
Certifique-se de que instala as dependências executando o seguinte código no *PowerShell*:
```bash
pip install mysql-connector-python bcrypt customtkinter
```

### Configurar o MySQL
Certifique-se de que tem o MySQL Server instalado e em execução.
Crie uma base de dados chamada:
```MySQl
CREATE DATABASE magasin_connect;
```

### Faça alterações no código
- **Atualize** o seu *user* nome e *password* do MySQL no ficheiro MagasinConnectGUI.py
```Python
MagasinConnect = SQL.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="magasin_connect"
)
```
- **Actualize** o caminho do tema no ficheiro MagasinConnectGUI.py para o caminho correspondente no seu sistema.
```Python
ctk.set_appearance_mode("system") # Sets the appearance mode to system default (light or dark based on system settings)
ctk.set_default_color_theme("C:/Users/username/Desktop/pastel_theme.json") # Sets the default color theme to a custom pastel theme (given alongside this code), please change the path to the theme file as per your system
```

### Execute a aplicação
```bash
python MagasinConnectGUI.py
```
---

## 👨🏻‍💻 Código
Copie e cole o código no **VS Code** ou no **Python IDLE** e execute-o após efetuar as alterações acima mencionadas.

| [Code in English](/MagasinConnectGUI.py) 🇬🇧 | [Le Code en Français](FR%20🇨🇵/MagasinConnectGUI_fr.py) 🇫🇷 |
|-|-|

[Theme File](/pastel_theme.json) 🎨

---

## 🙋‍♂️ Autor -  
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



- Aluno(a), 12º ano
- Dr. B.R. Ambedkar SoSE, Plot No. 1, Link Road, Karol Bagh
- Delhi Board of School Education (DBSE)

Este projeto foi desenvolvido com paixão pela Ciência da Computação e por aplicações no mundo real.

---

## 📜 Licença

Este projeto está licenciado sob a Licença MIT.

Consulte o ficheiro LICENSE para obter detalhes.

---

📌 Notas :

- ⚠️ Não nomeie a sua loja como **"shops"** (é uma tabela reservada).
- 🎨 O caminho do tema no código pode necessitar de ser atualizado, dependendo do seu sistema.

---

Sinta-se à vontade para dar uma estrela (⭐) ao repositório se o achar útil!
