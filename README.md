# 💧 Drink Water Reminder (Flask Project)

## 📌 Project Overview
The **Drink Water Reminder** is a Flask-based mini project developed using Python and web technologies.  
It helps users maintain healthy hydration habits by sending periodic water reminder notifications.  
The project provides a simple web interface to start and stop reminders.

---

## 🎯 Objectives
- To remind users to drink water at regular intervals  
- To demonstrate the use of the Flask framework  
- To implement background task execution using threading  
- To build a simple and interactive web application  

---

## 🛠️ Technologies Used
- Python – Backend logic  
- Flask – Web framework  
- HTML – Web page structure  
- CSS & Bootstrap – Styling and responsive design  
- JavaScript – Client-side interaction  
- Threading (Python) – Background execution of reminders  
- Plyer – Desktop notifications  

---

## ✨ Features
- Start and stop water reminders using a web interface  
- Desktop notifications at fixed time intervals  
- Background execution without blocking the server  
- Simple and user-friendly UI  

---

## 📂 Project Structure
drink-water-reminder/<br>
│<br>
├── app.py<br>
├── requirements.txt<br>
├── templates/<br>
│   └── index.html<br>
└── static/<br>
    └── style.css<br>

---

⚠️ Important Note
- Desktop notifications using plyer work only on local machines
- When deployed online, notification functionality will not work due to server limitations

---

## ▶️ How to Run the Project Locally

# 1️⃣ Install Required Libraries
```bash
pip install flask plyer
```
# 2️⃣ Run the Flask App
```
python app.py
```
# 3️⃣ Open in Browser
```
http://127.0.0.1:5000/
```

## Desktop notifications work only when the project is run locally using the Plyer module. They do not work after deployment. Sorry for the inconvenience caused.




