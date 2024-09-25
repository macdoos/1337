# O(n) time | O(1) space
def hIndex(citations):
    # Sort the citations in non-increasing order
    citations.sort(reverse=True)
    
    # Initialize the h-index
    h = 0
    
    # Iterate through the sorted citations array
    for i, citation in enumerate(citations):
        if citation >= i + 1:
            h = i + 1
        else:
            break
    
    return h

citations = [3,0,6,1,5]
print(hIndex(citations))
