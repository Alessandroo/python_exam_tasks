from multiprocessing import Pool
import argparse
import math
import time

class PrimeTask(object):
    def __init__(self, index, num):
        self.number = num
        self.index = index
        self.answer = None

    def perform(self):
        for d in range(2, int(math.sqrt(self.number) + 1)):
            if self.number % d == 0:
                self.answer = False
                break
        self.answer = True

        with open('task{}.out'.format(self.index), 'w+') as f:
            f.write(str(self))

    def __str__(self):
        return 'Task: {}, params: {}, answer: {}'.format('prime', self.number, self.answer)


class CheckTask(object):
    def __init__(self, index, a, b):
        self.a = a
        self.b = b
        self.index = index
        self.answer = None

    def perform(self):
        count = 0
        # import ipdb; ipdb.set_trace()
        for i in range(self.a, self.b + 1):
            if i % 2 == 0:
                count += 1

        self.answer = count
        with open('task{}.out'.format(self.index), 'w+') as f:
            f.write(str(self))

    def __str__(self):
        return 'Task: {}, params: {}, answer: {}'.format('check', (self.a, self.b), self.answer)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file', type=str, required=True)
    parser.add_argument('-p', '--processes', type=int, default=10)
    args = parser.parse_args()

    processes_count = args.processes
    filename = args.file

    tasks = []

    tasks_file = open(filename, 'r')
    i = 0
    while True:
        line = tasks_file.readline()
        if not line:
            break
        task = line.split('\t')
        if task[0] == 'prime':
            tasks.append(PrimeTask(i, int(task[1])))
        elif task[0] == 'check':
            # import ipdb; ipdb.set_trace()
            a, b = tuple(task[1].split(' '))
            tasks.append(CheckTask(i, int(a), int(b)))
        i += 1

    begin_time = time.time()
    for task in tasks:
        task.perform()

    print(time.time() - begin_time)
    # pool.join()
