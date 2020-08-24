__author__ = 'Mihail Mihaylov'
import sys
import unittest

from anagram import *
from array_pair_sum import *
from factorial import *
from fibonacci import *
from finder import *
from largest_continues_sum import *
from queue import *
from sentence_reversal import *
from stack import *
from string_compression import *
from unique_characters_in_string import *
from deque import *
from balance_parentheses_check import *
from linked_lists import *
from recursion import *


class TestAnagrams(unittest.TestCase):
    """Class that test anagram"""

    def test_anagram(self):
        """Test first anagram function."""
        self.assertEqual(is_anagram('gogogo', 'gggooo'), True)
        self.assertEqual(is_anagram('a', 'b'), False)
        self.assertEqual(is_anagram('clint eastwood', 'old west action'), True)
        self.assertEqual(is_anagram(' ', ' '), True)

    def test_second_anagram(self):
        """Test second anagram function."""
        self.assertEqual(is_anagram2('gogogo', 'gggooo'), True)
        self.assertEqual(is_anagram2('a', 'b'), False)
        self.assertEqual(is_anagram2('clint eastwood', 'old west action'), True)
        self.assertEqual(is_anagram2(' ', ' '), True)


class TestPairSum(unittest.TestCase):
    """"Class to test pair sum"""
    def test_pair_sum(self):
        self.assertEqual(pair_sum([1, 2, 3, 4], 4), '(1, 3)')
        self.assertEqual(pair_sum([1, 3, 2, 2], 4), '(1, 3)(2, 2)')
        self.assertEqual(pair_sum([1, 2, 4, 6, 7], 50), '')
        self.assertEqual(pair_sum([], 50), None)


class TestFactorial(unittest.TestCase):
    """"Class to factorial algorithm"""
    def test_factorial_recursive(self):
        """"Test recursive factorial"""
        self.assertEqual(fact(10), 3628800)
        self.assertEqual(fact(5), 120)
        self.assertEqual(fact(0), 1)

    def test_factorial_non_recursive(self):
        """"Test non recursive factorial"""
        self.assertEqual(fact_non_recursive(10), 3628800)
        self.assertEqual(fact_non_recursive(5), 120)
        self.assertEqual(fact_non_recursive(0), 1)


class TestFibonacci(unittest.TestCase):
    """"Class to fibonacci algorithm"""

    def test_fibonacci_generator(self):
        """"Test fibonacci generator"""
        self.assertEqual(get_fibonacci_with_generator(5), [0, 1, 1, 2, 3])
        self.assertEqual(get_fibonacci_with_generator(10), [0, 1, 1, 2, 3, 5, 8, 13, 21, 34])

    def test_get_fibonacci_recursive(self):
        """"Test fibonacci recursive 1"""
        self.assertEqual(get_fibonacci(fib_recursive, 5,), [0, 1, 1, 2, 3])
        self.assertEqual(get_fibonacci(fib_recursive, 10), [0, 1, 1, 2, 3, 5, 8, 13, 21, 34])

    def test_get_fibonacci_recursive2(self):
        """"Test fibonacci recursive 2"""
        self.assertEqual(get_fibonacci(fib_recursive2, 5), [0, 1, 1, 2, 3])
        self.assertEqual(get_fibonacci(fib_recursive2, 10), [0, 1, 1, 2, 3, 5, 8, 13, 21, 34])


class TestFinder(unittest.TestCase):
    """Test class for finder"""
    def test_pair_sum(self):
        self.assertEqual(finder([1, 2, 3, 4, 5, 6, 7], [1, 2, 3, 4, 6, 7]), 5)
        self.assertEqual(finder([1, 2, 3], [2]), 1)
        self.assertEqual(finder([7, 6, 5, 4], [5, 6, 4]), 7)

    def test_second_pair_sum(self):
        """Test class for finder 2"""
        self.assertEqual(finder2([1, 2, 3, 4, 5, 6, 7], [1, 2, 3, 4, 6, 7]), 5)
        self.assertEqual(finder2([1, 2, 3], [2]), 1)
        self.assertEqual(finder2([7, 6, 5, 4], [5, 6, 4]), 7)


class TestLargestSum(unittest.TestCase):
    """"Class to test largest continues sum"""
    def test_pair_sum(self):
        self.assertEqual(large_continues_sum([1, 2, -1, 3, 4, -1]), 9)
        self.assertEqual(large_continues_sum([1, 2, -1, 3, 4, 10, 10, -10, -1]), 29)
        self.assertEqual(large_continues_sum([-1, 1]), 1)
        self.assertEqual(large_continues_sum([]), 0)


class TestQueue(unittest.TestCase):
    """Class that test Queue class"""

    def setUp(self):
        self.queue = Queue()

    def tearDown(self):
        del self.queue

    def test_queue_initialize(self):
        """Test that queue can be initialized"""
        self.assertTrue(isinstance(self.queue, Queue))

    def test_is_empty(self):
        """Test is_empty method"""
        self.assertTrue(self.queue.is_empty())
        self.queue.enqueue(10)
        self.assertFalse(self.queue.is_empty())

    def test_enqueue(self):
        """Test enqueue method"""
        self.queue.enqueue(10)
        self.assertEqual(self.queue.items, [10])
        self.queue.enqueue(20)
        self.assertEqual(self.queue.items, [20, 10])

    def test_dequeue(self):
        """Test dequeue method"""
        self.queue.enqueue(10)
        self.queue.enqueue(20)
        self.assertEqual(self.queue.dequeue(), 10)

    def test_size_method(self):
        """Test size method returns correct len"""
        self.assertEqual(self.queue.size(), 0)
        self.queue.enqueue(10)
        self.assertEqual(self.queue.size(), 1)


class TestSentenceReversal(unittest.TestCase):
    """"Class to test Sentence Reversal"""
    def test_sentence_reversal1(self):
        """"Test sequence reversal1"""
        self.assertEqual(sentence_reversal1('    space before'), 'before space')
        self.assertEqual(sentence_reversal1('   Hello John    how are you   '), 'you are how John Hello')
        self.assertEqual(sentence_reversal1('1'), '1')

    def test_sentence_reversal2(self):
        """"Test sequence reversal2"""
        self.assertEqual(sentence_reversal1('    space before'), 'before space')
        self.assertEqual(sentence_reversal1('   Hello John    how are you   '), 'you are how John Hello')
        self.assertEqual(sentence_reversal1('1'), '1')


class TestStack(unittest.TestCase):

    def setUp(self):
        self.stack = Stack()

    def tearDown(self):
        del self.stack

    def test_stack_initialize(self):
        """Test that stack can be initialized"""
        self.assertTrue(isinstance(self.stack, Stack))

    def test_push_method(self):
        """Test push method works"""
        self.stack.push(5)
        self.assertEqual(self.stack.items, [5])
        self.stack.push(10)
        self.assertEqual(self.stack.items, [5, 10])

    def test_is_empty_method(self):
        """Test is_empty method"""
        self.assertTrue(self.stack.is_empty())
        self.stack.push(5)
        self.assertFalse(self.stack.is_empty())
        self.stack.pop(0)
        self.assertTrue(self.stack.is_empty())

    def test_pop_method(self):
        """Test pop method returns requested item"""
        self.stack.push(10)
        self.assertEqual(self.stack.pop(0), 10)

    def test_pop_method_raise_index_exception(self):
        """Test pop method raises index out of range exception"""
        self.stack.push(10)
        self.assertRaises(IndexError, self.stack.pop, 2)

    def test_peek_method(self):
        """Test peek method returns requested item"""
        self.stack.push(10)
        self.assertEqual(self.stack.peek(), 10)

    def test_peek_method_raises_index_exception(self):
        """Test peek method raises index out of range exception"""
        self.assertRaises(IndexError, self.stack.peek)

    def test_size_method(self):
        """Test size method returns correct len"""
        self.assertEqual(self.stack.size(), 0)
        self.stack.push(10)
        self.assertEqual(self.stack.size(), 1)


class TestStringCompression(unittest.TestCase):
    """"Class to test string compression"""
    def test_string_compression(self):
        """"Test string compression"""
        self.assertEqual(string_compression(''), '')
        self.assertEqual((string_compression('AAAA')), 'A4')
        self.assertEqual(string_compression('AABBCC'), 'A2B2C2')
        self.assertEqual(string_compression('BaRdBP'), 'B2a1R1d1P1')


class TestUniqueCharacters(unittest.TestCase):
    """"Class to determine if string contains unique characters"""
    def test_unique_characters1(self):
        """"Test unique characters v1"""
        self.assertEqual(find_unique_characters_in_str1('abcd'), True)
        self.assertEqual(find_unique_characters_in_str1(''), True)
        self.assertEqual(find_unique_characters_in_str1('gaa'), False)

    def test_unique_characters2(self):
        """"Test unique characters v2"""
        self.assertEqual(find_unique_characters_in_str2('abcd'), True)
        self.assertEqual(find_unique_characters_in_str2(''), True)
        self.assertEqual(find_unique_characters_in_str2('gaa'), False)


class TestDeque(unittest.TestCase):
    """Class to test Deque"""

    def setUp(self):
        self.deque = Deque()

    def tearDown(self):
        del self.deque

    def test_deque_initialize(self):
        """Test that deque can be initialized"""
        self.assertTrue(isinstance(self.deque, Deque))

    def test_is_empty_method(self):
        """Test is_empty method"""
        self.assertTrue(self.deque.is_empty())
        self.deque.add_front(5)
        self.assertFalse(self.deque.is_empty())
        self.deque.remove_front()
        self.assertTrue(self.deque.is_empty())

    def test_add_front(self):
        """Test add front method"""
        self.deque.add_front(5)
        self.assertEqual(self.deque.items, [5])
        self.deque.add_front(10)
        self.assertEqual(self.deque.items, [5, 10])

    def test_add_read(self):
        """Test add rear method"""
        self.deque.add_rear(5)
        self.assertEqual(self.deque.items[0], 5)
        self.deque.add_rear(10)
        self.assertEqual(self.deque.items[0], 10)

    def test_remove_front(self):
        """Test remove front method"""
        self.deque.add_front(5)
        self.deque.add_front(10)
        self.assertEqual(self.deque.remove_front(), 10)
        self.assertEqual(self.deque.remove_front(), 5)

    def test_remove_rear(self):
        """Test remove rear method"""
        self.deque.add_front(5)
        self.deque.add_front(10)
        self.assertEqual(self.deque.remove_rear(), 5)
        self.assertEqual(self.deque.remove_rear(), 10)

    def test_size_method(self):
        """Test size method returns correct len"""
        self.assertEqual(self.deque.size(), 0)
        self.deque.add_front(10)
        self.assertEqual(self.deque.size(), 1)


class TestBalanceParentheses(unittest.TestCase):
    """Class to test balance parentheses checker"""

    def test_balance_parentheses_check(self):
        """Test balance parentheses algorithm"""
        self.assertFalse(balance_parentheses_check('[](){([[[]]])}('))
        self.assertTrue(balance_parentheses_check('[{{{(())}}}]((()))'))
        self.assertFalse(balance_parentheses_check('[[[]])]'))
        self.assertTrue(balance_parentheses_check('[]'))
        self.assertFalse(balance_parentheses_check('[[]'))
        self.assertTrue(balance_parentheses_check(''))


class TestSinglyLinkedList(unittest.TestCase):

    def test_cycle_check(self):
        """Test that singly linked list cycle check returns correct value"""
        # CREATE CYCLE LIST
        node1 = Node(1)
        node2 = Node(2)
        node3 = Node(3)

        node1.next_node = node2
        node2.next_node = node3
        node3.next_node = node1  # Cycle Here!

        # CREATE NON CYCLE LIST
        x = Node(1)
        y = Node(2)
        z = Node(3)

        x.next_node = y
        y.next_node = z

        self.assertTrue(node1.cycle_check(node2))
        self.assertFalse(x.cycle_check(x))

    def test_reverse(self):
        """Test that linked list can be reversed"""
        node1 = Node(1)
        node2 = Node(2)
        node3 = Node(3)
        node4 = Node(4)

        node1.next_node = node2
        node2.next_node = node3
        node3.next_node = node4
        #  the attribute next_node of node4 has no value
        self.assertRaises(AttributeError, node4.next_node)
        node1.reverse(node1)
        self.assertEqual(node4.next_node.value, 3)
        # After reverse the attribute next_node of node1 has no value
        self.assertRaises(AttributeError, node1.next_node)

    def test_get_nth_to_last_node(self):
        node1 = Node(1)
        node2 = Node(2)
        node3 = Node(3)
        node4 = Node(4)
        node5 = Node(5)

        node1.next_node = node2
        node2.next_node = node3
        node3.next_node = node4
        node4.next_node = node5

        result = node1.get_nth_to_last_node(2, node1)
        self.assertEqual(result.value, 4)


class Recursion(unittest.TestCase):
    """Class to test recursive functions"""

    def test_recursive_sum(self):
        self.assertEqual(recursive_sum(4), 10)
        self.assertEqual(recursive_sum(5), 15)
        self.assertEqual(recursive_sum(0), 0)

    def test_sum_func(self):
        self.assertEqual(sum_func(4321), 10)
        self.assertEqual(sum_func(0), 0)
        self.assertEqual(sum_func(1), 1)

    def test_word_split(self):
        self.assertEqual(word_split('themanran', ['the', 'ran', 'man']), ['the', 'man', 'ran'])
        self.assertEqual(word_split('ilovedogsJohn', ['i', 'am', 'a', 'dogs', 'lover', 'love', 'John']),
                         ['i', 'love', 'dogs', 'John'])
        self.assertEqual(word_split('', []), [])


if __name__ == '__main__':
    unittest.main(testRunner=unittest.TextTestRunner(verbosity=2, stream=sys.stdout))
