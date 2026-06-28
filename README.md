# X_x Tool

## 📋 Requirements

- **Windows 10/11**
- **Python 3.10 or 3.11** 
- **GPU with CUDA support** 

---

## 🚀 Installation (Step by Step)

### Step 1: Install Python

1. Download Python from: **https://www.python.org/downloads/**
2. Run the installer
3. ⚠️ **IMPORTANT: Check the box `Add Python to PATH`** at the bottom of the installer!
4. Click "Install Now"

### Step 2: Download This Project

Download and extract the project ZIP file to any folder on your computer

### Step 3: Install Dependencies

Simply double-click **`install.bat`** and wait for it to finish.

### Step 4: Run the Program

Double-click **`run.bat`**


## ⚙️ First-Time Setup

On the first run, the program will ask you to configure your screen resolution:
- Enter your screen **width** (e.g. `1920`)
- Enter your screen **height** (e.g. `1080`)

To reconfigure later:
```
python X_x.py setup
```

### "Python is not recognized"
→ You forgot to check **"Add Python to PATH"** during installation. 

### "pip is not recognized"
→ Run: `python -m ensurepip --upgrade`

### torch/CUDA errors
→ If you don't have an NVIDIA GPU, the CPU version of PyTorch will be used automatically. Performance will be slower but it will still work.

### "ModuleNotFoundError: No module named '...'"
→ Run `pip install -r requirements.txt` again, or install the missing module:
```
pip install <module_name>
```

## 📌 Version

Current version: **0.1.1**
