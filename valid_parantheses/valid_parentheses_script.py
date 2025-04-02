braces = {
    '(': ')',
    '{': '}',
    '[': ']',
}


class ValidParenthesesSolution(object):
    def is_valid(self, braces_s):
        if not braces_s or len(braces_s) % 2 != 0:
            return "Invalid"

        open_indexes = []
        close_indexes = []
        start = 0

        while True:
            open_indexes.append(start)
            open_brace = braces_s[start]
            closing_brace_index = self.get_closing_brace_index(braces_s, open_brace, start + 1)

            if not closing_brace_index:
                return "Invalid"
            close_indexes.append(closing_brace_index)

            indexes = open_indexes + close_indexes
            start = min(indexes) + 1

            while start in indexes and start < len(braces_s):
                start = start + 1

            if len(indexes) == len(braces_s) and len(open_indexes) == len(close_indexes):
                return "Valid"
            a = 0

    def get_closing_brace_index(self, braces_s, opening_brace, start_index):
        match_level = 1
        if opening_brace not in braces:
            return

        for i, next_brace in enumerate(braces_s[:]):
            if i < start_index:
                continue
            if opening_brace == next_brace:
                match_level += 1
            if braces[opening_brace] == next_brace:
                if match_level > 1:
                    match_level -= 1
                    continue
                # closing_brace = next_b
                # return closing_brace
                return i


if __name__ == "__main__":
    parentheses_input = [
        # "()[]{}",
        # "(()[]{})",
        # "[(()[]){}]",
        # "[(()[]){}]{{",
        # "((()))",
        # ")(}{][",
        # "(){}][",
        # "(()}{)",
        "({)}",  # incorrect order - need to fix this case
    ]

    for s in parentheses_input:
        result = ValidParenthesesSolution().is_valid(s)
        print(f'{result} = "{s}"')
