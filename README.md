<h1 align="center"><code>Exam_seats_generator  📚💻🖨☕️📖📓📚📝✍️📜✒️🎓</code></h1>

<div align="center">
  <sub>Created by Gab-182 {Ghaiath Abdoush} for 42 AbuDhabi</sub>
</div>

---

### Script to request student data from 42 intra API,and send email to each student about where he/she is going to set in the exam.

---

## Tree structure
```
(base) ➜  Exam_seats_generator git:(master) ✗ tree      
.
├── algorithm.py
├── api_lib
│   ├── config.yml
│   └── intra.py
├── chosen_labs
│   ├── exam_choices.py
│   └── seats_comps.py
├── main.py
├── READ_***_FIRST.txt
├── README.md
├── request_data.py
├── requirements.txt
├── res
│   ├── colors.py
│   └── Intra-Meta-Clusters.png
├── send_emails.py
└── users_data.csv

3 directories, 14 files

```
---

## Pre-requisites:

First things first, get yourself Python 3.6 or above. You will also need the packages listed in the 'requirements.txt'. Install them with the command `pip3 install -r requirements.txt`
In order to request info from 42 intra api, you will need to configure your `config.yml` file
    client: "example_726432892489323472345" #UID
    secret: "example_238749273073423748329" #SECRET

---

## Usage:
run the script with command `python3 main.py` then follow the instructions

---
## NOTE:
`42API Lib` is used in this script, to edit the configuration for api requests go and check <a href="https://github.com/hivehelsinki/42api-lib">42API Lib</a>
42API Lib is Adapted by Hive Helsinki for all the 42 Network

---

![alt text](https://github.com/Gab-182/E_script/blob/master/res/Intra-Meta-Clusters.png)
