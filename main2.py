
class Main():
    tracenum=0
    def get_question(self):
        print("*******질문*******")
        print("놀러 갈 사람이 혼자입니끼?")
        people=int(input("혼자면:1, 2명 이상이면:2 ==>"))
        if people ==1:

            print("1인 기준으로 돈 여유는?")
            money = int(input("10000원 이하:1, 2, 10000원 넘는다.==>"))
            if money == 1: #이쪽은 돈이없다
                travel = []
                while True:
                    print("여행하고 싶은 시간은? ")
                    result = int(input("1~2시간:1, 2~3시간:2, 3~4시간:3 , 그 이상:4==>"))
                    if result == 1:
                        print('출력테스트')
                        global tracenum
                        tracenum =1
                        return tracenum
                        break
                    elif result ==2:
                        tracenum = 2
                        return tracenum

                        break
                    elif result == 3:
                        tracenum = 3
                        return tracenum
                        break
                    elif result == 4:
                        tracenum = 4
                        return tracenum
                        break
                    else:
                        print("1,2,3,4中 택1")

            elif money == 2: #돈이 많다. 이쪽은

                while True:
                    print("여행하고 싶은 시간은? ")
                    result = int(input("1~2시간:1, 2~3시간:2, 3~4시간:3 , 그 이상:4==>"))
                    if result == 1:
                        tracenum = 5
                        return tracenum
                        break
                    elif result ==2:
                        tracenum = 6
                        return tracenum
                        break
                    elif result ==3:
                        tracenum = 7
                        return tracenum
                    elif result ==4:
                        tracenum = 8
                        return tracenum
                        break
                    else:
                        print("1,2,3,4中 택1")
            else:
                print("잘못 누르신거죠? ")
        elif people ==2: # 사람이 다수이다
            print("1인 기준으로 돈 여유는?")
            money = int(input("10000원 이하:1, 2, 10000원 넘는다.==>"))
            if money == 1:
                print("여행하고 싶은 시간은? ")
                result = int(input("1~2시간:1, 2~3시간:2, 3~4시간:3 , 그 이상:4==>"))
                while True:
                    print("여행하고 싶은 시간은? ")
                    result = int(input("1~2시간:1, 2~3시간:2, 3~4시간:3 , 그 이상:4==>"))
                    if result == 1:
                        tracenum = 9
                        return tracenum
                        break
                    elif result == 2:
                        tracenum = 10
                        return tracenum
                        break
                    elif result == 3:
                        tracenum = 11
                        return tracenum
                        break
                    elif result == 4:
                        tracenum = 12
                        return tracenum
                        break
                    else:
                        print("1,2,3,4中 택1")
            elif money == 2:
                while True:
                    print("여행하고 싶은 시간은? ")
                    result = int(input("1~2시간:1, 2~3시간:2, 3~4시간:3 , 그 이상:4==>"))
                    if result == 1:
                        tracenum = 13
                        return tracenum
                        break
                    elif result == 2:
                        tracenum = 14
                        return tracenum
                        return tracenum
                        break
                    elif result == 3:
                        tracenum = 15
                        return tracenum
                        return tracenum
                        break
                    elif result == 4:
                        tracenum = 16
                        return tracenum
                        break

                    else:
                        print("1,2,3,4中 택1")
            else:
                print("잘못 누르신거죠? ")

        else:
            print("1,2中 택1")
    def get_travel(self):
        print("======================")
        print("당신에게 맞는 놀거리는...")
        print("↓↓↓↓↓↓↓↓↓↓")

        global tracenum
        if tracenum ==1:
            answer = ["배다리저수지"]
            print(answer)
            print("그냥 음악 들으면서 여기 몇바뀌도는것도 좋음 옆에있는 도서관 완전 최근 건물이라 짱임!")
        elif tracenum ==2:
            answer = ["나태한책방"]
            print(answer)
            print("솔직히 혼자 쫌 오래있기는 도서관이나 책방이 낫지않나?")
        elif tracenum ==3:
            answer = ["더마룸"]
            print(answer)
            print("혼자여도 여기 닌텐도도 있고 영화도 됨. 돈도 8000원!")
        elif tracenum ==4:
            answer = ["배다리"]
            print(answer)
            print("배다리에서 놀다가 옆에있는 도서관에서 구경하다가 그냥 소사벌 구경하면됨. 나도 그랬음..ㅋ")
        elif tracenum ==5:
            answer = ["짱오락실"]
            print(answer)
        elif tracenum ==6:
            answer = ["아르카북스",'스타필드','ak플라자']
            print(answer)
        elif tracenum ==7:
            answer = ["그림한잔"]
            print(answer)
            print("바싸긴하지만 혼자서 엄청 안심심할꺼다.")
        elif tracenum ==8:
            answer = ["소사벌"]
            print(answer)
            print("딱 어디라 단정 짓기 어려움. 혼자라서 어디에서 오래 머물기도 지루할터라 그냥 소사벌 여행하는걸 추천 돈도 있으니 할거 많은것 장담")
        elif tracenum ==9:
            answer = ["놀러와다락방","평택호"]
            print(answer)
            print("2020에 핫했던 이곳!과 호수지만 둘이서 오면 은근 데이트장소 ")
        elif tracenum ==10:
            answer = ["더마룸",'공간의공감']
            print(answer)
        elif tracenum ==11:
            answer = ["fff"]
            print(answer)
        elif tracenum ==12:
            answer = ["fff"]
            print(answer)
        elif tracenum ==13:
            answer = ["방탈출카페"]
            print(answer)
            print("4군데 다 동등하게 2인 44000원 1시간은 스릴로 보낼수 있음")
        elif tracenum ==14:
            answer = ["안성팜랜드"]
            print(answer)
        elif tracenum ==15:
            answer = ["스타필드"]
            print(answer)
            print("여기서 하루쟁일 있어도됨. 뭐 오락실에다 카페, 서점, 밥집 액세서리 다있음")
        else:
            answer = ["트리하우스"]
            print(answer)
            print("1박2일 영화에 나올만한 집. 돈 쫌 많이 필요")
    def star(self):
        print("------------------------------")
        print("혹시 다른사람의 평가가 궁금하다면?")
        #print("후기 본다:1, 그냥 끝낸다:2")
        result = int(input("후기 본다:1, 그냥 끝낸다:2 ==>"))
        if result ==1:
            print("후기가 없습니다. 본인이 입력하세요")
            while (True):
                star = int(input("이 장소에 대한 별점은?(1~5까지):"))
                if star > 5:
                    print("1~5중 선택하세요")
                else:
                    break
        elif result ==2:
            pass



t= Main()
t.get_question()
t.get_travel()
t.star()
