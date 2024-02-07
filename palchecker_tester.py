import palchecker
import unittest


class T0_TestingQueue(unittest.TestCase):

    def test_basic_enqueue(self):
        # testing the basic enqueue operation
        print("\n")
        q = palchecker.Queue()
        q.enqueue(1)
        q.enqueue(2)
        q.enqueue(3)
        q.enqueue(4)

        self.assertEqual(q.__str__(), '[1, 2, 3, 4]')

    def test_is_empty_false(self):
        # testing if queue is empty
        print("\n")
        s = palchecker.Queue()
        s.enqueue("4")
        print("return false if the queue is not empty")
        self.assertEqual(s.isEmpty(), False)

    def test_is_empty_true(self):
        # testing if queue is empty
        print("\n")
        s = palchecker.Queue()
        print("return true if the queue is empty")
        self.assertEqual(s.isEmpty(), True)

    def test_dequeue_normal(self):
        # testing the dequeue operation
        print("\n")
        q = palchecker.Queue()
        q.enqueue(1)
        q.enqueue(2)

        self.assertEqual(q.dequeue(), 1)

    def test_dequeue_empty(self):
        # testing the dequeue operation on empty queue
        print("\n")
        q = palchecker.Queue()

        with self.assertRaises(Exception):
            q.dequeue()

class T1_TestingStack(unittest.TestCase):

    def test_is_empty_false(self):
        # testing if stack is empty
        print("\n")
        s = palchecker.Stack()
        s.push("4")
        print("return false if the stack is not empty")
        self.assertEqual(s.isEmpty(), False)

    def test_is_empty_true(self):
        # testing if stack is empty
        print("\n")
        s = palchecker.Stack()
        print("return true if the stack is empty")
        self.assertEqual(s.isEmpty(), True)

    def test_basic_push(self):
        # testing the basic push operation
        print("\n")
        q = palchecker.Stack()
        q.push(1)
        q.push(2)
        q.push(3)
        q.push(4)

        self.assertEqual(q.__str__(), '[4, 3, 2, 1]')

    def test_pop_empty(self):
        # testing the pop operation on empty stack
        print("\n")
        s = palchecker.Stack()

        with self.assertRaises(Exception):
            s.pop()

    def test_dequeue_normal(self):
        # testing the dequeue operation
        print("\n")
        s = palchecker.Stack()
        s.push(1)
        s.push(2)

        self.assertEqual(s.pop(), 2)


class T2_TestingPalindrome(unittest.TestCase):

    def test_basic_string(self):
        # testing with basic string
        print("\n")
        string = "hello"
        p = palchecker.isPalindrome(string)
        print("The string being tested is -> ", string)
        self.assertEqual(p, False)

    def test_harder_string(self):
        # testing with harder string
        print("\n")
        string = "TaCo CaT"
        p = palchecker.isPalindrome(string)
        print("The string being tested is -> ", string)
        self.assertEqual(p, True)

    def test_number_string(self):
        # testing with numbers
        print("\n")
        string = "123454321"
        p = palchecker.isPalindrome(string)
        print("The string being tested is -> ", string)
        self.assertEqual(p, True)

    def test_symbol_string(self):
        # testing with symbols
        print("\n")
        string = "&%$%&"
        p = palchecker.isPalindrome(string)
        print("The string being tested is -> ", string)
        self.assertEqual(p, True)


class T3_TestingQueue(unittest.TestCase):

    def test_basic_enqueue(self):
        # testing the basic enqueue operation
        print("\n")
        q = palchecker.TwoStackQueue()
        q.enqueue(1)
        q.enqueue(2)
        q.enqueue(3)
        q.enqueue(4)

        self.assertEqual(q.__str__(), '[1, 2, 3, 4]')

    def test_is_empty_false(self):
        # testing if queue is empty
        print("\n")
        s = palchecker.TwoStackQueue()
        s.enqueue("4")
        print("return false if the queue is not empty")
        self.assertEqual(s.isEmpty(), False)

    def test_is_empty_true(self):
        # testing if queue is empty
        print("\n")
        s = palchecker.TwoStackQueue()
        print("return true if the queue is empty")
        self.assertEqual(s.isEmpty(), True)

    def test_dequeue_normal(self):
        # testing the dequeue operation
        print("\n")
        q = palchecker.TwoStackQueue()
        q.enqueue(1)
        q.enqueue(2)

        self.assertEqual(q.dequeue(), 1)

    def test_dequeue_empty(self):
        # testing the dequeue operation on empty queue
        print("\n")
        q = palchecker.TwoStackQueue()

        with self.assertRaises(Exception):
            q.dequeue()


class T4_TestingPalindromeEC(unittest.TestCase):

    def test_basic_string(self):
        # testing with basic string
        print("\n")
        string = "hello"
        p = palchecker.isPalindromeEC(string)
        print("The string being tested is -> ", string)
        self.assertEqual(p, False)

    def test_harder_string(self):
        # testing with harder string
        print("\n")
        string = "TaCo CaT"
        p = palchecker.isPalindromeEC(string)
        print("The string being tested is -> ", string)
        self.assertEqual(p, True)

    def test_number_string(self):
        # testing with numbers
        print("\n")
        string = "123454321"
        p = palchecker.isPalindromeEC(string)
        print("The string being tested is -> ", string)
        self.assertEqual(p, True)

    def test_symbol_string(self):
        # testing with symbols
        print("\n")
        string = "&%$%&"
        p = palchecker.isPalindromeEC(string)
        print("The string being tested is -> ", string)
        self.assertEqual(p, True)


if __name__ == '__main__':
    unittest.main()
