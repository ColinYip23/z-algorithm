def z_algo(string, z):
    """
    Z-algorithm to compute the Z-array for a given string.
    
    The Z-algorithm constructs an array Z where Z[i] is the length of the longest
    substring starting from str[i] which is also a prefix of the string.
    """
    n = len(string)
    
    # L and R is the left and right index of the current Z-box
    # K is the current index we are at 
    L, R, K = 0, 0, 0
    
    while K < n:
        # Case 1: K is outside the current Z-box [L, R]
        # We need to compute Z[K] from scratch
        if K > R:
            L, R = K, K  # Start a new Z-box at position K
            
            # Extend R as far as possible while characters match the prefix
            while R < n and string[R] == string[R - L]:
                R += 1
            
            z[K] = R - L  # Length of the matching substring
            K = L + z[L]  # Jump to the next position that needs computation
            
        # Case 2: K is inside the current Z-box [L, R]
        # We can use previously computed Z-values to optimize
        else:
            K1 = K - L  # Corresponding position in the prefix
            
            # Case 2a: Z[K1] is completely within the remaining Z-box
            # We can directly copy the value
            if z[K1] < R - K + 1:
                z[K] = z[K1]
                
            # Case 2b: Z[K1] extends beyond the current Z-box
            # We need to extend the comparison from position R
            else:   
                L = K  # Start new Z-box from K
                
                # Continue matching from where the current Z-box ends
                while R < n and string[R] == string[R - L]:
                    R += 1
                    
                z[K] = R - L  # Length of the matching substring
                
        K += 1  # Move to the next position
        
    return z

def search(text, pattern):
    """
    Search for occurrences of a pattern in a text using the Z-algorithm.
    
    Returns a list of starting indices where the pattern is found in the text.
    """
    combined = pattern + "$" + text
    z = [0] * len(combined)
    
    z_algo(combined, z)
    
    pattern_length = len(pattern)
    result = []
    
    for i in range(len(z)):
        if z[i] == pattern_length:
            result.append(i - pattern_length - 1)  # Adjust index to match text
    
    return result

if __name__ == "__main__":
    text = "ababcababcabc"
    pattern = "abc"
    
    occurrences = search(text, pattern)
    print(f"Pattern '{pattern}' found at indices: {occurrences}")