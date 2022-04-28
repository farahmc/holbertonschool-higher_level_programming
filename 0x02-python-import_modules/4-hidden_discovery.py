#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4

    directories = dir(hidden_4)
    for name in directories:
        if name[0:2] == '__':
            continue
        print(name)
