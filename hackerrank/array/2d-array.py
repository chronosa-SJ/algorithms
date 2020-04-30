def hourglassSum(arr:list):
    # i : y의 길이(|), j = x의 길이(----)
    i = len(arr)
    j = len(arr[0])
    # 호리병 모양을 위해서는 결국 3*3 범위가 필요하므로
      # 이를 고려하여 검색할 수 있는 최대치를 계산
    try:
        i_max = i - 2
        j_max = j - 2
    except Exception as e:
        return 0
    
    my_sum = -99999
    temp_sum = 0
    
    # (0,0) 부터 (i_max, j_max)까지 반복하면서 호리병 영역의 값을 계산하고
      # 이전 max 값과 비교
    for y in range(i_max):
        for x in range(j_max):
            temp_sum = calc_hourglass(arr,y,x)
            my_sum = max(temp_sum, my_sum)
            print(f"{y},{x},{my_sum}") # Debuging
    
    return my_sum

def calc_hourglass(arr,y:int,x:int):
    temp_sum = 0
    temp_sum += arr[y][x]
    temp_sum += arr[y][x+1]
    temp_sum += arr[y][x+2]
    temp_sum += arr[y+1][x+1]
    temp_sum += arr[y+2][x]
    temp_sum += arr[y+2][x+1]
    temp_sum += arr[y+2][x+2]
    return temp_sum
