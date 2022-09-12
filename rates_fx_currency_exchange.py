
class Solution:
    def function(rates, original, target):
        max_res = -1
        result = -1
        search_between = ""
        rates_list = rates.split(";")
        for rate in rates_list:
            group_rate = rate.split(',')
            if group_rate[0] == original:
                if group_rate[1] == target:
                    result = float(group_rate[2])
                    max_res = max(max_res, result)
                else:
                    search_between = group_rate[1]
                    carry_over_rate = float(group_rate[2])
                    for rate in rates_list:
                        group_rate = rate.split(',')
                        if group_rate[0] == search_between and group_rate[1] == target:
                            result = float(group_rate[2]) * carry_over_rate
                            max_res = max(max_res, result)

        return float(max_res)



    result = function("USD,CAD,1.3;USD,GBP,0.71;USD,JPY,109;GBP,JPY,155", "USD", "JPY")
    result1 = function("USD,GBP,0.7;USD,JPY,109;GBP,JPY,155;CAD,CNY,5.27;CAD,KRW,921", "USD", "CNY")
    print(result)
    print(result1)
