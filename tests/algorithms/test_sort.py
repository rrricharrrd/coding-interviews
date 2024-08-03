import random

import pytest

from interviews.algorithms import bubble_sort, heap_sort, merge_sort, quick_sort

RNG = random.Random(123)
ARRAY_SIZE = 5


@pytest.mark.parametrize("sort_fn", [bubble_sort, heap_sort, merge_sort, quick_sort])
def test_sort_empty(sort_fn):
    items = []
    result = sort_fn(items)
    assert result == sorted(items)


@pytest.mark.parametrize("sort_fn", [bubble_sort, heap_sort, merge_sort, quick_sort])
def test_sort_sorted(sort_fn):
    items = [random.randint(0, 2 * ARRAY_SIZE) for _ in range(ARRAY_SIZE)]
    items = sorted(items)
    result = sort_fn(items)
    assert result == sorted(items)


@pytest.mark.parametrize("sort_fn", [bubble_sort, heap_sort, merge_sort, quick_sort])
def test_sort(sort_fn):
    items = [random.randint(0, 2 * ARRAY_SIZE) for _ in range(ARRAY_SIZE)]
    for _ in range(5):
        RNG.shuffle(items)
        result = sort_fn(items)
        assert result == sorted(items)
