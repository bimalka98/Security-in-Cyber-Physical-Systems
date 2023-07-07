# -*- coding: utf-8 -*-
""" CNT5410 -- Assignment 1: Passwords -- rainbow.py
"""

import sys
import utils

"""
## Build rainbow table.

    Inputs:
        pc: performance counter (PerfCounter),
        next_fn: next candidate password function,
        out_fp: output filepath,
        num_chains: number of chains to compute,
        k: length of each chain,
        pwhash_fn: compute password hash function,
        reduce_fn: reduce function family,
        random_candidates_fn: random password candidates function

    Outputs:
        None
"""
def build_rainbow(pc, out_fp, num_chains, k, pwhash_fn, reduce_fn, random_candidates_fn):

    table = {}

    ## TODO: Problem 3.3 ##
    ## Put your code here to avoid duplicating start points

    sys.stdout.write('Building rainbow table')
    for i in range(0, num_chains):
        # build chain i
        startpoint = random_candidates_fn()

        ## TODO: Problem 3.3 ##
        ## Put your code here to avoid duplicating start points

        current = startpoint

        for j in range(0, k):
            # do one iteration
            hv = pwhash_fn(current)
            next = reduce_fn(j, hv)
            current = next

        pc.inc(k) # increment by k

        if i > 0 and (pc.get() % 100000) < k:
            sys.stdout.write('.')
            sys.stdout.flush()

        endpoint = current

        if endpoint not in table:
            table[endpoint] = []
        table[endpoint].append({'chain': i, 'start': startpoint, 'end': endpoint})

    utils.write_json(out_fp, table)
    print(' done.')


## TODO: Problem 2.4 ##
"""
## Rainbow table lookup.

    Inputs:
        pc: performance counter (PerfCounter),
        in_fp: table filepath,
        k: length of each chain,
        pwhash_fn: compute password hash function,
        reduce_fn: reduce function family,
        pwhash_list: the list of password hashes we want to invert (find the plaintext password for)
        
    Outputs:
        results: array of length len(pwhash_list) containing the matching passwords (or None)
"""
def lookup_rainbow(pc, in_fp, k, pwhash_fn, reduce_fn, pwhash_list, verbose = False):
    # entry format: {'9g5i': [{'chain': 1, 'end': '9g5i', 'start': 'ex2b'}],...}
    table = utils.read_json(in_fp)    
    # code to understand the structure of the table
    print("Type of the lookup table: {}".format(type(table)))
    print("Length of the lookup table: {}".format(len(table)))    
    # initialize the results array for the cracked passwords
    pwres = [None for i in range(len(pwhash_list))]
    # iterate over the password hashes
    for pwidx, pwhash in enumerate(pwhash_list):
        # a lsit of dictionaries to store the chain info if there is a match
        chain_infos = []
        # apply the reduce function family to the hash value        
        for i in range(k):
            
            current_hash = pwhash
            # reduce the hash value
            rv = None
            for j in range(i, k):
                rv = reduce_fn(j, current_hash)
                current_hash = pwhash_fn(rv)

            # check if the reduced value is in the table
            if rv in table:                
                # if it is in the table, then we have a match
                chain_infos.extend(table[rv])
                print(pwhash, rv, table[rv])
                # break

        pc.inc(k)  # increment by k

        for j, chain_info in enumerate(chain_infos):
            # print("Chain info: {} : {}".format(j, chain_info))
            chain_idx = chain_info['chain']
            startpoint = chain_info['start']
            # plaintext password candidate
            current = startpoint

            if pwres[pwidx] is not None:
                break

            found = False
            for l in range(0, k):
                # do one iteration
                hv = pwhash_fn(current)
                # print(current, hv)
                # check if the hash value matches the target hash value
                if hv == pwhash:
                    found = True
                    pwres[pwidx] = current
                    print("Password found: ", current)
                    break
                # if not, then reduce the hash value
                next = reduce_fn(l, hv)
                current = next

            if verbose and not found:
                print('\t[False alarm] for pwhash {} in chain {} [start: {}, end: {}]!'.format(pwhash, chain_idx, startpoint, chain_info['end']))

    return pwres
