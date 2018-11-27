from Python.Coding_Puzzles_Challenges.CodeWars.CW_Test import Test


class Dictionary:

    def __init__(self, words):
        self.words = words

    def find_most_similar(self, term):
        term = sorted(term)

        for word in self.words:
            word = sorted(word)



if __name__ == '__main__':
    words = ['cherry', 'peach', 'pineapple', 'melon', 'strawberry', 'raspberry', 'apple', 'coconut', 'banana']
    test_dict = Dictionary(words)
    Test.assert_equals(test_dict.find_most_similar('strawbery'), 'strawberry')
    Test.assert_equals(test_dict.find_most_similar('berry'), 'cherry')
Test.assert_equals(test_dict.find_most_similar('aple'), 'apple')                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        AZAZAZAZAZAZAZAZAZAZAZAZAZAZAZAZAZAZ