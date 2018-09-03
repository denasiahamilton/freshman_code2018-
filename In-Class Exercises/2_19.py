def search_binary(xs, target):
    """ Find and return the index of key in sequence xs """
    lb = 0
    ub = len(xs)
    while True:
        if lb == ub:   # If region of interest (ROI) becomes empty
           return -1

        # Next probe should be in the middle of the ROI
        mid_index = (lb + ub) // 2

        # Fetch the item at that position
        item_at_mid = xs[mid_index]

        print("ROI[{0}:{1}](size={2}), probed='{3}', target='{4}'"
            .format(lb, ub, ub-lb, item_at_mid, target))

        # How does the probed item compare to the target?
        if item_at_mid == target:
            return mid_index      # Found it!
        if item_at_mid < target:
            lb = mid_index + 1    # Use upper half of ROI next time
        else:
            ub = mid_index        # Use lower half of ROI next time

"""
xs = ["Alex", "Ben", "Clara", "Ellen", "David", "Jason", "Leo", "Mary", "Maya", "Peter"]
target = "Maya"
print(search_binary(xs,target)) #index that 20 is at
"""

xs = [0, 2, 5,10,37,89,107, 117, 127, 340]
target = 107
print(search_binary(xs,target)) #index that 20 is at
