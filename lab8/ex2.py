import asyncio


@asyncio.coroutine
def first_coroutine(future, N):
    count = 0
    for i in range(1, N + 1):
        count += i
    yield from asyncio.sleep(4)
    future.set_result("coroutine 1 result = " + str(count))


@asyncio.coroutine
def second_coroutine(future, N):
    count = 1
    for i in range(2, N + 1):
        count *= i
    yield from asyncio.sleep(3)
    future.set_result("coroutine 2 result = " + str(count))


def got_result(future):
    print(future.result())


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    future1 = asyncio.Future()
    future2 = asyncio.Future()

    tasks = [first_coroutine(future1, 5), second_coroutine(future2, 5)]

    future1.add_done_callback(got_result)
    future2.add_done_callback(got_result)

    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()

