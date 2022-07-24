# python3
import itertools
from collections import namedtuple
from queue import PriorityQueue
AssignedJob = namedtuple("AssignedJob", ["worker", "started_at"])


def assign_jobs(n_workers, jobs):
    # TODO: replace this code with a faster algorithm.
    num_of_jobs = len(jobs)
    if n_workers >= num_of_jobs :
        return [AssignedJob(worker, 0) for worker in range(n_workers)]

    pq = PriorityQueue()
    result = []
    #start the process
    for worker_idx in range(n_workers):
        #The earlier the finish time, the hgiher the priority is
        pq.put((jobs[worker_idx], worker_idx))
        result.append(AssignedJob(worker_idx, 0))

    for i in range(n_workers, num_of_jobs):
        next_available_worker = pq.get()
        worker_idx = next_available_worker[1]
        current_time = next_available_worker[0]
        result.append(AssignedJob(worker_idx, current_time))
        pq.put((jobs[i]+current_time, worker_idx))

    return result



def main():
    n_workers, n_jobs = map(int, input().split())
    jobs = list(map(int, input().split()))
    assert len(jobs) == n_jobs

    # n_workers = 4
    # jobs = [1] * 20
    assigned_jobs = assign_jobs(n_workers, jobs)

    for job in assigned_jobs:
        print(job.worker, job.started_at)


if __name__ == "__main__":
    main()
