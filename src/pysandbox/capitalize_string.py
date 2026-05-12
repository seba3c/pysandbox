# -*- coding: utf-8 -*-

# Write a program that will correct an input string to use proper capitalization and spacing.
# Allowed punctuation are the period ( . ), question mark ( ? ), and exclamation ( ! ).
# Make sure that single space always follows commas ( , ), colons ( : ), semicolons ( ; )
# and all other punctuation.
# The input string will be a valid English
# sentence.capitalizeString("first, solve the problem.then, write the code.")
# // "First, solve the problem. Then, write the code."
# capitalizeString("this is a test... and another test.")
# // "This is a test... And another test."
import re


def capitalize_string(S):
    def upper_after_dot(m):
        return m[1] + " " + m[2].strip().capitalize()

    if S is not None:
        # remove leading and trailing spaces
        ss = S.strip()
        # capitalize first letter
        ss = ss.capitalize()
        # replace more than one space by one space
        ss = re.sub(r"\s+", " ", ss)
        # fix . spacing
        ss = re.sub(r"([.])(\s{2,*})", r". \2", ss)
        ss = re.sub(r"([.])(\w+)", r". \2", ss)
        # fix , spacing
        ss = re.sub(r"(,)(\s{2,*})", r", \2", ss)
        ss = re.sub(r"(,)(\w+)", r", \2", ss)
        # fix ; spacing
        ss = re.sub(r"(;)(\s{2,*})", r"; \2", ss)
        ss = re.sub(r"(;)(\w+)", r"; \2", ss)
        # fix : spacing
        ss = re.sub(r"(:)(\s{2,*})", r": \2", ss)
        ss = re.sub(r"(:)(\w+)", r": \2", ss)
        # fix ? spacing
        ss = re.sub(r"(\?)(\s{2,*})", r"? \2", ss)
        ss = re.sub(r"(\?)(\w+)", r"? \2", ss)
        # fix ! spacing
        ss = re.sub(r"(!)(\s{2,*})", r"! \2", ss)
        ss = re.sub(r"(!)(\w+)", r"! \2", ss)
        # upper case after .
        ss = re.sub(r"([.])(\s[a-z]*)", upper_after_dot, ss)

        return ss
    return None


if __name__ == "__main__":
    print(capitalize_string("first, solve the problem.then, write the code."))
