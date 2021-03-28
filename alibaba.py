while True:
    HowItem = input("Кол-во предметов?").split(" ")
    PriceItem = input("Cтоимость предметов?").split(" ")

    if len(PriceItem) > int(HowItem[0]):
        print(f"Максимальное число предметов {HowItem[0]}")
    else:
         Max = []
         for i in PriceItem:
             Max.append(int(i))
         Max.sort()
    Total = 0
    for i in Max[len(Max) - int(HowItem[1]) : len(Max)]:
        Total += i
        print(Total)
