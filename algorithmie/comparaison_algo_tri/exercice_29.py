import random
import time

# Tri Fusion (Merge Sort)
def merge_sort(arr):
    if len(arr) > 1:
        mid: int = len(arr) // 2
        left_array: list = arr[:mid]
        right_array: list = arr[mid:]

        merge_sort(left_array)
        merge_sort(right_array)

        left_index = right_index = main_index = 0

        while left_index < len(left_array) and right_index < len(right_array):
            if left_array[left_index] < right_array[right_index]:
                arr[main_index] = left_array[left_index]
                left_index += 1
            else:
                arr[main_index] = right_array[right_index]
                right_index += 1
            main_index += 1

        while left_index < len(left_array):
            arr[main_index] = left_array[left_index]
            left_index += 1
            main_index += 1

        while right_index < len(right_array):
            arr[main_index] = right_array[right_index]
            right_index += 1
            main_index += 1

# Tri par Insertion
def insertion_sort(arr):
    for current_index in range(1, len(arr)):
        key = arr[current_index]
        previous_index = current_index - 1
        while previous_index >= 0 and key < arr[previous_index]:
            arr[previous_index + 1] = arr[previous_index]
            previous_index -= 1
        arr[previous_index + 1] = key

# Génération aléatoire des tableaux de taille entre 100 et 1000
def generate_random_array():
    size = random.randint(100, 1000)
    return [random.randint(-10**9, 10**9) for _ in range(size)]

# Comparaison des temps d'exécution
def compare_execution_time(num_arrays):
    merge_sort_time = 0
    insertion_sort_time = 0

    for _ in range(num_arrays):
        random_array = generate_random_array()

        start_time = time.time()
        merge_sort(random_array.copy())  # Tri fusion
        merge_sort_time += time.time() - start_time

        start_time = time.time()
        insertion_sort(random_array.copy())  # Tri par insertion
        insertion_sort_time += time.time() - start_time

    merge_sort_avg_time = merge_sort_time / num_arrays
    insertion_sort_avg_time = insertion_sort_time / num_arrays

    return merge_sort_avg_time, insertion_sort_avg_time

# Comparaison des temps d'exécution sur 200 tableaux
merge_time, insertion_time = compare_execution_time(200)
print("Temps moyen d'exécution du tri fusion (Merge Sort) :", merge_time)
print("Temps moyen d'exécution du tri par insertion :", insertion_time)
