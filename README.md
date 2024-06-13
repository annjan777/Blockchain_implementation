# Blockchain Implementation

## Overview
This project implements a basic blockchain-based transaction system using Proof of Work (PoW). The system consists of a blockchain, miners, and a distributor that acts as an intermediary between users and miners.

## Directory Structure

blockchain_implementation/
- `app.py`
- `blockchain.py`
- `miner.py`
- `distributor.py`
- `transaction.py`
- `manager.py`
- `requirements.txt`
- `templates/`
  - `index.html`
- `static/`
  - `css/`
    - `style.css`
  - `js/`
    - `main.js`



## Setup
1. **Install Dependencies**: Ensure Python is installed. Navigate to the project directory in your terminal and run:
    ```bash
    pip install -r requirements.txt
    ```

2. **Run the application**: Execute the following command to start the Flask server:
    ```bash
    python app.py
    ```

3. **Access the Web Interface**: Open your web browser and go to `http://localhost:5000`. You can now interact with the blockchain through the provided web interface.

## Usage
- Submit a transaction using the form on the web interface.
- View the blockchain using the `/chain` endpoint.

## Components
- **Blockchain**: Manages the chain of blocks.
- **Miner**: Mines new blocks and adds them to the blockchain.
- **Distributor**: Receives transactions from users and distributes them to miners.

## Detailed Instructions

### How to Run

1. **Install Dependencies**: Ensure you have Python installed on your system. Navigate to the project directory in your terminal and run:
    ```bash
    pip install -r requirements.txt
    ```

2. **Start the Application**: Run the following command to start the Flask server:
    ```bash
    python app.py
    ```

3. **Access the Web Interface**: Open your web browser and go to `http://localhost:5000`. You can now interact with the blockchain through the provided web interface.

### Additional Notes

- Ensure you replace placeholders like `<server_ip>`, `<miner_host>`, `<miner_port>`, `<miner_name>`, `<sender_name>`, `<recipient_name>`, and `<transaction_amount>` with actual values.
- Feel free to reach out for any assistance or issues you encounter.

## License
MIT License
