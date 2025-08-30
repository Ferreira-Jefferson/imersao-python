import sys

if __name__ == "__main__":
    try:
        if len(sys.argv) > 1:
            value = sys.argv[1]
            print(float(value))
    except ValueError:
        print("conversion impossible")

