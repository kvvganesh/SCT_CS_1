# Caesar Cipher Encryption Tool 🔐

A simple Python-based Caesar Cipher program that allows users to encrypt and decrypt messages using a custom shift value.

## Overview

The Caesar Cipher is one of the oldest and simplest encryption techniques. It works by shifting each letter in a message by a fixed number of positions in the alphabet.

For example, with a shift value of **3**:

* A → D
* B → E
* X → A
* Y → B
* Z → C

This project provides both encryption and decryption functionality through an interactive menu-driven interface.

---

Features:

* Encrypt plaintext messages
* Decrypt encrypted messages
* User-defined shift values
* Preserves spaces, numbers, and special characters
* Interactive command-line interface
* Beginner-friendly Python implementation

---

## 🛠️ Technologies Used

* Python 3

---

## 📂 Project Structure

```text
Caesar-Cipher/
│
├── caesar_cipher.py
├── README.md
└── screenshots/
    └── terminal_output.png
```

---

## 🚀 How to Run

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/caesar-cipher.git
```

### 2. Navigate to the Project Directory

```bash
cd caesar-cipher
```

### 3. Run the Program

```bash
python caesar_cipher.py
```

---

## 📖 Usage

When the program starts, you will see a menu:

```text
1. Encrypt Message
2. Decrypt Message
3. Exit
```

### Example

#### Encryption

```text
Enter message: HELLO
Enter shift value: 3

Encrypted Message: KHOOR
```

 Decryption

```text
Enter encrypted message: KHOOR
Enter shift value: 3

Decrypted Message: HELLO
```



🔒 About Caesar Cipher

The Caesar Cipher is a substitution cipher where each letter is shifted by a fixed number of positions in the alphabet. Although it is not secure by modern standards, it is widely used as an introductory concept for learning cryptography.



👨‍💻 Author

Ganesh

Learning Python & Security Fundamentals


