# 🏰️ Job Scheduling System

A simple **Job Scheduling System** built with Django & Bootstrap.

## 🚀 Features
- Add & remove jobs dynamically
- Apply **Job Scheduling Algorithm** for maximum profit
- Display **scheduled jobs & total profit**
- Built with **Django & Bootstrap**

## 🛠️ Setup
1️⃣ Clone the repo:
```sh
git clone https://github.com/darshangohil46/JobScheduling.git
cd job-scheduling
```
2️⃣ Install dependencies:
```sh
pip install django
```
3️⃣ Run the server:
```sh
python manage.py runserver
```
Now, visit [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in your browser.

## 🌜 Job Scheduling Algorithm
- Sort jobs in **descending order of profit**
- Assign to the latest available time slot before its deadline
- Track scheduled jobs & calculate total profit

## 🌜 Example Input
| Job ID | Deadline | Profit |
|--------|---------|--------|
| A      | 2       | 100    |
| B      | 1       | 19     |
| C      | 2       | 27     |

## 🌜 Output (Scheduled Jobs)
| Job ID | Deadline | Profit |
|--------|---------|--------|
| A      | 2       | 100    |
| C      | 2       | 27     |

💰 **Total Profit: ₹127**

## 🖥️ Technologies Used
- Django (Backend)
- Bootstrap (Frontend)
- JavaScript (Dynamic Input)

📌 **Star this repo if you like it!**

