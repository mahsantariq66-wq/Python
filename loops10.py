import time
wait_time=1
attempts=0
retries=5
while attempts < retries:
    print(f"Attempts: {attempts+1} - wait_time: {wait_time}")
    time.sleep(wait_time)
    wait_time*=2
    attempts+=1
print(f"Max Attempts Reached: {attempts}")

