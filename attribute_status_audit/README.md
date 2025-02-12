# 📝 Attribute Status Audit Script Setup (macOS)

## 🚀 Overview

This guide helps you set up and run the **Attribute Status Audit** script on macOS while resolving the **"externally managed environment"** issue when installing Python packages.

Since **macOS restricts global Python package installations**, we will use a **virtual environment** to properly install `pandas` and `openpyxl` without breaking system configurations.

---

## 📌 **Step-by-Step Installation Guide**

### **1️⃣ Create a Virtual Environment**

We first create an isolated Python environment so that dependencies like `pandas` can be installed without issues.

```bash
python3 -m venv ~/venvs/attribute_status_env
```

✅ This will create a virtual environment in `~/venvs/attribute_status_env`.

---

### **2️⃣ Activate the Virtual Environment**

Before installing packages, activate the environment:

```bash
source ~/venvs/attribute_status_env/bin/activate
```

✅ If activated successfully, your terminal should show:

```
(attribute_status_env) yourname@Mac ~ %
```

---

### **3️⃣ Install Required Python Packages**

Once inside the virtual environment, install the necessary dependencies:

```bash
pip install pandas openpyxl
```

---

### **4️⃣ Run the Script**

Now, navigate to your **local desktop** and execute the script:

```bash
cd ~/Desktop
python3 attribute_status_audit.py
```

✅ This will process the Excel file and generate the required output.

---

### **5️⃣ Exit the Virtual Environment (When Done)**

To deactivate the virtual environment and return to the normal terminal session:

```bash
deactivate
```

Your command prompt will no longer show `(attribute_status_env)`.

---

## 📌 **Quick Summary of Commands**

| Step                           | Command                                             |
| ------------------------------ | --------------------------------------------------- |
| **Create Virtual Environment** | `python3 -m venv ~/venvs/attribute_status_env`      |
| **Activate Environment**       | `source ~/venvs/attribute_status_env/bin/activate`  |
| **Install pandas & openpyxl**  | `pip install pandas openpyxl`                       |
| **Run the Script**             | `cd ~/Desktop && python3 attribute_status_audit.py` |
| **Exit Environment**           | `deactivate`                                        |

---

## ❓ **Troubleshooting**

### 🔹 **Check If pandas Is Installed**

If you get a `ModuleNotFoundError: No module named 'pandas'`, verify the installation:

```bash
python3 -m pip show pandas
```

If it doesn’t show output, ensure you activated the virtual environment using:

```bash
source ~/venvs/attribute_status_env/bin/activate
```
