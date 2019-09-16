

if __name__ == '__main__':

    with open("crawled.txt", "r") as f:
        crawled = f.read()
        crawled = [e for e in crawled.split(",")]

    with open("request.txt", "r") as f:
        request = f.read()
        request = [e for e in request.split(",")]

    included = [e for e in request if e in crawled]
    not_included = [e for e in request if not e in crawled]

    print("INCLUDED")
    print(included)
    print("NOT INCLUDED")
    print(not_included)