import asyncio


#@asyncio.coroutine
async def factorial(number):
    f = 1
    for i in range(2, number + 1):
        print("Compute factorial(%s)" % i)
        #yield from asyncio.sleep(1)
        await asyncio.sleep(1)
        f *= i
    print("Result factorial %s! = %s" % (number, f))


#@asyncio.coroutine
async def fibonacci(number):
    a, b = 0, 1
    for i in range(number):
        print("Compute fibnacci(%s)" % i)
        #yield from asyncio.sleep(1)
        await asyncio.sleep(1)
        a, b = b, a + b
    print("Result fibnacci(%s) = %s" % (number, a))


if __name__ == "__main__":
    tasks = [asyncio.Task(factorial(10)), asyncio.Task(fibonacci(10))]
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()

