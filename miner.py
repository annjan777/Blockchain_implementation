import threading
from blockchain import Block

class Miner(threading.Thread):
    def __init__(self, blockchain, pending_transactions, miner_address, mined_blocks):
        threading.Thread.__init__(self)
        self.blockchain = blockchain
        self.pending_transactions = pending_transactions
        self.miner_address = miner_address
        self.mined_blocks = mined_blocks

    def run(self):
        while True:
            if self.pending_transactions:
                transaction_data = self.pending_transactions.pop(0)
                new_block = Block(
                    index=len(self.blockchain.chain),
                    previous_hash=self.blockchain.get_latest_block().hash,
                    timestamp=time.time(),
                    transactions=transaction_data
                )
                self.blockchain.add_block(new_block)
                self.mined_blocks.append(new_block)
                print(f"Miner {self.miner_address} mined a block: {new_block.hash}")
