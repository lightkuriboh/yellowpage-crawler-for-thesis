
import queue
import threading


class ThreadPool:
    class Thread(threading.Thread):
        def __init__(self, func, *args):
            threading.Thread.__init__(self, target=func, args=args)
            self.start()

    @staticmethod
    def looking_for_job(job_queue: queue.Queue):
        while True:
            task, call_back, kwargs = job_queue.get()
            task(**kwargs)
            call_back()

    def __init__(self, n_workers: int):
        self.task_queue = queue.Queue()
        self.workers = []
        for _ in range(n_workers):
            self.workers.append(ThreadPool.Thread(ThreadPool.looking_for_job, self.task_queue))

    def enqueue(self, job, call_back, **kwargs):
        self.task_queue.put((job, call_back, kwargs))

    def close(self):
        self.task_queue.join()

