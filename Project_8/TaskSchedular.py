'''
Create a task scheduler that processes jobs in FIFO order with simulated delays.
    A simple FIFO task scheduler with optional per-task delay.
    enqueue: append to the back
    dequeue/process: pop from the front
'''
from collections import deque
import time

class TaskScheduler:
    def __init__(self, delay_seconds: float = 0.5):
        self._q = deque()
        self.delay = delay_seconds

    def add_task(self, task):
        self._q.append(task)

    def remove_task(self):
        if not self._q:
            return None
        return self._q.popleft()

    def list_tasks(self):
        return list(self._q)

# all process things are gpt additions i don't yet understand
    def process_next(self):
        """
        Process exactly one task in FIFO order with a simulated delay.
        Returns the processed task or None if queue is empty.
        """
        task = self.remove_task()
        if task is None:
            print("No tasks to process.")
            return None
        print(f"Processing: {task}")
        time.sleep(self.delay)  # simulated work
        print(f"Done:       {task}")
        return task

    def process_all(self):
        """Process until the queue is empty."""
        while self._q:
            self.process_next()
# gpt addition stops here


    def __len__(self):
        return len(self._q)

if __name__ == "__main__":
    q = TaskScheduler(delay_seconds=0.25)
    print(q)  # empty queue

    q.add_task("play video games")
    q.add_task("study python")
    q.add_task("gym")
    print("Queued:", q.list_tasks())

    q.process_next()  # processes "play video games"
    q.process_all()   # processes remaining in FIFO order

    print("Remaining:", q.list_tasks())