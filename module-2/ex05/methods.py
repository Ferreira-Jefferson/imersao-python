import sys

if __name__ == "__main__":
    arg_str = sys.argv[1]
    print("São maíusculas?", arg_str.isupper())
    print("É númerico?", arg_str.isdigit())
    print("É ascii?", arg_str.isascii())
    print("É alfanumérico?", arg_str.isalnum())