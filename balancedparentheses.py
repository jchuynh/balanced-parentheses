"""Does a string have balanced parentheses?

For example::

   >>> has_balanced_parens("()")
   True

   >>> has_balanced_parens("(Oh Noes!)(")
   False

   >>> has_balanced_parens("((There's a bonus open paren here.)")
   False

   >>> has_balanced_parens(")")
   False

   >>> has_balanced_parens("(")
   False

   >>> has_balanced_parens("(This has (too many closes.) ) )")
   False

If you receive a string with no parentheses, consider it balanced::

   >>> has_balanced_parens("Hey...there are no parens here!")
   True
"""


def has_balanced_parens(phrase):
    """Does a string have balanced parentheses?"""

    # create a count for '(' (p_open)
    # create a count for ')' (p_close)

    p_open = 0
    p_close = 0

    # if a phrase/string is empty, return balance parentheses is True

    if phrase == "":
        return True

    # for loop through each character in the phrase 
    # if character is '(' add a count of +1
    # if character is ')' add a count of +1 

    for char in phrase:
        if char == '(':
            p_open += 1
        if char == ')':
            p_close += 1

    # if count of open is equal to the count of close
    # return True 

    # print(p_open)
    # print(p_close)

    if p_open == p_close:
        return True

    # else return False

    else:
        return False

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. YOU CAUGHT ALL THE STRAY PARENS!\n")
