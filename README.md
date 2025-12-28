# Selenium Automation Practice Form Project

##  Project Overview
This project automates the **DemoQA Automation Practice Form** using **Python and Selenium**.  
It reads user input from a `.txt` file and automatically fills the web form, simulating real user behavior.

This project demonstrates **data-driven automation**, **explicit waits**, and **form handling** in Selenium.

---

##  Target Website
🔗 https://demoqa.com/automation-practice-form

---

##  Tech Stack
- **Python 3**
- **Selenium WebDriver**
- **Google Chrome**
- **VS Code**
- **Text file (data-driven testing)**

---

##  Key Features
-  Data-driven automation using `.txt` file
-  Auto-fills:
  - First Name, Last Name
  - Email & Mobile Number
  - Current Address
-  Handles:
  - Gender (Radio Buttons)
  - Date of Birth (Date Picker)
  - Subjects (Auto-suggestion)
  - Hobbies (Checkboxes)
-  Manual pause for user verification before submission
-  Uses **Explicit Waits** for stability
-  Safe execution with proper browser cleanup

---

## Project Structure
selenium-practice-form/
│
├── automation.py # Main automation script
├── data.txt # Input test data
├── requirements.txt # Project dependencies
└── README.md # Project documentation

## Sample `data.txt`
first_name=Pranav
last_name=Pardhi
email=pranav@gmail.com
mobile=9876543210
gender=Male
dob=10 Oct 1999
subjects=Maths, Physics
hobbies=Sports, Reading
address=Dev Bhumi Bharat
