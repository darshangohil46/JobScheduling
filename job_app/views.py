from django.shortcuts import render


# Create your views here.
class Job:
    def __init__(self, jobId, deadline, profit):
        self.jobId = jobId
        self.deadline = deadline
        self.profit = profit


# job scheduling algo
def schedule_jobs(jobs):
    jobs.sort(key=lambda x: x.profit, reverse=True)
    max_deadline = max(job.deadline for job in jobs) if jobs else 0
    slots = [False] * max_deadline
    scheduled_jobs = []
    print(slots, max_deadline)
    total_profit = 0

    for job in jobs:
        j = min(max_deadline, job.deadline) - 1
        print(j)
        while j >= 0:
            if not slots[j]:
                slots[j] = True
                scheduled_jobs.append(
                    {"jobId": job.jobId, "deadline": job.deadline, "profit": job.profit}
                )
                print(slots, scheduled_jobs)
                total_profit += job.profit
                break
            print(slots, scheduled_jobs, total_profit)
            j -= 1

    return scheduled_jobs, total_profit


def job_scheduler_view(request):
    scheduled_jobs = []
    total_profit = 0

    if request.method == "POST":
        job_ids = request.POST.getlist("jobId[]")
        deadlines = request.POST.getlist("deadline[]")
        profits = request.POST.getlist("profit[]")

        print(job_ids, deadlines, profits)
        jobs = [
            Job(job_ids[i], int(deadlines[i]), int(profits[i]))
            for i in range(len(job_ids))
        ]
        allJobs = jobs.copy()
        for j in jobs:
            print(j.jobId, j.deadline, j.profit)
        scheduled_jobs, total_profit = schedule_jobs(jobs)

        return render(
            request,
            "job_scheduler.html",
            {
                "jobs": allJobs,
                "scheduled_jobs": scheduled_jobs,
                "total_profit": total_profit,
            },
        )
    return render(request, "job_scheduler.html")
