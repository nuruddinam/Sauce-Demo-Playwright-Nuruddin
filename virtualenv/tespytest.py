def luas_lingkaran(r):
    luas = r**2 * 3.14
    return luas

print(luas_lingkaran(10))

def test_luas_lingkaran():
    r=10
    luas = luas_lingkaran(r)
    print(luas)
    assert luas == '314'