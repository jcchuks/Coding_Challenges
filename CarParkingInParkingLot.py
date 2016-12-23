#Beating Uber Bot on the Car Parking In Parking Lot game was fun
#Try out on https://codefights.com/signup/6BDTrS8CLRjtZkKWe/company-bots/bot_uber

def parkingSpot(carDimensions, parkingLot, luckySpot):
    width = carDimensions[1]
    length = carDimensions[0]
    enter = 0
    def frmLeft():
        if length > len(parkingLot[0]):
            return False
        #==>
        entrance = []
        for row in parkingLot:
            entrance.append(row[0]) 
        gridCount = 0  
        start = 0
        flag = True
        index = 0
        for grid in entrance:
            if grid == 0:
                if flag:
                    start = index
                    flag = False
                gridCount = index - start
                print gridCount
                if gridCount >= width - 1 :
                    enter = 1
                    while enter >= 1:
                        if enter - length == luckySpot[0] and index+ 1 - width == luckySpot[1] and index == luckySpot[2] and enter - 1 == luckySpot[3]:
                            print enter+1 - length,index+ 1 - width,index,enter
                            return True
                        check = 0
                        for row in parkingLot[index + 1 - width:index + 1]:
                            #print index parkingLot[index - width:index + 1]
                            if row[enter] == 0:
                                check += 1
                            else:
                                check = 0 
                        if check == width:
                            enter += 1
                             
                        else:
                            enter = 0
                        
            
            else:
                #Reset grid count to zero 
                flag = True
            index += 1 
        return False
            
        
    def frmRight():
        entrance = []
        if length > len(parkingLot[0]):
            return False
        rowSize = len(parkingLot[0])
        for row in parkingLot:
            entrance.append(row[rowSize - 1]) 
        gridCount = 0  
        start = 0
        flag = True
        index = 0
        for grid in entrance:
            if grid == 0:
                if flag:
                    start = index
                    flag = False
                gridCount = index - start 
                if gridCount >= width - 1 : 
                    enter = 1
                    while enter >= 1:
                        if enter - length == luckySpot[0] and index+ 1 - width == luckySpot[1] and index == luckySpot[2] and enter - 1 == luckySpot[3]:
                            print enter+1 - length,index+ 1 - width,index,enter
                            return True
                        check = 0
                        for row in parkingLot[index + 1- width:index + 1]:
                            if row[rowSize -1 - enter] == 0:
                                check += 1
                            else:
                                check = 0 
                        if check == width:
                            enter += 1
                        else:
                            enter = 0
                        
            
            else:
                #Reset grid count to zero 
                flag = True
            index += 1
        return False
        
    def frmTop():
        if length > len(parkingLot):
            return False
        rowSize = len(parkingLot[0])
         
        entrance =  parkingLot[0]
        gridCount = 0  
        start = 0
        flag = True
        index = 0
        for grid in entrance:
            if grid == 0:
                if flag:
                    start = index
                    flag = False
                gridCount = index - start 
                if gridCount >= width - 1 : 
                    enter = 1
                    while enter >= 1 and enter < len(parkingLot):
                        if enter + 1 - length == luckySpot[0] and index+ 1 - width == luckySpot[1] and index == luckySpot[2] and enter == luckySpot[3]:
                            print enter+1 - length,index+ 1 - width,index,enter
                            return True
                        check = 0
                        for col in parkingLot[enter][index + 1 - width:index + 1]:
                             
                            if col == 0:
                                check += 1
                            else:
                                check = 0 
                        if check == width:
                            enter += 1
                        else:
                            enter = 0 
            else:
                #Reset grid count to zero 
                flag = True
            index += 1 
        return False
        
    def frmBottom():
        if length > len(parkingLot):
            return False
        colSize = len(parkingLot) 
        entrance =  parkingLot[colSize - 1]
        gridCount = 0  
        start = 0
        flag = True
        index = 0
        for grid in entrance:
            if grid == 0:
                if flag:
                    start = index
                    flag = False
                gridCount = index - start 
                if gridCount >= width - 1 : 
                    enter = 1
                    while enter >= 1 and enter < len(parkingLot):
                        if enter - length == luckySpot[0] and index+ 1 - width == luckySpot[1] and index == luckySpot[2] and enter - 1== luckySpot[3]:
                            print enter + 1 - length, index + 1 - width, index, enter
                            return True
                        check = 0
                        for col in parkingLot[colSize - 1 - enter][index + 1 - width:index + 1]: 
                            if col == 0:
                                check += 1
                            else:
                                check = 0 
                        if check == width:
                            enter += 1
                        else:
                            enter = 0 
            else:
                #Reset grid count to zero 
                flag = True
            index += 1
        return False
    if frmBottom():
        return True
    elif frmLeft():
        return True
    elif frmRight():
        return True
    elif frmTop():
        return True
    else:
        return False
