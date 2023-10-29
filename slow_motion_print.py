import time

def delay_print(text, delay):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
        
delay_print("H", 0.2)
delay_print("e", 0.2)
delay_print("l", 0.2)
delay_print("l", 0.2)
delay_print("o", 0.2)

print(", ", end='', flush=True)
time.sleep(0.5)

delay_print("W", 0.2)
delay_print("o", 0.2)
delay_print("r", 0.2)
delay_print("l", 0.2)
delay_print("d", 0.2)
delay_print("!", 0.2)

print("\n")

