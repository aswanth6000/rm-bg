# 🖼️ RemoveBG for Windows

A simple, privacy-first tool to **remove image backgrounds** instantly — right from your Windows context menu.

![screenshot](https://res.cloudinary.com/dpqpclkby/image/upload/v1752391456/2ae36aa0-d89c-4e8f-a913-f084cc18bbb6.png)

## ✨ Features

* 🗱️ Right-click any image → **Remove Background**
* ⚡ Works **offline** — no cloud processing
* 🔒 100% local & private (nothing is uploaded)
* �� Saves result with `_no_bg.png` suffix
* 📦 Easy installer, clean uninstall

---

## 📅 Download

👉 [Download RemoveBG for Windows (.exe)](https://removebg.aswanth.blog)

---


## 🧠 How It Works

1. Installs a right-click context menu entry for `.png`, `.jpg`, `.jpeg`, and `.webp` images.
2. When triggered, it runs a bundled Python executable using [rembg](https://github.com/danielgatis/rembg).
3. Background is removed using ONNX models (local), and saved next to the original file.

---

## 🛠️ Built With

* Python 3.11
* [rembg](https://github.com/danielgatis/rembg)
* [onnxruntime](https://onnxruntime.ai/)
* [pyinstaller](https://pyinstaller.org/)
* Inno Setup
* Shell scripting + Registry edits

---

## 📦 For Developers

If you want to build or modify it yourself:

### 1. Clone and install dependencies

```bash
git clone https://github.com/aswanth6000/rm-bg
cd removebg
pip install -r requirements.txt
```

### 2. Test the script

```bash
python remove_bg.py path/to/image.jpg
```

### 3. Build EXE

```bash
pyinstaller --onefile remove_bg.py   
```
It will create .exe file in dist folder 


### 4. Create Installer

Use [Inno Setup](https://github.com/aswanth6000/RemoveBGInstaller) and the provided `.iss` file.

---

## 🧪 Known Limitations

* First run might take a few seconds (model warm-up)
* Basic UI (command line hidden, but no GUI)

---

## ☕ Support This Project

If you find this useful:

* 🌟 Star this repo
---

## 📄 License

MIT License

---

> Built with ❤️ by [@aswanth6000](https://github.com/aswanth6000)
