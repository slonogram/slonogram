from sys import argv, exit

try:
    to_import = argv[1]
except IndexError:
    print("usage: examples <example_name>")
    exit(1)

__import__(f"examples.{to_import}")
