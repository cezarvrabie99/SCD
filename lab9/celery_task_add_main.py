import celery_task_add

if __name__ == "__main__":
    result = celery_task_add.add.delay(5, 10)
    print('Result=', result)
