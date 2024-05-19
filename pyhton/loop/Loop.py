import time

start_time = time.time()
count = 0

for i in range(200_000_000):
    count += 1

elapsed_time = (time.time() - start_time) * 1000  # Convert to milliseconds
print(f"Time taken: {elapsed_time:.3f} milliseconds to count: {count}")