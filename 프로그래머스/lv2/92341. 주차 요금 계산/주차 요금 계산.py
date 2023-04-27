from collections import defaultdict
import math

def solution(fees, records):
    car_fee_time = defaultdict(int)
    car_time = defaultdict(lambda:-1)
    car_fee = {}
    
    for record in records:
        time, number, inout = record.split()
        hour, minute = map(int, time.split(':'))
        if inout == 'IN':
            car_time[number] = hour*60 + minute
        else:
            car_fee_time[number] += (hour*60 + minute - car_time[number])
            car_time[number] = -1
    
    norm_time, norm_fee, unit_time, unit_fee = fees
    
    for num in car_time.keys():
        if car_time[num] != -1:
            car_fee_time[num] += (23*60+59 - car_time[num])
        
        if norm_time >= car_fee_time[num]:
            car_fee[num] = norm_fee
        else:
            car_fee[num] = norm_fee + math.ceil((car_fee_time[num] - norm_time) / unit_time)*unit_fee
    

    
    answer = []

    for key, value in sorted(car_fee.items(), key = lambda x: x[0]):
        answer.append(value)

    return answer







"""
[180, 5000, 10, 600]
['05:34 5961 IN', '06:00 0000 IN', '06:34 0000 OUT', '07:59 5961 OUT', '07:59 0148 IN', '18:59 0000 IN', '19:09 0148 OUT', '22:59 5961 IN', '23:00 5961 OUT']

누적 주차 시간이 기본 시간이하라면, 기본 요금을 청구
누적 주차 시간이 기본 시간을 초과하면, 기본 요금에 더해서, 초과한 시간에 대해서 단위 시간 마다 단위 요금을 청구
차량 번호가 작은 자동차부터 청구할 주차 요금을 차례대로 정수 배열에 담아서 return
"""
