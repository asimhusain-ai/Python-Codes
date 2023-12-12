import threading
def vol_cube(s):
    print("Cube:- {}".format(s*s*s))
def area_square(sd):
    print("Square:- {}".format(sd *sd))
if __name__=="__main__":
    t1=threading.Thread(target=vol_cube,args=(5,))
    t2=threading.Thread(target=area_square,args=(6,))
    t1.start()
    t2.start()

    t1.join()
    t1.join()