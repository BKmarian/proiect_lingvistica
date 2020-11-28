import time

MAX_COST = 2


def get_input():
    with open("corola.300.20.vec", "r", encoding="iso-8859-2") as ins:
        for line in ins:
            if line == "250942 300\n":
                continue
            word = line.rstrip().rsplit(' ')[0]
            yield word


def levenshtein(word1, word2):
    columns = len(word1) + 1
    rows = len(word2) + 1

    # build first row
    current_row = [0]
    for column in range(1, columns):
        current_row.append(current_row[column - 1] + 1)

    for row in range(1, rows):
        previous_row = current_row
        current_row = [previous_row[0] + 1]

        for column in range(1, columns):

            insert_cost = current_row[column - 1] + 1
            delete_cost = previous_row[column] + 1

            if word1[column - 1] != word2[row - 1]:
                replace_cost = previous_row[column - 1] + 1
            else:
                replace_cost = previous_row[column - 1]

            current_row.append(min(insert_cost, delete_cost, replace_cost))

    return current_row[-1]


TARGET = "copilc"


def search():
    results = []
    for word in list(get_input()):
        cost = levenshtein(TARGET, word)

        if cost <= MAX_COST:
            results.append((word, cost))

    results.sort(key=lambda tup: tup[1], reverse=True)
    return results


def main():
    start = time.time()
    results = search()
    end = time.time()

    for result in results:
        print(result)

    print("Search took %g s" % (end - start))


if __name__ == '__main__':
    main()
