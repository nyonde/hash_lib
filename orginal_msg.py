# hash_lib

import hashlib

# The original message
original_message = "Hello, world!"

# Calculate the hash of the original message
original_hash = hashlib.sha256(original_message.encode())

# The modified message
modified_message = "Hello, world! How are you?"

# Calculate the hash of the modified message
modified_hash = hashlib.sha256(modified_message.encode())

# Compare the original hash and the modified hash
if original_hash == modified_hash:
    print("The message has not been modified.")
else:
    print("The message has been modified.")
