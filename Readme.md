# 📱 Appium Pytest Sample for Android & iOS | LambdaTest

This repository contains a sample framework for **native mobile app testing** using **Python**, **Pytest**, and **Appium**, designed to run on the [LambdaTest](https://www.lambdatest.com/) Real Device Cloud using **HyperExecute** or the Appium grid.

## ✅ Features

- 🚀 Runs on **real Android and iOS devices**
- ⚙️ Uses **Appium + Pytest**
- 🌐 Supports **LambdaTest Mobile App Grid**
- 📦 Includes **3 test cases each** for Android and iOS
- 🔁 Easily extendable for CI tools and HyperExecute

---

## 📁 Project Structure

appium-pytest-sample/
│
├── tests/
│ ├── test_android_app.py # Main Android test flow
│ └── test_ios_app.py # Optional: iOS test file
│
├── hyperexecute.yaml # HyperExecute config (if used)
├── requirements.txt # Python dependencies
└── README.md # You're here!


---

## 🔧 Setup Instructions

### 1. Clone the repo

```bash
git clone https://github.com/yourusername/appium-pytest-sample.git
cd appium-pytest-sample


2. Install dependencies

We recommend using a virtual environment:

python -m venv venv
source venv/bin/activate   # or venv\Scripts\activate on Windows
pip install -r requirements.txt


🔐 LambdaTest Credentials
Set your LambdaTest credentials as environment variables:

bash

export LT_USERNAME=<your-username>
export LT_ACCESS_KEY=<your-access-key>
On Windows (PowerShell):

powershell

$env:LT_USERNAME="<your-username>"
$env:LT_ACCESS_KEY="<your-access-key>"


📲 Upload Your App

Upload your .apk or .ipa to LambdaTest and get the app URL (looks like lt://APP_ID_HERE).

Replace the value in the app capability in your test file:

python

options.set_capability("app", "lt://YOUR_APP_ID")



▶️ Run Tests
Android Example

pytest tests/test_android_app.py

iOS Example

pytest tests/test_ios_app.py