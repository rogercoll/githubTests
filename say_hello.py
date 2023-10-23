import sys

if len(sys.argv) != 2:
    print("Usage: python replace_slashes.py <path>")
    sys.exit(1)

argument = sys.argv[1]
argument = argument.replace('\\', '/')

print(argument)
