#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4

    for files in dir(hidden_4):
        if files[0] != "_":
            print(files)
