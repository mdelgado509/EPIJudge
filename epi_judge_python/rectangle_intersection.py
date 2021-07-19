import collections

from test_framework import generic_test
from test_framework.test_failure import PropertyName

Rect = collections.namedtuple('Rect', ('x', 'y', 'width', 'height'))


def intersect_rectangle(r1: Rect, r2: Rect) -> Rect:
    def is_intersect(r1, r2):
        return (r1.x <= r2.x + r2.width and # leftmost point of r1 is less than or equal to rightmost point of r2
                r1.x + r1.width >= r2.x and # rightmost point of r1 is greater than or equal to leftmost point of r2
                r1.y <= r2.y + r2.height and # lowest point of r1 is less than or equal to highest point of r2
                r1.y + r1.height >= r2.y) # highest point of r1 is greater than or equal to lowest point of r2

    if not is_intersect(r1, r2):
        return Rect(0, 0, -1, -1) # no intersection
    return Rect(
        max(r1.x, r2.x), # the rightmost point of the two intersecting rectangles leftmost points
        max(r1.y, r2.y), # the highest point of the two intersecting rectangles lowest points
        min(r1.x + r1.width, r2.x + r2.width) - max(r1.x, r2.x), # the smaller of the two rectangles rightmost points minus the x max
        min(r1.y + r1.height, r2.y + r2.height) - max(r1.y, r2.y) # the smaller of the two rectangles highest points minus the y max
    )


def intersect_rectangle_wrapper(r1, r2):
    return intersect_rectangle(Rect(*r1), Rect(*r2))


def res_printer(prop, value):
    def fmt(x):
        return [x[0], x[1], x[2], x[3]] if x else None

    if prop in (PropertyName.EXPECTED, PropertyName.RESULT):
        return fmt(value)
    else:
        return value


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('rectangle_intersection.py',
                                       'rectangle_intersection.tsv',
                                       intersect_rectangle_wrapper,
                                       res_printer=res_printer))
