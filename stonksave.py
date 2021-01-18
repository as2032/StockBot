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
                templist.append(tick)
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
    out = str(n) + "watchlist: " + str(wl)
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
    out  = "Removed stocks from "+ str(n) + " watchlist"

    return out