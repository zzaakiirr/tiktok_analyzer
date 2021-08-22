from apscheduler.schedulers.blocking import BlockingScheduler

from main import run_worker


if __name__ == '__main__':
    scheduler = BlockingScheduler()
    scheduler.add_job(run_worker, "interval", hours=3)

    scheduler.start()
