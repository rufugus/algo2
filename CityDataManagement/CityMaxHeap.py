from typing import List
from CityDataManagement.City import City
from CityDataManagement.AbstractCityHeap import AbstractCityHeap


class CityMaxHeap(AbstractCityHeap):
    """
    Class with the responsibility to create a Max-Heap-structure based on unstructured data.
    (Every Parents Key must be greater than its children Key)

    """

    def __init__(self, raw_city_data: List[City], recursive: bool, floyd: bool):
        """
        Creation of a Max-City-Heap.

        :param raw_city_data:    A unsorted List of Cities
        :param recursive:    Should the heapify be recursiv? False = use the iterative approach; True = Recursiv approach
        :param floyd:       Should Floyds algorithm be used for insertion? True = instead of the iterative or recursiv approach Floyds algorithm will be used instead.
                            For removal the approach specified in :param recursiv will be used.
        """
        super().__init__(raw_city_data, recursive, floyd)

    def heapify_up_iterative(self):
        """
        Establish heap conditions for a Max-Heap iterative upwards.
        """
        for i in range(self.currentHeapLastIndex):
            index = self.currentHeapLastIndex - i
            while index > 0:
                if self.get_city_population(index) > self.get_city_population(self.get_parent_index(index)):
                    self.swap_nodes(index, self.get_parent_index(index))
                    index = self.get_parent_index(index)
                else:
                    break



    def heapify_up_recursive(self, index):
        """
        Establish heap conditions for a Max-Heap recursive upwards.
        """

        # TODO: implement me!
        ...

    def heapify_floyd(self, index, amount_of_cities):
        """
        Establish heap conditions for a Max-Heap via Floyds Heap Construction Algorithmus.

        """
        # TODO: implement me!
        ...

    def heapify_down_iterative(self):
        """
        Establish heap conditions for a Max-Heap iterative downwards.
        """
        for i in range(self.currentHeapLastIndex):
            index = 0 + i
            while index < self.currentHeapLastIndex:
                if self.get_city_population(index) > self.get_city_population(self.get_parent_index(index)):
                    self.swap_nodes(index, self.get_parent_index(index))
                    index = self.get_parent_index(index)
                else:
                    break


    def heapify_down_recursive(self, index):
        """
        Establish heap conditions for a Max-Heap recursive downwards.
        """
        # TODO: Anschauen und nach Fehler prüfen nur PseudoCode!
        leftChild = self.get_left_child_index(index)
        rightChild = self.get_right_child_index(index)

        max = index

        if self.has_left_child(index) and self.get_city_population(leftChild) > self.get_city_population(max):
            max = leftChild
        if self.has_right_child(index) and self.get_city_population(rightChild) > self.get_city_population(max):
            max = rightChild
        if max != index:
            self.swap_nodes(index, max)
            self.heapify_up_recursive(max)

    def remove(self):
        """
        Remove a City from the Max-Heap
        """
        self.swap_nodes(0, self.currentHeapLastIndex)
        self.currentHeapLastIndex -= 1
        self.heapify_down_iterative()
