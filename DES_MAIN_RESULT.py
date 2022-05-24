# 라운드 돌리는 클래스
import Fstpermutation
import ProduceKey
import OperatingF
import SBOX
import PBOX

saveResult=[]
fristPermutation = Fstpermutation.FristPermutation
keySting=ProduceKey.KeySting
calculation=OperatingF.Operating
sBox=SBOX.S_Box
pBox=PBOX.P_Box
count=0

plain = input("평문을 입력하세요 : ")
keyValue=input("키를 입력해 주세요(8자리) : ")
plain = fristPermutation.paddingPlain(plain) #패딩 결과 저장
binPlain = fristPermutation.changeBit(plain) #문자열 -> 비트열
fristPermutationResult=fristPermutation.fristPermutationMapping(fristPermutation,binPlain) #초기순열결과 저장
keyPressPermutation1=keySting.keyPressPermutation1(keyValue) #압축 순열 결과를 변수에 저장

for i in range(16):
    keyShift=keySting.keyShift(i,keyPressPermutation1) #라운드 마다 시프트를 다르게 하여 저장하는 메소드
    keyPressPermutation2=keySting.keyPressPermutation2(keyShift) #압축순열 2 결과
    extendPlain=fristPermutation.extendPermutation(fristPermutationResult) # 32bit 평문 확장
    xorResult=calculation.operatingExclusive(extendPlain,keyPressPermutation2) #평문48bit calculation 키
    sBoxResult=sBox.sBoxRepalce(sBox,xorResult) #s-box결과
    pBoxResult=pBox.pBoxReplace(sBoxResult) #p-box결과
    roundR32Bit=calculation.operatingExclusive(fristPermutationResult,pBoxResult) #pbox결과 xor평문
    keyPressPermutation1=keyShift #시프트 결과를 저장하여 다음 시프트 함수에 넣기위한 변수
    fristPermutationResult=[fristPermutationResult[1],roundR32Bit[0]] #평문 오른쪽 32bit를 왼쪽 평문,마지막 xor결과를 오른쪽 평문으로
    saveResult.append(fristPermutationResult) #결과를 하나의 리스트에 저장
else:
    saveResult[-1][0],saveResult[-1][1]=saveResult[-1][1],saveResult[-1][0] #마지막 라운드 서로 바꿈

for i in saveResult: # 1~16라운드 결과
    print("[{0} 라운드 결과]".format(count+1)) #전역변수 count를 통하여 라운드 당 비트열을 표현
    calculation.displayBit(i)  
    count+=1
#최종 순열 결과
print("[64bit 블록 암호화 결과]")
finalRoundResult = calculation.FinalPermutation(saveResult)
calculation.displayBit(finalRoundResult) #최종 순열 거친 뒤 결과 출력
print(finalRoundResult)
    


    

    


