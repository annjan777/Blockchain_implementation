from flask import Flask, request, jsonify, render_template
from blockchain import Blockchain
from distributor import Distributor
from miner import Miner
from transaction import Transaction
from manager import MinerManager, MinerNode

app = Flask(__name__)

blockchain = Blockchain()
manager = MinerManager()
distributor = Distributor(manager)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/transaction', methods=['POST'])
def new_transaction():
    transaction_data = request.get_json()
    transaction = Transaction(
        sender=transaction_data['sender'],
        recipient=transaction_data['recipient'],
        amount=transaction_data['amount']
    )
    distributor.receive_transaction(transaction.__dict__)
    return jsonify({"message": "Transaction received"}), 201

@app.route('/chain', methods=['GET'])
def get_chain():
    chain_data = [block.__dict__ for block in blockchain.chain]
    return jsonify(chain_data), 200

@app.route('/miners', methods=['GET'])
def list_miners():
    miners = distributor.list_miners()
    return jsonify(miners), 200

@app.route('/add_miner', methods=['POST'])
def add_miner():
    miner_data = request.get_json()
    miner = MinerNode(
        host=miner_data['host'],
        port=miner_data['port'],
        blockchain=blockchain,
        pending_transactions=distributor.pending_transactions,
        miner_address=miner_data['miner_address'],
        mined_blocks=[]
    )
    miner.start()
    distributor.register_miner(miner)
    return jsonify({"message": "Miner added"}), 201

@app.route('/remove_miner', methods=['POST'])
def remove_miner():
    miner_data = request.get_json()
    miner = next((m for m in distributor.manager.miners if m.miner_address == miner_data['miner_address']), None)
    if miner:
        distributor.remove_miner(miner)
        return jsonify({"message": "Miner removed"}), 200
    return jsonify({"message": "Miner not found"}), 404

if __name__ == '__main__':
    miner1 = MinerNode(host='10.14.190.227', port=6001, blockchain=blockchain, pending_transactions=[], miner_address='miner1', mined_blocks=[])
    miner2 = MinerNode(host='10.14.198.220', port=6002, blockchain=blockchain, pending_transactions=[], miner_address='miner2', mined_blocks=[])
    
    miner1.start()
    miner2.start()
    
    manager.add_miner(miner1)
    manager.add_miner(miner2)
    
    distributor.register_miner(miner1)
    distributor.register_miner(miner2)
    
    app.run(host='0.0.0.0', port=5001)
