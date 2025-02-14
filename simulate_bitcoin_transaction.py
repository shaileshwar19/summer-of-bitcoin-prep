import hashlib

def generate_transaction(sender, receiver, amount):
    transaction_data = f"{sender} -> {receiver}: {amount} BTC"
    transaction_hash = hashlib.sha256(transaction_data.encode()).hexdigest()
    return f"Transaction Hash: {transaction_hash}"

# Example Transaction
sender = "Alice"
receiver = "Bob"
amount = 0.005  # BTC

print(generate_transaction(sender, receiver, amount))
