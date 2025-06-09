import random

def simulate_consensus_mechanisms():
    """
    Simulates PoW, PoS, and DPoS consensus mechanisms
    and prints the selected validator and an explanation.
    """

    # Create mock objects for 3 validators
    # For simplicity, we'll use a dictionary for each validator
    # and a list to hold all validators.
    validators = []

    # Miner for PoW (power: random value)
    validators.append({
        'id': 'miner_1',
        'type': 'PoW',
        'power': random.randint(100, 1000)  # Random power value
    })

    # Staker for PoS (stake: random value)
    validators.append({
        'id': 'staker_1',
        'type': 'PoS',
        'stake': random.randint(50, 500)  # Random stake value
    })

    # Voters for DPoS (mock accounts voting)
    # We'll represent voters as a list of dictionaries with their votes
    dpos_voters = [
        {'account': 'voter_A', 'votes_for': 'delegate_X'},
        {'account': 'voter_B', 'votes_for': 'delegate_Y'},
        {'account': 'voter_C', 'votes_for': 'delegate_X'},
        {'account': 'voter_D', 'votes_for': 'delegate_Z'},
        {'account': 'voter_E', 'votes_for': 'delegate_Y'},
        {'account': 'voter_F', 'votes_for': 'delegate_X'},
    ]

    # --- Simulate ---

    # For PoW: Select validator with highest power
    selected_pow_validator = None
    max_power = -1
    for validator in validators:
        if validator['type'] == 'PoW' and validator['power'] > max_power:
            max_power = validator['power']
            selected_pow_validator = validator

    # For PoS: Select validator with highest stake
    selected_pos_validator = None
    max_stake = -1
    for validator in validators:
        if validator['type'] == 'PoS' and validator['stake'] > max_stake:
            max_stake = validator['stake']
            selected_pos_validator = validator

    # For DPoS: Randomly choose a delegate based on most votes
    # First, tally the votes for each delegate
    delegate_votes = {}
    for voter in dpos_voters:
        delegate_name = voter['votes_for']
        delegate_votes[delegate_name] = delegate_votes.get(delegate_name, 0) + 1

    # Find the delegate(s) with the maximum votes
    if delegate_votes:
        max_votes = 0
        for delegate, votes in delegate_votes.items():
            if votes > max_votes:
                max_votes = votes

        delegates_with_max_votes = [
            delegate for delegate, votes in delegate_votes.items() if votes == max_votes
        ]

        # If there's a tie, randomly choose one of the top delegates
        selected_dpos_delegate = random.choice(delegates_with_max_votes)
    else:
        selected_dpos_delegate = "No delegates voted for"


    # --- Output ---

    # PoW Output
    print("--- Proof of Work (PoW) ---")
    if selected_pow_validator:
        print(f"Selected validator: {selected_pow_validator['id']}")
        print(f"Power: {selected_pow_validator['power']}")
        print("console.log explanation: In PoW, the validator with the highest 'power' (representing computational effort) is selected to propose the next block.")
    else:
        print("No PoW validator found.")
    print("-" * 30)

    # PoS Output
    print("--- Proof of Stake (PoS) ---")
    if selected_pos_validator:
        print(f"Selected validator: {selected_pos_validator['id']}")
        print(f"Stake: {selected_pos_validator['stake']}")
        print("console.log explanation: In PoS, the validator with the highest 'stake' (representing economic interest) is selected to propose the next block.")
    else:
        print("No PoS validator found.")
    print("-" * 30)

    # DPoS Output
    print("--- Delegated Proof of Stake (DPoS) ---")
    print(f"Selected delegate: {selected_dpos_delegate}")
    print(f"Delegate votes: {delegate_votes}")
    print("console.log explanation: In DPoS, token holders vote for delegates, and the delegate(s) with the most votes are chosen to validate transactions. If there's a tie, one is randomly selected from the top contenders.")
    print("-" * 30)

    print("\nGoal: Compare decision-making in various consensus mechanisms")


if __name__ == "__main__":
    simulate_consensus_mechanisms()
