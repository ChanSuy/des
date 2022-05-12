# P-box순열
class P_Box():
    def pBoxReplace(sBoxResult):
        pBox=[16,  7, 20, 21,29, 12, 28, 17,1, 15, 23, 26,5, 18, 31, 10,2,  8, 24, 14,32, 27,  3,  9,19, 13, 30,  6,22, 11,  4, 25]
        sBoxResultBit=''
        pBoxResultBit=''
        bit=''
        emptyList=[]
        pBoxResult=[]


        for i in range(len(sBoxResult)):
            for j in range(len(sBoxResult[i])):
                sBoxResultBit+=sBoxResult[i][j]

        for i in pBox:
            pBoxResultBit+=sBoxResultBit[i-1]
        
        for i in pBoxResultBit:
            bit+=i
            if len(bit)==8:
                emptyList.append(bit)
                bit=''
        pBoxResult.append(emptyList)    
        
        return pBoxResult