import hashlib
import datetime

class Block:
    def __init__(self, index, timestamp, data, previous_hash, nonce=0):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = nonce
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        """
        Calculates the SHA-256 hash of the block's contents.
        """
        block_string = str(self.index) + str(self.timestamp) + str(self.data) + \
                       str(self.previous_hash) + str(self.nonce)
        return hashlib.sha256(block_string.encode()).hexdigest()

class Blockchain:
    def __init__(self):
        self.chain = []
        self.create_genesis_block()

    def create_genesis_block(self):
        """
        Creates the first block in the blockchain (genesis block).
        """
        self.chain.append(Block(0, datetime.datetime.now(), "Genesis Block", "0"))

    def get_latest_block(self):
        """
        Returns the latest block in the chain.
        """
        return self.chain[-1]

    def add_block(self, new_block):
        """
        Adds a new block to the chain, linking it to the previous block.
        """
        new_block.previous_hash = self.get_latest_block().hash
        new_block.hash = new_block.calculate_hash()
        self.chain.append(new_block)

    def display_chain(self):
        """
        Displays all blocks in the blockchain with their hashes.
        """
        print("\n--- Blockchain ---")
        for block in self.chain:
            print(f"Index: {block.index}")
            print(f"Timestamp: {block.timestamp}")
            print(f"Data: {block.data}")
            print(f"Previous Hash: {block.previous_hash}")
            print(f"Hash: {block.hash}")
            print("-" * 20)
        print("------------------")

    def is_chain_valid(self):
        """
        Checks if the blockchain is valid (hashes are correctly linked).
        """
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i-1]

            # Check if the current block's hash is correct
            if current_block.hash != current_block.calculate_hash():
                return False

            # Check if the current block's previous_hash links to the actual previous block's hash
            if current_block.previous_hash != previous_block.hash:
                return False
        return True

# --- Main execution ---
if __name__ == "__main__":
    my_blockchain = Blockchain()

    # Link 3 blocks by chaining their previousHash
    print("Creating Block 1...")
    block1 = Block(1, datetime.datetime.now(), {"amount": 10, "to": "Alice", "from": "Bob"}, "")
    my_blockchain.add_block(block1)

    print("Creating Block 2...")
    block2 = Block(2, datetime.datetime.now(), {"amount": 5, "to": "Charlie", "from": "Alice"}, "")
    my_blockchain.add_block(block2)

    print("Creating Block 3...")
    block3 = Block(3, datetime.datetime.now(), {"amount": 12, "to": "Bob", "from": "Charlie"}, "")
    my_blockchain.add_block(block3)

    # Display all blocks with their hashes
    my_blockchain.display_chain()

    print(f"\nIs blockchain valid initially? {my_blockchain.is_chain_valid()}")

    # --- Challenge: Change the data of Block 1 and recalculate its hash. ---
    print("\n--- Challenge: Tampering with Block 1 ---")
    # Access Block 1 (index 1 in the chain list, as genesis is at 0)
    # IMPORTANT: In a real blockchain, direct modification like this is prevented by proof-of-work
    # and network consensus. This is for demonstration of the hashing concept.
    tampered_block = my_blockchain.chain[1]
    original_data = tampered_block.data
    tampered_block.data = {"amount": 1000, "to": "Alice", "from": "Bob"} # Tamper the data
    print(f"Original data of Block 1: {original_data}")
    print(f"Tampered data of Block 1: {tampered_block.data}")

    # Recalculate hash of tampered block (as per challenge instruction)
    tampered_block.hash = tampered_block.calculate_hash()
    print(f"Recalculated hash for tampered Block 1: {tampered_block.hash}")

    # Observe how all following blocks become invalid unless hashes are recomputed.
    print("\nDisplaying chain after tampering with Block 1:")
    my_blockchain.display_chain()
    print(f"Is blockchain valid after tampering Block 1? {my_blockchain.is_chain_valid()}")
    print("Notice that Block 2 and Block 3 are now invalid because their 'previous_hash' no longer matches the tampered Block 1's hash.")

    print("\n--- Recalculating hashes for subsequent blocks to make the chain valid again ---")
    # This demonstrates the "recompute" part of the challenge.
    # In a real blockchain, this would require re-mining or network consensus.
    for i in range(2, len(my_blockchain.chain)):
        current_block = my_blockchain.chain[i]
        previous_block = my_blockchain.chain[i-1]
        current_block.previous_hash = previous_block.hash
        current_block.hash = current_block.calculate_hash()
        print(f"Recomputed hash for Block {current_block.index}")

    my_blockchain.display_chain()
    print(f"Is blockchain valid after recomputing subsequent hashes? {my_blockchain.is_chain_valid()}")
    print("\nGoal: Understand how tampering one block affects the entire chain.")
    print("By changing Block 1's data, its hash changed. This broke the link with Block 2 (as Block 2's 'previous_hash' was based on the old hash of Block 1).")
    print("To make the chain valid again after tampering, you'd need to recompute the hashes of all subsequent blocks, which is computationally expensive in a real blockchain with Proof-of-Work.")
