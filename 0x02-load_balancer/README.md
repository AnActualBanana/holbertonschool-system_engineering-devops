# 0x02. Load Balancer ⚖️

This project focuses on the implementation and configuration of a **load balancer** to distribute network traffic across multiple servers. It forms part of the **System Engineering & DevOps** track at **Holberton School**, aiming to improve scalability, reliability, and performance of web services.

---

## 🧰 Project Files

| File                         | Description |
|------------------------------|-------------|
| `0-custom_http_response_header` | Configures a web server to return a custom HTTP response header, useful for identifying backend responses when using a load balancer |
| `1-install_load_balancer`      | Script to install and configure HAProxy as a load balancer between two backend web servers |
| `README.md`                    | Project overview and documentation |

---

## 💡 Concepts Covered

- What is a **load balancer** and why it's important
- Setting up **HAProxy** to distribute traffic
- Configuring web servers to return unique HTTP headers for traceability
- High availability, scalability, and fault tolerance principles

---

## ⚙️ Setup Instructions

### Add Custom HTTP Header on Web Server

In your Nginx configuration (on each backend server):

```nginx
add_header X-Served-By $hostname;
```

## Install and Configure HAProxy
To install and configure HAProxy as a load balancer:

bash
sudo apt-get update
sudo apt-get install -y haproxy

## Author
Logan McClain
