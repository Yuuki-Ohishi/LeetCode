import math

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        str1_num = len(str1)
        str2_num = len(str2)
        num_box = [str1_num, str2_num]
        str_box = [str1, str2]

        max_index = num_box.index(max(num_box))
        min_index = num_box.index(min(num_box))

        if max_index == min_index:
            min_index = 1

        numbers = list(range(1, 1001))

        min_str = str_box[min_index]
        flag = 0
        return_word_box = []
        return_word_num = []
        for k in range(num_box[min_index]):
            test_str = min_str[:k+1]
            #print(test_str)
            for j in range(len(numbers)):
                if len(str_box[max_index]) < len(test_str*numbers[j]):
                    break

                if str_box[max_index]==test_str*numbers[j]:
                    return_word_box.append(test_str)
                    return_word_num.append(numbers[j])
                    flag +=1
                    
                    #最初に一致するword
                    if flag==1:
                        first_word = test_str
                        flag += 1

        if flag > 0:
            if len(return_word_box)==1:
                last_check = len(min_str)/len(return_word_box[0])
                if min_str != return_word_box[0]*int(last_check):
                    return ""
                return return_word_box[0]
            
            for l in range(len(return_word_box)):
                if len(min_str) % len(return_word_box[len(return_word_box)-l-1]) == 0:
                    last_check = len(min_str)/len(return_word_box[len(return_word_box)-l-1])
                    if min_str != return_word_box[len(return_word_box)-l-1]*int(last_check):
                        return ""

                    return return_word_box[len(return_word_box)-l-1]

            return return_word
        
        return ""

                
                 

           


        



        