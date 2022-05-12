
import DES1
import DES2
import DES3

fristPermutation = DES1.FristPermutation
keySting=DES2.KeySting
xor=DES3.Operating

while True:
        plain = input("평문을 입력하세요 : ")
        plain = fristPermutation.paddingPlain(plain)
        print("[평문 문자열]",'\n','>>>',plain,sep='')
        binPlain = fristPermutation.changeBit(plain)
        print("[평문 비트열]")
        fristPermutation.displayBit(binPlain)
        print("[초기순열 결과]")
        fristPermutationResult=fristPermutation.fristPermutationMapping(fristPermutation,binPlain) #초기순열
        fristPermutation.displayBit(fristPermutationResult)
        print("[초기순열 결과 32bit 단위]")
        fristPermutation.displayBit(fristPermutation.display32Bit(fristPermutationResult))

        keyValue=input("키를 입력해 주세요(8자리) : ")

        print("[키 비트열]")
        keyValueBit=fristPermutation.changeBit(keyValue) #DES1.py의 changeBit(문자열을 8비트 씩 저장하는 2차원 리스트로 만드는 메소드)
        fristPermutation.displayBit(keyValueBit) #위의 결과를 표현하는 displayBit
        print("[압축순열1 결과]")
        keyPressPermutation1=keySting.keyPressPermutation1(keyValue) #압축 순열 결과를 변수에 저장
        fristPermutation.displayBit(keyPressPermutation1) #압축 순열 결과를 표현하는 메소드에 파라미터로 압축순열 결과 전달

        print("[시프트 결과]")
        keyShift=keySting.keyShift(1,keyPressPermutation1) #현재 1 라운드 이지만 라운드 함수를 만들어 전역변수 round를 라운드마다 카운트 할 것
        fristPermutation.displayBit(keyShift) #키 시프트 결과 출력

        print("[압축순열2 결과]")
        keyPressPermutation2=keySting.keyPressPermutation2(keyShift)
        fristPermutation.displayBit(keyPressPermutation2)

        print("[오른쪽 평문 32bit 확장 순열 결과]")
        extendKey=fristPermutation.extendPermutation(fristPermutationResult)
        fristPermutation.displayBit(extendKey)

        print("[XOR연산 결과]")
        xorResult=xor.operatingExclusive(extendKey,keyPressPermutation2)
        fristPermutation.displayBit(xorResult)

        
        

