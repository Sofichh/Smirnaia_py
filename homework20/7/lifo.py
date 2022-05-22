class Lifo:

    def __init__(self):
        self.lst = []

    def add(self, elem):
        self.lst.append(elem)

    def get(self):
        return self.lst.pop()

    def printst(self):
        print('Результат:')
        self.lst = sorted(self.lst)
        for n in range(len(self.lst)):
            if type(self.lst[n][1]) == tuple:
                print(self.lst[n][0], '; '.join(self.lst[n][1]))
            else:
                print(self.lst[n][0], self.lst[n][1])
        self.lst = sorted(self.lst, reverse=True)
        print('\n')


class TaskManager:

    def new_task(self, name, prior, que):
        que.add((prior, name))

    def completedtask(self, que):
        que.get()
