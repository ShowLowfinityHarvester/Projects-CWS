haystack = ["hay", "junk", "hay", "hay", "moreJunk", "needle", "randomJunk"]

def find_needle(haystack):
    
    NeedlePos = (haystack.index("needle"))
    
    print(f"found the needle at position {NeedlePos}")


find_needle(haystack)
