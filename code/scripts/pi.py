import random

EPOCH = 1000000

def calculate_pi(epoch):
    inCircle = 0
    for i in range(0,epoch):
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)
        dist = x*x + y*y
        if(dist <= 1):
            inCircle += 1
    return 4*(inCircle/epoch)

def main():
    pi = calculate_pi(EPOCH)
    print(pi)


if __name__ == "__main__":
    main()
