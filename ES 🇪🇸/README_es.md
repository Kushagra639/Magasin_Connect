| [Français 🇫🇷](FR%20🇨🇵/README_fr.md) | [English 🇬🇧](/README.md) | [Italiano 🇮🇹](IT%20🇮🇹/README_it.md) | [Deutsch 🇩🇪](DE%20🇩🇪/README_de.md) | [Nederlands 🇳🇱](NL%20🇳🇱/README_nl.md) | [Русский 🇷🇺](RU%20🇷🇺/README_ru.md) | [日本 🇯🇵](JP%20🇯🇵/README_jp.md) |
|-|-|-|-|-|-|-| 
# 🛍️ Magasin Connect

**Magasin Connect** es un **sistema de gestión de tiendas** basado en Python con una interfaz gráfica de usuario atractiva y moderna, desarrollada con `CustomTkinter`. Permite a los comerciantes gestionar su inventario, registrar transacciones de compra y venta, y hacer un seguimiento de las ganancias, todo ello almacenando los datos de forma segura en una base de datos MySQL.

> 💡 Desarrollado como proyecto de informática de 12º grado.

---

## ✨ Características

- 🔐 **Inicio de sesión y registro seguro en la tienda** (con hash de contraseña `bcrypt`)
- 📦 **Gestión de inventario**: añade, edita y visualiza artículos
- 📊 **Registro de transacciones**: registra las ventas/compras con actualizaciones de stock en tiempo real
- 💰 **Cálculo de ganancias/pérdidas**: total o entre dos fechas
- 🎨 **Cambio de tema**: compatible con los modos claro y oscuro con una interfaz de usuario personalizada en tonos pastel
- 🛢️ **Integración con base de datos MySQL**: todos los datos de la tienda se almacenan de forma persistente
- 🧹 **Validación de datos y gestión de errores**: para una mayor fiabilidad y experiencia de usuario

---

## 🛠️ Tecnologías utilizadas

| Herramienta / Biblioteca  | Propósito                                               |
|---------------------------|---------------------------------------------------------|
| `Python 3`                | Lenguaje de programación principal                      |
| `MySQL`                   | Base de datos para almacenar inventario y transacciones |
| `mysql-connector-python`  | Conectar Python con MySQL                               |
| `bcrypt`                  | Hash seguro de contraseñas                              |
| `CustomTkinter`           | Framework GUI moderno para Python (con temas)           |
| `tkinter.messagebox`      | Mensajes emergentes de errores/información              |

---
## ⚙️ Configuración
### Instalar dependencias
Asegúrate de instalar las dependencias ejecutando el siguiente código en *PowerShell*:
```bash
pip install mysql-connector-python bcrypt customtkinter
```

### Configurar MySQL
Asegúrate de tener el servidor MySQL instalado y en ejecución. Cree una base de datos llamada:
```MySQl
CREATE DATABASE magasin_connect;
```

### Realizar cambios en el código
**Actualizar** tu *usuario* y *contraseña* de MySQL en el archivo MagasinConnectGUI.py
```Python
MagasinConnect = SQL.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="magasin_connect"
)
```

### Ejecutar la aplicación
```bash
python MagasinConnectGUI.py
```
---

## 🙋‍♂️ Autor - 
Kushagra Aggarwal
- Estudiante, 12.º curso
- Dr. B. R. Ambedkar SoSE, Plot No. 1, Link Road, Karol Bagh
- Delhi Board of School Education (DBSE)

Este proyecto se creó con pasión por la informática y su aplicación práctica.

---

📄 Licencia:

Este proyecto está abierto para uso educativo.

Para otros usos, contacta con el autor.

---

📌 Notas:

- ⚠️ No nombre su tienda "shops" (es una tabla reservada).
- 🎨 La ruta del tema en el código podría necesitar actualizarse según su sistema.

---

Si le resulta útil, ¡comparta el repositorio con ⭐!
