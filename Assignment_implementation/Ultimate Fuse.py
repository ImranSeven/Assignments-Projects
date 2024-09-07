def fuse(fitmons):
    """
    Function description:
    This function takes a list of FITMONs and fuses them together to create the ultimate FITMON with the highest possible cuteness score.

    Approach description:
    I used dynamic programming to calculate the maximum cuteness score for any FITMON fusion combination. By doing so, I can get the cuteness score 
    for each fusion by iterating over all possible fusion lengths, starting indices, and fusion points within each fusion range. I then save the highest 
    possible cuteness score in a 2D array. By taking into account every potential fusion combination and keeping track of subsequent outcomes, I then 
    calculate the maximum cuteness score that may be achieved for the complete list of FITMONs.

    :Input:
    fitmons: A list of FITMONs, where each FITMON is represented by a list containing three values: 
                1. affinity_left 
                2. cuteness_score 
                3. affinity_right.

    :Output, return or postcondition:
    Returns the highest possible cuteness score obtained from fusing all the FITMONs together.

    :Time complexity:
    O(N^3) where N is the number of FITMONs.

    :Time complexity analysis:
    The function iterates over all possible fusion lengths, starting indices, and fusion points within each fusion range, 
    resulting in a cubic time complexity. Hence, the function takes O(N^3) time.

    :Space complexity:
    O(N^2) where N is the number of FITMONs.

    :Space complexity analysis:
    The function uses a 2D array (dynamic programming) to store the maximum cuteness score for each FITMONs, 
    resulting in a quadratic space complexity. Therefore, the function uses O(N^2) space.
    """

    n = len(fitmons)
   
    # Base case: If there's only one FITMON, return its cuteness_score
    if n == 1:
        return fitmons[0][1]
    
    # Initialize a 2D array to store maximum cuteness scores
    dp = [[0] * n for _ in range(n)]
    
     # Initialize diagonal elements with FITMON cuteness scores
    for i in range(n): 
        dp[i][i] = fitmons[i][1]


    for length in range(2, n + 1):  # Iterate over all possible fusion lengths
        for i in range(n - length + 1): # Iterate over starting indices
            j = i + length - 1
            max_cuteness = 0

            # Iterate over all possible fusion points within the current fusion range
            for k in range(i, j):

                # Calculate cuteness score for fusion of FITMONs at indices i to k and k+1 to j
                left_fitmon_affinity = fitmons[k][2] if k < n - 1 else 0
                right_fitmon_affinity = fitmons[k + 1][0] if k + 1 < n else 0
                cuteness_score = int(dp[i][k] * left_fitmon_affinity + dp[k + 1][j] * right_fitmon_affinity)

                # Update maximum cuteness score for current fusion range
                max_cuteness = max(max_cuteness, cuteness_score)
            
            # Store maximum cuteness score
            dp[i][j] = max_cuteness

    # Return maximum cuteness score for entire list of FITMONs
    return dp[0][n - 1]