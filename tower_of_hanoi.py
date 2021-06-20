n=int(input("Enter the number of disks."))
frompeg="A"
topeg='B'
auxpeg='C'

def towers_of_hanoi(n,frompeg,topeg,auxpeg):
    #if only one disk make the move and return
    if(n==1):
        print("Move disk 1 from peg",frompeg," to peg",topeg)
        return

    #Move top n-1 disks from source peg to destination peg, using auxiliary peg
    towers_of_hanoi(n-1,frompeg,topeg,topeg)

    #movie the remaining disks from source to destination
    print("Move disk ",n , "from peg ",frompeg, "to peg",topeg)

    #move n-1 disks from destination peg to auxilary peg
    towers_of_hanoi(n-1,auxpeg,topeg,frompeg)

towers_of_hanoi(n,frompeg,topeg,auxpeg)