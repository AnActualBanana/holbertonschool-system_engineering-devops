# 0x04. MySQL 🐬

This project is part of the **System Engineering & DevOps** curriculum at **Holberton School**. It focuses on installing and configuring MySQL, setting up primary-replica architecture, and implementing automated backups.

---

## 📁 Project Files

| File Name                     | Description                                                    |
|------------------------------|----------------------------------------------------------------|
| `4-mysql_configuration_primary` | Configuration file for setting up the **primary MySQL server** |
| `4-mysql_configuration_replica` | Configuration file for setting up the **replica MySQL server** |
| `5-mysql_backup`               | Bash script to automate **MySQL backups**                      |
| `README.md`                   | Project documentation                                          |

---

## 🔧 Project Objectives

- Understand the role of a database in a web infrastructure
- Install and configure MySQL on Ubuntu servers
- Set up **primary-replica** MySQL configuration
- Automate database **backups** using scripts
- Modify MySQL configurations securely and effectively

---

## 🗃️ Key Concepts

- MySQL user creation and privilege granting
- MySQL configuration via `/etc/mysql/my.cnf`
- Database replication setup
- Secure connection and bind-address adjustments
- Dumping and restoring data using `mysqldump`

---

## 🚀 Usage

### 📌 1. Configure Primary Server
Edit your MySQL config:
```bash
sudo vim /etc/mysql/my.cnf
# Comment out bind-address or set it to 0.0.0.0
```

Then apply changes:

```bash
Copy
Edit
sudo service mysql restart
```
📌 2. Set Up Replica Server
Repeat the above with appropriate adjustments and connect the replica to the primary using replication credentials.

📌 3. Run Backup Script
```bash
Copy
Edit
chmod +x 5-mysql_backup
./5-mysql_backup
```
This script will generate a .sql dump of your database for easy recovery.


## Author
Logan McClain
