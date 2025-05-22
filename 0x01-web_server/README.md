# 0x01. Web Server 🌐

This project focuses on setting up and managing a web server using **Nginx** on a Linux-based system. It covers basic server configuration, file transfer, domain setup, redirection, and custom error pages.

---

## 📁 Project Structure

| File                         | Description |
|------------------------------|-------------|
| `0-transfer_file`            | Script to transfer a file to a remote server using `scp` |
| `1-install_nginx_web_server` | Script to install and configure Nginx on a remote server |
| `2-setup_a_domain_name`      | Instructions for setting up and pointing a domain name to the server |
| `3-redirection`              | Nginx configuration to redirect all requests to a specific URL |
| `4-not_found_page_404`       | Custom 404 error page setup using Nginx |
| `README.md`                  | Project overview and documentation |

---

## 🧠 Concepts Covered

- Securely transferring files to a server using `scp`
- Installing and configuring Nginx
- Managing Nginx services
- DNS basics and setting up a custom domain
- Creating redirection rules with Nginx
- Serving custom 404 error pages

---

## 🔧 Setup Instructions

### Install Nginx on a Remote Server
```bash
./1-install_nginx_web_server
```

📌 Note
This project is part of the System Engineering & DevOps curriculum at Holberton School, aimed at building foundational skills in server administration, web hosting, and DevOps practices.

## Author
AnActualBanana
