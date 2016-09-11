def chunks(l,n):
    """Yield n-sized chunks from l.
    """
    for i in range(0, len(l), n):
        yield l[i:i+n]