def f(start,finish):
    if start==finish:
        return 1
    if start>finish:
        return 0
    return f(start+2,finish)+f(start*4,finish)+f(start+1,finish)
print(f(2,25))
