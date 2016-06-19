from multiprocessing import Pool
import argparse
import math
import time

class Task(object):
    def __init__(self, index, param):
        self.name = 'task'
        self.param = param
        self.index = index
        self.answer = None

    def __str__(self):
        return 'Task: {}, params: {}, answer: {}'.format(self.name, self.param, self.answer)

class PrimeTask(Task):
    def __init__(self, index, param):
        super(PrimeTask, self).__init__(index, param)
        self.name = 'prime'

    def __call__(self):
        for d in range(2, int(math.sqrt(self.param) + 1)):
            if self.param % d == 0:
                self.answer = False
                break
        self.answer = True

        with open('task{}.out'.format(self.index), 'w+') as f:
            f.write(str(self))

class CheckTask(Task):
    def __init__(self, index, param):
        super(CheckTask, self).__init__(index, param)
        self.name = 'check'

    def __call__(self):
        count = 0
        for i in range(self.param[0], self.param[1] + 1):
            if i % 2 == 0:
                count += 1

        self.answer = count
        with open('task{}.out'.format(self.index), 'w+') as f:
            f.write(str(self))

def perform(task):
    task()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file', type=str, required=True)
    parser.add_argument('-p', '--processes', type=int, default=2)
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
            a, b = tuple(task[1].split(' '))
            tasks.append(CheckTask(i, (int(a), int(b))))
        i += 1

    pool = Pool(processes=args.processes)

    begin_time = time.time()
    pool.map(perform, tasks)

    print(time.time() - begin_time)
    pool.close()
    pool.join()
