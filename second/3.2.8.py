def test_substring(full_string, substring):
    assert substring in full_string, "expected {}, to be substring {}".format('substring' in 'full_string')

