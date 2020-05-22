##### Functions ################################################################

def lgis3( seq, count ):
    '''
    Returns reversed version of (a) longest increasing subsequence.

    seq: the sequence for which (a) longest increasing subsequence is desired.
    count: number of items in seq

    Notes:
    Uses "Patience Sorting"
    Each 'pile' is a subsequence with the opposite polarity {decreasing} to
        that of the desired longest subsequence {increasing}
    **LOGIC**: when backtracking, once an element from a pile is selected, 
        all elements to the left are larger, and all to the right are smaller
        THUS only one element from each pile can be used in an increasing subseq
    '''       
    # list of lists of decreasing subsequences
    piles = []

    # all possible indices that could be used for decreasing subsequences 
    #    -- i.e. if whole sequence is increasing
    pile_indices = range(count)

    # loop appends each item to the end of first 'pile' for which it continues 
    #        the descending subsequence
    #    the second value in each tuple is the index + 1 of the preceeding 
    #        pile's last element (or -1 if no preceeding pile)
    #    this allows the traceback to find the last element from the 
    #        preceeding pile that was added before this element
    for item in seq:
        # using for & break is simpler and faster than the original
        # elminating range(len(piles)) and catching the exception when going
        #    beyond the end of the list (instead of using else) gives an
        #    additional slight improvement in speed
        try:
            for j in pile_indices:

                if piles[j][-1][0] > item:
                    # pile index
                    idx = j

                    # append tuple comprising the current item and the position 
                    #   of the preceeding pile's last element (for traceback)
                    piles[idx].append(
                        (
                            item, 
                            len(piles[idx-1]) if idx > 0 else -1
                        )
                    )

                    # resume outer loop
                    break

        except:
            # start a new pile each time the current element is larger than the 
            #    last element of all current piles
            piles.append( 
                [(
                    item, 
                    # length of the last 'pile' (before this one is created)
                    len(piles[-1]) if piles else -1
                )]
            )

    # the increasing subsequence (reversed)
    result = []

    # backward pointer -- index of last item in the preceeding pile that was 
    #    added before the current item
    point_back = -1

    # reverse iteration over the piles
    for i in range( len(piles) - 1, -1, -1 ):

        result.append( piles[i][point_back][0] )
        point_back = piles[i][point_back][1] - 1

    return result

##### Execution ################################################################

# read permutation from file
with open('input.txt', 'r') as infile:
    # size of permutation
    count = int(infile.readline().strip())

    # sequence of permutation
    seq = [int(item) for item in infile.readline().split()]

# write results to file
with open('output.txt', 'w') as outfile:
    outfile.write(
                    " ".join(map(str, lgis3(seq, count)[::-1])) + 
                    '\n' + 
                    " ".join(map(str, lgis3(seq[::-1], count)))
    )
