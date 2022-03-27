exc = AssertionError


def ok_(expr, msg=None):
    """Check expression is true
    """
    if not expr:
        raise exc(msg)


def not_(expr, msg=None):
    """Check expression is false
    """
    if expr:
        raise exc(msg)


def eq_(a, b, msg=None):
    """Check a == b
    """
    if not a == b:
        raise exc(
            msg or "%r != %r" % (a, b)
        )


def fail(msg=None):
    """Fail with the message
    """
    raise exc(msg)
