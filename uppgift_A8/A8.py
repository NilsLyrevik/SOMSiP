import time 

def f():
    for i in range(5,15):
        print("FREQ ", i*100)
        time.sleep(0.5)
    print("Done")

if __name__ == "__main__":
    f()
