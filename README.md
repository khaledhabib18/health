# 🩺 Health Monitoring Dashboard

A simple real-time health monitoring web dashboard built using **HTML, CSS, JavaScript, and Python**. The project displays important health metrics in a clean and visual way, making it suitable for learning, prototyping, or integration with real sensors and IoT systems.

---

## 🚀 Features

* 📊 Real-time display of health data
* 🎨 Clean and responsive user interface
* 🐍 Python backend server
* 🌐 Web-based dashboard
* 🧩 Easy to extend with real sensors (Arduino / ESP32)

Displayed metrics include:

* Heart Rate
* Body Temperature
* Blood Oxygen Level (SpO₂)
* Humidity
* Additional health indicators

---

## 🧠 Project Overview

The project consists of a frontend dashboard and a Python backend:

* **Frontend**: Displays health data using HTML, CSS, and JavaScript
* **Backend**: A Python server (`server.py`) that serves the web page and provides health data (real or simulated)
* **Assets**: Icons and images representing each health parameter

---

## 🛠 Installation & Setup

### 1️⃣ Clone the repository

```bash
git clone https://github.com/khaledhabib18/health.git
cd health
```

### 2️⃣ Install Python dependencies

```bash
pip install flask
```

*(If you add a `requirements.txt` later, install using it instead)*

### 3️⃣ Run the server

```bash
python server.py
```

### 4️⃣ Open in browser

```
http://localhost:5000
```

---

## 📁 Project Structure

```
health/
│── index.html        # Main dashboard page
│── style.css         # Styling and layout
│── script.js         # Frontend logic
│── server.py         # Python backend server
│── logo.png          # Project logo
│── heart_rate.png    # Heart rate icon
│── temperature.png   # Temperature icon
│── blood_oxygen.png  # SpO₂ icon
│── humidity.png      # Humidity icon
│── body_temp.png     # Body temperature icon
└── README.md         # Documentation
```

---

## 📌 Use Cases

* Health monitoring system prototype
* IoT dashboard for medical sensors
* Educational project for web + Python integration
* Base project for ESP32 / Arduino sensor dashboards

---

## 🔧 Future Improvements

* Connect to real health sensors
* Add database support
* User authentication
* Mobile-friendly layout
* WebSocket-based real-time updates

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create a new branch
3. Make your changes
4. Submit a pull request

---

## 📄 License

This project is currently unlicensed. Feel free to add a license if you plan to open-source it publicly.

---

## 👤 Author

**Khaled Habib**
Electrical Engineer | Embedded Systems | Web & IoT Enthusiast

---

⭐ If you like this project, consider giving it a star on GitHub!
