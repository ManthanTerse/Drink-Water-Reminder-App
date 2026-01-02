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


---

# Screenshots :
<img width="1919" height="900" alt="Screenshot 2026-01-02 221536" src="https://github.com/user-attachments/assets/5dc72dc1-b01c-4489-80c9-f1d2b97b0241" />
<img width="1919" height="904" alt="Screenshot 2026-01-02 221607" src="https://github.com/user-attachments/assets/f5d9be16-d1fc-44d2-8366-c469576fc08a" />
<img width="794" height="569"  align = "center" alt="Screenshot 2026-01-02 221624" src="https://github.com/user-attachments/assets/dba5c37a-edf1-4969-a6cb-850d14d6207d" />

---

## Desktop notifications work only when the project is run locally using the Plyer module. They do not work after deployment. Sorry for the inconvenience caused.






