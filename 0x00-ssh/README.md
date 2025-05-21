# 0x00. SSH 🔐

This project focuses on setting up and managing secure connections between remote systems using SSH (Secure Shell). It covers the creation of SSH key pairs, configuring SSH access, and using private keys to authenticate securely with remote servers.

---

## 📁 Project Structure

| File/Directory         | Description |
|------------------------|-------------|
| `0-use_a_private_key`  | Demonstrates how to connect to a remote server using a provided private key |
| `1-create_ssh_key_pair`| Instructions for creating a new SSH key pair using `ssh-keygen` |
| `2-ssh_config`         | Example SSH configuration file to simplify future SSH connections |
| `school`               | Private key file (⚠️ should be kept secret and secure) |
| `school.pub`           | Public key corresponding to the `school` private key |

---

## 🧠 Concepts Covered

- Understanding how SSH works
- Generating and managing SSH key pairs
- Connecting to remote servers using private key authentication
- Simplifying SSH connections with configuration files
- Secure practices when working with private/public key pairs

---

## 🧪 Usage Examples

### Connect with a Private Key
```bash
ssh -i school ubuntu@<remote-ip-address>
```

## Author
Logan McClain
