import hashlib
import datetime
import time

class Block:
    def __init__(self, index, timestamp, data, previous_hash=''):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = 0  # Initialize nonce
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        # Concatenate all block properties to create a string
        # then encode it to bytes before hashing.
        block_string = str(self.index) + str(self.timestamp) + str(self.data) + \
                       str(self.previous_hash) + str(self.nonce)
        return hashlib.sha256(block_string.encode()).hexdigest()

    def mineBlock(self, difficulty):
        print("Mining block...")
        start_time = time.time()
        nonce_attempts = 0

        # Create the target prefix for the hash based on difficulty
        # e.g., if difficulty is 4, target_prefix = "0000"
        target_prefix = "0" * difficulty

        while self.hash[:difficulty] != target_prefix:
            self.nonce += 1
            self.hash = self.calculate_hash()
            nonce_attempts += 1
        
        end_time = time.time()
        time_taken = end_time - start_time

        print(f"Block mined: {self.hash}")
        print(f"Nonce attempts needed: {nonce_attempts}")
        print(f"Time taken to mine: {time_taken:.4f} seconds")

        return nonce_attempts, time_taken

# --- Example Usage ---

# Create a genesis block (first block in the chain)
genesis_block = Block(0, datetime.datetime.now(), "Genesis Block", "0")

# Set desired difficulty (e.g., 4 leading zeros)
difficulty_level = 4 

# Mine the genesis block
print("\n--- Mining Genesis Block ---")
genesis_block.mineBlock(difficulty_level)

# Create another block
block2 = Block(1, datetime.datetime.now(), "Transaction Data 1", genesis_block.hash)

# Mine the second block
print("\n--- Mining Second Block ---")
block2.mineBlock(difficulty_level)

# Experiment with higher difficulty
difficulty_level_higher = 5
print(f"\n--- Mining with higher difficulty ({difficulty_level_higher}) ---")
block3 = Block(2, datetime.datetime.now(), "Transaction Data 2", block2.hash)
block3.mineBlock(difficulty_level_higher)
