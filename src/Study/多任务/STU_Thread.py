# encoding:utf-8
import time
import threading


# 并行：真的多任务
# 并发：似的多任务

def dance():
    """跳舞"""
    for i in range(5):
        print("———正在跳舞———")
        time.sleep(1)


def sing():
    """唱歌"""
    for i in range(5):
        print("———RELAX———")
        time.sleep(1)


def main():
    t1 = threading.Thread(target=sing)
    t2 = threading.Thread(target=dance)
    t1.start()
    t2.start()


if __name__ == "__main__":
    main()
