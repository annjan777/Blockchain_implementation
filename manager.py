import socket
import threading
import json

class MinerManager:
    def __init__(self):
        self.miners = []

    def add_miner(self, miner):
        self.miners.append(miner)

    def remove_miner(self, miner):
        self.miners.remove(miner)

    def list_miners(self):
        return [miner.miner_address for miner in self.miners]

    def communicate(self, miner, data):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect((miner.host, miner.port))
                s.sendall(json.dumps(data).encode())
        except ConnectionRefusedError:
            print(f"Could not connect to miner {miner.miner_address} at {miner.host}:{miner.port}")

class MinerNode(threading.Thread):
    def __init__(self, host, port, blockchain, pending_transactions, miner_address, mined_blocks):
        threading.Thread.__init__(self)
        self.host = host
        self.port = port
        self.blockchain = blockchain
        self.pending_transactions = pending_transactions
        self.miner_address = miner_address
        self.mined_blocks = mined_blocks

    def run(self):
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind((self.host, self.port))
        server_socket.listen(5)
        print(f"Miner {self.miner_address} listening on {self.host}:{self.port}")

        while True:
            client_socket, addr = server_socket.accept()
            data = client_socket.recv(1024).decode()
            if data:
                transaction_data = json.loads(data)
                self.pending_transactions.append(transaction_data)
                new_block = Block(
                    index=len(self.blockchain.chain),
                    previous_hash=self.blockchain.get_latest_block().hash,
                    timestamp=time.time(),
                    transactions=transaction_data
                )
                self.blockchain.add_block(new_block)
                self.mined_blocks.append(new_block)
                print(f"Miner {self.miner_address} mined a block: {new_block.hash}")
            client_socket.close()
