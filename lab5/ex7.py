import multiprocessing


def create_items(pipe):
    endA, _ = pipe
    for item in range(10):
        endA.send(item)
    endA.close()


def multiply_items(pipeAB, pipeCD):
    endA, endB = pipeAB
    endA.close()
    endC, _ = pipeCD
    try:
        while True:
            item = endB.recv()
            endC.send(item * item)
    except EOFError:
        endC. close()


if __name__ == '__main__':
    pipeAB = multiprocessing.Pipe(True)
    process_1 = multiprocessing.Process(target=create_items, args=(pipeAB,))
    process_1.start()

    pipeCD = multiprocessing.Pipe(True)
    process_2 = multiprocessing. Process (target=multiply_items, args=(pipeAB, pipeCD,))
    process_2.start()

    pipeAB[0].close()
    pipeCD[0].close()

    try:
        while True:
            print (pipeCD[1].recv())
    except EOFError:
        print ("End")
