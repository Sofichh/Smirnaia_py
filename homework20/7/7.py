from lifo import Lifo, TaskManager
queue = Lifo()
lstt = []
manager = TaskManager()
manager.new_task("сделать уборку", 4, queue)
manager.new_task("помыть посуду", 4, queue)
manager.new_task("отдохнуть", 1, queue)
manager.new_task("поесть", 2, queue)
manager.new_task("сдать дз", 2, queue)
queue.printst()
manager.completedtask(queue)
queue.printst()
