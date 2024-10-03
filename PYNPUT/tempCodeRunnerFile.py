try:
        print('alphanumeric key {0} pressed'.format(
            key.char))
    except AttributeError:
        pass