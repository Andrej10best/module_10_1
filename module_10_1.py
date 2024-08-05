from time import sleep
from threading import Thread
from datetime import datetime


def wite_words(word_count, file_name):
    file = open(file_name, 'w', encoding='utf-8')
    for num_string in range(1, word_count + 1):
        file.write(f'Какое-то слово № {num_string}\n')
        sleep(0.1)
    file.close()
    print(f'Завершилась запись в файл {file_name}')


time_start = datetime.now()
wite_words(10, 'example1.txt')
wite_words(30, 'example2.txt')
wite_words(200, 'example3.txt')
wite_words(100, 'example4.txt')
time_end = datetime.now()
time_res = time_end - time_start
print(time_res)

time_start = datetime.now()
thr_1 = Thread(target=wite_words, args=(10, 'example5.txt'))
thr_2 = Thread(target=wite_words, args=(30, 'example6.txt'))
thr_3 = Thread(target=wite_words, args=(200, 'example7.txt'))
thr_4 = Thread(target=wite_words, args=(100, 'example8.txt'))

thr_1.start()
thr_2.start()
thr_3.start()
thr_4.start()

thr_1.join()
thr_2.join()
thr_3.join()
thr_4.join()

time_end = datetime.now()
time_res = time_end - time_start
print(time_res)