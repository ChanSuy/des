# 키 64bit
# 압축 순열 (56bit)
# 왼쪽 28bit 
# 오른쪽 28bit
# 왼쪽 시프트 
# 오른쪽 시프트
# 키 56bit
# 압축순열 48bit ->1라운드 키값
# 48비트로 확장하고 XOR연산 까지

class KeySting:
    def keyPressPermutation1(keyValue): #키 값을 받아 압축 순열 해주는 함수
        keyPressPermutationgraph1=[57,49,41,33,25,17,9,1,58,50,42,34,26,18,10,2,59,51,43,35,27,19,11,3,60,52,44,36,63,55,47,39,31,23,15,7,62,54,46,38,30,22,14,6,61,53,45,37,29,21,13,5,28,20,12,4]
        pressKeyBit='' #압축 결과를 저장할 문자열
        emptyList=[] #2차원 리스트 만들기 위한 일회용 빈 리스트
        pressKeyList=[] #키를 28비트 씩 2개의 리스트로 저장할 빈 리스트
        bitBin=''
        bitHalf=''
        count=0
        for i in keyValue: #
            bit=bin(ord(i))[2:]
            bitBin+='0'*(8-len(bit))+bit

        for i in keyPressPermutationgraph1:
            pressKeyBit+=bitBin[i-1] #압축 순열 리스트 인덱싱하여 압축

        for i in pressKeyBit: #DES1에 있는 display메소드를 사용하기위해 형식 맞추기
            bitHalf+=i
            count+=1
            if len(bitHalf)==8 or count==28 or count==56: #28단위로 넣어야 하기 때문에 24비트 채워지면 다음 비트는 4비트만 채움
                emptyList.append(bitHalf)
                bitHalf=''
            if len(emptyList)==4:
                pressKeyList.append(emptyList)
                emptyList=[]
        return pressKeyList #현재 28비트씩 나눠진 리스트 2개가 담겨있는 리스트와 56비트 압축된 문자열

    def keyShift(round,pressKeyList): #압축된 키 리스트를 받아 시프트하는 함수
        count=0
        roundKey=''
        roundShiftKey=[]
        emptyList=[]
        bitHalf=''
        for i in range(len(pressKeyList)):
            for j in range(len(pressKeyList[i])):
                roundKey+=pressKeyList[i][j] #2차원 리스트 문자열로

        if 1<=round<=2 or round==9 or round==16: #해당 라운드마다 1시프트
            lkey="".join(roundKey[1:28]+roundKey[0])
            rkey="".join(roundKey[29:]+roundKey[28])
        else: #해당 라운드에 2시프트
            lkey="".join(roundKey[2:28]+roundKey[0:2])
            rkey="".join(roundKey[30:]+roundKey[28:30])

        for i in lkey+rkey: #DES1에 있는 display메소드를 사용하기위해 형식 맞추기
            bitHalf+=i
            count+=1
            if len(bitHalf)==8 or count==28 or count==56: #28단위로 넣어야 하기 때문에 24비트 채워지면 다음 비트는 4비트만 채움
                emptyList.append(bitHalf)
                bitHalf=''
            if len(emptyList)==4:
                roundShiftKey.append(emptyList)
                emptyList=[]

        return roundShiftKey #2차원 리스트 왼,오 28비트 시프트키
        
    def keyPressPermutation2(roundShiftKey): #2번 째 압축 순열을 수행하는 함수
        keyPressPermutationgraph2=[14,17,11,24,1,5,3,28,15,6,21,10,23,19,12,4,26,8,16,7,27,20,13,2,41,52,31,37,47,55,30,40,51,45,33,48,44,49,39,56,34,53,46,42,50,36,29,32]
        pressRoundKey=[] #라운드키를 2차원 리스트에 저장하기 위한 리스트
        emptyList=[]
        emptyStr=''
        pressKey=''
        bit=''

        for i in range(len(roundShiftKey)):
            for j in range(len(roundShiftKey[i])):
                pressKey+=roundShiftKey[i][j] #2차원 리스트 문자열로

        for i in keyPressPermutationgraph2: #압출 순열표를 참고하여 2차원 리스트에 압축 순열 24비트씩 저장
            emptyStr+=pressKey[i-1]

        for i in emptyStr: #2차원 리스트로 만드는 알고리즘
            bit+=i
            if len(bit)%8==0:
                emptyList.append(bit)
                bit=''
        pressRoundKey.append(emptyList)
        
        return pressRoundKey #현재 8비트씩 나누어 2차원 리스트에 저장됨
            
        

