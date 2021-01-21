# ---
# dependencies:
#   - process__1
# python_callable: main
# ---

class Process2:
    def __init__(self):
        pass

    def call(self):
        return 'Hey I fucking ran too, whussup.'


def main():
    p = Process2()
    return p.call()