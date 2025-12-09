import CSP_4_02_List_practice as HW
def test_bookends():
    x = [1,5,7,3,2]
    y = HW.bookends(x)
    assert y == [1,2]
    assert x == [5,7,3]
    x = [0,0]
    y = HW.bookends(x)
    assert y ==[0,0]
    assert x == []


def test_in_order():
    assert HW.inOrder([1,5,6,8])==True
    assert HW.inOrder([1,7,5,6,8])==False
    assert HW.inOrder([])==True


def test_find():
    assert HW.find([1,4,6,8,10],10)==4
    assert HW.find([1,4,6,8,10],1)==0
    assert HW.find([1,4,6,8,10],11)==-1


def test_remove_lowest():
    x = [6,1,4,2,3]
    HW.removeLowest(x)
    assert x == [6,4,2,3]
    HW.removeLowest(x)
    assert x == [6,4,3]
    HW.removeLowest(x)
    assert x == [6, 4]


def test_keep_order():
    x = [1,3,5,7]
    HW.keepOrder(x, 4)
    assert x== [1,3,4,5,7]
    HW.keepOrder(x,8)
    assert x ==[1,3,4,5,7,8]
    HW.keepOrder(x, 0)
    assert x == [0, 1, 3, 4, 5, 7, 8]


def test_merge():
    x = [1,3,5]
    y = [2,4,6,8]
    z = HW.merge(x,y)
    assert z == [1,2,3,4,5,6,8]
    assert x == [1,3,5]
    assert y == [2,4,6,8]
