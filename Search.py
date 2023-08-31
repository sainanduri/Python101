class Search:
    """
     this class is for search.
    """

    def __init__(self, array, target):
        """
        constructor for search class
        :param array: array of elements
        :type array:  list
        :param target:  element to be searched
        :type target: int
        """
        if type(target) != int or type(array) != list:
            raise ValueError("Invalid data given")

        # class members or class variables
        self.search_array = array
        self.search_element = target

    # class methods
    def linear_search(self):
        """
        Does search using linear search mechanism
        :return: True - if element found False - if element not found.
        :rtype: bool
        """
        pass

    # class methods
    def binary_search(self):
        """
        does search using  binary search mechanism
        :return: True - if element found False - if element not found.
        :rtype: bool
        """
        pass

    def add_element(self, element):
        """
        Adds element to the existing array
        :param element: element
        :type element: integer
        :return: None
        :rtype: None
        :raises ValueError if given data is not valid
        """
        if type(element) != int or element is None:
            raise ValueError(f"Element {element} should be integer and not None.")
        if element in self.search_array:
            raise ValueError(f"Element {element} already in array")
        self.search_array.append(element)

    def delete_element(self, element):
        """
        Deletes elements to the existing array
        :param element: element
        :type element: integer
        :return: None
        :rtype: None
        """
        pass


if __name__ == '__main__':
    s1_name = Search(array=[1, 2, 3, 4, 5, 6], target="4")
    s2_name = Search(array=[7, 8, 9, 10, 11, 12], target=5)
    if s1_name.linear_search():
        print("element found using linear search")
    else:
        print("Element not found")
    s1_name.delete_element(element=4)
    if s1_name.binary_search():
        print("Element found")
    else:
        print("Element not found")

    if s2_name.binary_search():
        print("Element found using binary search")
    else:
        print("Element not found using binary search")
