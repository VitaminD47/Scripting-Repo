from ping3 import ping

response_time = ping("8.8.8.8")
if response_time is not None:
    print(f"Ping successful: {response_time:.2f} seconds")
else:
    print("Ping failed")
