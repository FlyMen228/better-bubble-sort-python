from random import randint


def main():

    array = [randint(-500, 500) for _ in range(10000)]

    bubble_sort(array)

    print(*array)


def bubble_sort(array):

    for i in range(len(array) - 1):

        break_point = False

        min_index = i

        for j in range(i, len(array) - i - 1):

            if array[j] > array[j+1]:

                array[j], array[j+1] = array[j+1], array[j]

                break_point = True

            if array[j] < array[min_index]:

                min_index = j

        if break_point == False:

            break

        if min_index != i:

            array[i], array[min_index] = array[min_index], array[i]

    return array


if __name__ == "__main__":

    main()