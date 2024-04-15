from circularDoublyLinkedList import *  #import Circular Doubly Linked List 

def do_sim(cache_slots):        #define simulation
    cdl = CircularDoublyLinkedList()    #allocate CircularDoublyLinkedList() as cdl
    cache_hit = 0   #count if workload is in cache_slots at the moment
    tot_cnt = 0     #count every lpn

    data_file = open("linkbench_short.trc")     #open trc file

    for line in data_file.readlines():      #read every lines in trc file
        lpn = line.split()[0]       #put workloads into lpn
        tot_cnt += 1        #count every workloads

        if cdl.index(lpn) != -12345:    #if lpn is not in cdl, cdl.index returns -12345
            cdl.remove(lpn)     #remove cache from cdl
            cache_hit += 1      #count if lpn is in cdl
        cdl.append(lpn)     #add lpn to cdl
        if cdl.size() > cache_slots:        #check if caches overs cache_slots
            cdl.pop(0)      #pop least resently used cache
        

    print("cache_slot = ", cache_slots, "cache_hit = ", cache_hit, "hit ratio = ", cache_hit / tot_cnt) #print cashe_slots, cache_hit, hit_ratio

if __name__ == "__main__":
    for cache_slots in range(100, 1000, 100):   #execute do_sim
        do_sim(cache_slots)