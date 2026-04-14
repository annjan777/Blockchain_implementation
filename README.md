# 🔗 Blockchain Implementation (Python)

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Blockchain](https://img.shields.io/badge/Blockchain-Proof%20of%20Work-green)
![Flask](https://img.shields.io/badge/Flask-Web%20App-black?logo=flask)

---

## 📌 Overview
This project implements a **blockchain-based transaction system** using **Proof of Work (PoW)**, simulating how decentralized systems validate and store transactions securely.

The system consists of:
- A **blockchain ledger**
- Multiple **miners performing PoW**
- A **distributor** acting as an intermediary between users and miners  
- A **web interface** for interaction

---

## 🏗️ Architecture

User → Web Interface → Distributor → Miners → Blockchain Ledger

- Users submit transactions via UI  
- Distributor forwards transactions to miners  
- Miners validate and mine blocks using PoW  
- Blockchain stores immutable transaction history  

---

## ⚙️ Tech Stack
- Python 3.x  
- Flask (Web framework)  
- HTML, CSS, JavaScript (Frontend)  

---

## 📂 Project Structure
```
blockchain_implementation/
│── app.py              # Flask entry point
│── blockchain.py       # Core blockchain logic
│── miner.py            # Mining logic (Proof-of-Work)
│── distributor.py      # Transaction distribution system
│── transaction.py      # Transaction model
│── manager.py          # System coordination
│── requirements.txt
│── templates/
│   └── index.html
│── static/
│   ├── css/
│   │   └── style.css
│   └── js/
│       └── main.js
```

---

## 🔥 Key Features
- ⛓️ Blockchain ledger with immutable records  
- ⚡ Proof-of-Work mining mechanism  
- 💸 Transaction creation and validation  
- 🔁 Distributor system for miner communication  
- 🌐 Web interface for user interaction  
- 🧩 Modular architecture (miners, distributor, manager)  

---

## 🚀 Setup & Execution

### 1️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 2️⃣ Run Application
```bash
python app.py
```

### 3️⃣ Access Web Interface
Open:
```
http://localhost:5000
```

---

## 📊 How It Works

1. User submits a transaction via UI  
2. Distributor receives and forwards it  
3. Miners perform Proof-of-Work  
4. Valid block is added to blockchain  
5. Blockchain updates across system  

---

## 🔌 Usage

- Submit transactions using the web interface  
- View blockchain data:
```
/chain
```

---

## 🧠 System Components

### 🔹 Blockchain
Manages the chain of blocks and ensures data integrity using hashing.

### 🔹 Miner
Performs Proof-of-Work to validate transactions and create new blocks.

### 🔹 Distributor
Acts as a communication layer between users and miners.

### 🔹 Manager
Coordinates system operations and workflow.

---

## 🧪 Observability
- View blockchain state via `/chain` endpoint  
- Monitor transaction flow through UI  
- Debug mining and validation processes  

---

## 🧠 Key Learnings
- Implemented blockchain logic from scratch  
- Understood Proof-of-Work and mining  
- Designed modular distributed components  
- Built full-stack system with backend + UI  

---

## 💡 Future Improvements
- 🔐 Add cryptographic signatures for transactions  
- 🌍 Implement peer-to-peer networking  
- 💾 Persistent storage (database integration)  
- ⚡ Optimize mining efficiency  
- 🪙 Add cryptocurrency/token system  

---

## 📜 License
MIT License

---

## 👨‍💻 Author
**Annjan Arora**

---

## ⭐ Star this repo if you found it useful!
