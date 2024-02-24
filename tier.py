tier_problems = {
    1: ['Contains Duplicate','Valid Anagram'],
    2: ['Valid Palindrome', 'Two Sum II Input Array Is Sorted', 'Valid Parantheses', 'Min Stack' ],
    3: ['Binary Search', 'Search a 2D Matrix', 'Best Time to Buy And Sell Stock', 'Longest Substring Without Repeating Characters', 'Reverse Linked List', 'Merge Two Sorted Lists'],
    4: ['Invert Binary Tree', 'Maximum Depth of Binary Tree'], 
    5: ['Implement Trie Prefix Tree', 'Subsets'],
    6: ['Kth Largest Element in a Stream', 'Number of Islands', 'Climbing Stairs'],
    7: ["Insert Interval", 'Maximum Subarray'], 
    8: ['Rotate Image', 'Spiral Matrix']
    # Add more Questions as needed
}

#Array of completed User Problems
user_completed_problems = ['Contains Duplicate', 'Valid Anagram', 'Binary Search']

user_score = 0

for problem in user_completed_problems:
    for tier, tier_problems_list in tier_problems.items():
        if problem in tier_problems_list:
            user_score += tier * 10
            break 

tierEnd = False


def get_user_tier(user_problems):
    global tierEnd  

    greatest_tier = 0  # Initialized with the lowest tier

    for tier, tier_problems_list in tier_problems.items():
        if set(tier_problems_list).issubset(set(user_problems)):
            greatest_tier = max(greatest_tier, tier)
            tierEnd = True
        elif tierEnd:
            return greatest_tier

    return greatest_tier


user_tier = get_user_tier(user_completed_problems)
print(f"The users score is {user_score}")
print(f'The user is in Tier {user_tier}')