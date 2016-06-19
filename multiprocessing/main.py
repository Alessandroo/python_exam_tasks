from multiprocessing import JoinableQueue, Queue, Process
import math
import argparse
import time

class Worker(Process):
    def __init__(self, queue, index):
        super(Worker, self).__init__()
        self._queue = queue
        self._results = []
        self._index = index

    def run(self):
        while not self._queue.empty():
            task = self._queue.get()
            task()
            self._results.append(str(task))
            self._queue.task_done()
        with open('task{}.out'.format(self._index), 'w+') as f:
            f.write('\n'.join(self._results))

class Task(object):
    def __init__(self, param):
        self.name = 'task'
        self.answer = None
        self._param = param

    def __str__(self):
        return 'Task: {}, params: {}, answer: {}'.format(self.name, self._param, self.answer)

class CheckTask(Task):
    def __init__(self, param):
        super(CheckTask, self).__init__(param)
        self.name = 'check'

    def __call__(self):
        a = self._param[0]
        b = self._param[1]

        count = 0
        for x in range(a, b + 1):
            if x % 2 == 0:
                count += 1

        self.answer = count

class PrimeTask(Task):
    def __init__(self, param):
        super(PrimeTask, self).__init__(param)
        self.name = 'prime'

    def __call__(self):
        n = self._param
        for x in range(2, int(math.sqrt(n)) + 1):
            if n % x == 0:
                self.answer = False
                return

        self.answer = True


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file', type=str, required=True)
    parser.add_argument('-p', '--processes', type=int, default=2)

    args = parser.parse_args()

    queue = JoinableQueue()
    workers = [Worker(queue, i) for i in range(args.processes)]
    for worker in workers:
        worker.start()

    tasks_file = open(args.file, 'r')

    begin_time = time.time()
    while True:
        task_str = tasks_file.readline()
        if not task_str:
            break
        task = task_str.split('\t')
        if task[0] == 'prime':
            queue.put(PrimeTask(int(task[1])))
        elif task[0] == 'check':
            a, b = task[1].split(' ')
            queue.put(CheckTask((int(a), int(b))))

    queue.join()
    print(time.time() - begin_time)
