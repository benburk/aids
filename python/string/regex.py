"""
Implement regex operators: .+*
"""


def match(pattern, string):
    """
    dp[i][j]
    """
    pattern = " " + pattern
    string = " " + string
    dp = [[0] * (len(pattern) + 1) for _ in range(len(string) + 1)]
    dp[0][0] = True

    for i in range(1, len(string) + 1):
        for j in range(1, len(pattern) + 1):
            if pattern[j - 1] in (".", string[i - 1]):
                dp[j][i] = dp[j - 1][i - 1]
            elif pattern[j - 1] == "*":
                dp[j][i] = (
                    (
                        pattern[j - 2] in [".", string[i - 1]]
                        and (dp[j - 1][i - 1] or dp[j][i - 1])
                    )
                    or dp[j - 2][i]
                    or dp[j - 1][i]
                )

    return dp[-1][-1]


print(match("a.*b", "ab"))
