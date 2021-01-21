# ---
# python_callable: main
# ---

class Process1:
    def __init__(self):
        pass

    def call(self):
        return 'I am process__1 and yes, I ran.'


def main():
    p = Process1()
    return p.call()