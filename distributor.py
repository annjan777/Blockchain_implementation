class Distributor:
    def __init__(self, manager):
        self.pending_transactions = []
        self.manager = manager

    def register_miner(self, miner):
        self.manager.add_miner(miner)

    def remove_miner(self, miner):
        self.manager.remove_miner(miner)

    def list_miners(self):
        return self.manager.list_miners()

    def receive_transaction(self, transaction):
        self.pending_transactions.append(transaction)
        self.distribute_transaction()

    def distribute_transaction(self):
        for miner in self.manager.miners:
            self.manager.communicate(miner, self.pending_transactions.copy())
