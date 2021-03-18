import morse
if __name__ == "__main__":
    e = morse.encode('us')
    print('%s' % e)
    d = morse.decode(e)
    print('%s' % d)

    assert morse.encode('us') == '..- ...', "Should be ..- ..."
    assert morse.decode('..- ...') == 'us', "Should be us"