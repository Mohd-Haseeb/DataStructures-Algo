def func(i:int):
    if i>5:
        return
    print("CFS ",i)
    func(i+1)

func(1)