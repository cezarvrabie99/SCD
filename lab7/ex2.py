import asyncio
import datetime
import time


def function_1(end_time, loop):
    print("function 1 called")
    print(end_time)
    if(loop.time() + 1.0) < end_time:
        loop.call_later(1, function_2, end_time, loop)
    else:
        loop.stop()


def function_2(end_time, loop):
    print("function 2 called")
    print(end_time)
    if(loop.time() + 1.0) < end_time:
        loop.call_later(1, function_3, end_time, loop)
    else:
        loop.stop()


def function_3(end_time, loop):
    print("function 3 called")
    print(end_time)
    if(loop.time() + 1.0) < end_time:
        loop.call_later(1, function_1, end_time, loop)
    else:
        loop.stop()


def function_4(end_time, loop):
    print("function 4 called")
    print(end_time)
    if(loop.time() + 1.0) < end_time:
        loop.call_later(1, function_4, end_time, loop)
    else:
        loop.stop()


loop = asyncio.get_event_loop()

end_loop_1 = loop.time() + 9.0
loop.call_soon(function_1, end_loop_1, loop)

loop.run_forever()
loop.close()
