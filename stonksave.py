import stock
import stock2
watchlistArray = {}

def saveStonk(watchlist):

    i = 0
    templist = []
    for tick in watchlist:
        if(i == 0):
            name = tick
            if(name not in watchlistArray):
                watchlistArray[name] = []

                i= i+1
            else:
                i = i+1
        else:
            templist.append(tick)

    watchlistArray[name] = templist
    out = "Added " + str(templist) + " to "+ str(name) +" watchlist."
    return out


def getList(name):
    for i in name:
        n = i
        break
    wl = watchlistArray.get(n)
    out = str(n) + " watchlist: " + str(wl)
    return out



def runList(name):
    for i in name:
        n = i
        break
    wl = watchlistArray.get(n)
    out = stock.runStonks(wl)

    return out

def runListd(arg):

    i = 0

    for thing in arg:
        if i==0:
            name = thing
            i = i+1
        else:
            dateOffset = thing

    wl = watchlistArray.get(name)

    wl.insert(0,dateOffset)

    out = stock2.runStonks(wl)

    return out

def removeList(name):
    for i in name:
        n = i
        break
    del watchlistArray[n]
    out  = "Removed all stocks from "+ str(n) + " watchlist"

    return out

def removeStock(list):
    j = 0
    toRem = []
    for i in list:
        if(j==0):
            n = i
            j = 1
        else:
            toRem.append(i)
    wl = watchlistArray[n]
    for tick in toRem:
        wl.remove(tick)

    out  = "Removed "+ str(toRem) +" from "+ str(n) + " watchlist"

    return out


def getall():
    out = []
    
    for n in watchlistArray.keys():
        out.append(str(n)+": "+watchlistArray.get(n)+"|| ")
        
    return out