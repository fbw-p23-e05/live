sample_text = 'Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim. Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. In enim justo, rhoncus ut, imperdiet a, venenatis vitae, justo. Nullam dictum felis eu pede mollis pretium. Integer tincidunt. Cras dapibus. Vivamus elementum semper nisi. Aenean vulputate eleifend tellus. Aenean leo ligula, porttitor eu, consequat vitae, eleifend ac, enim. Aliquam lorem ante, dapibus in, viverra quis, feugiat a, tellus. Phasellus viverra nulla ut metus varius laoreet. Quisque rutrum. Aenean imperdiet. Etiam ultricies nisi vel augue. Curabitur ullamcorper ultricies nisi. Nam eget dui. Etiam rhoncus. Maecenas tempus, tellus eget condimentum rhoncus, sem quam semper libero, sit amet adipiscing sem neque sed ipsum. Nam quam nunc, blandit vel, luctus pulvinar, hendrerit id, lorem. Maecenas nec odio et ante tincidunt tempus. Donec vitae sapien ut libero venenatis faucibus. Nullam quis ante. Etiam sit amet orci eget eros faucibus tincidunt. Duis leo. Sed fringilla mauris sit amet nibh. Donec sodales sagittis magna. Sed consequat, leo eget bibendum sodales, augue velit cursus nunc, quis gravida magna mi a libero. Fusce vulputate eleifend sapien. Vestibulum purus quam, scelerisque ut, mollis sed, nonummy id, metus. Nullam accumsan lorem in dui. Cras ultricies mi eu turpis hendrerit fringilla. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; In ac dui quis mi consectetuer lacinia. Nam pretium turpis et arcu. Duis arcu tortor, suscipit eget, imperdiet nec, imperdiet iaculis, ipsum. Sed aliquam ultrices mauris. Integer ante arcu, accumsan a, consectetuer eget, posuere ut, mauris. Praesent adipiscing. Phasellus ullamcorper ipsum rutrum nunc. Nunc nonummy metus. Vestibulum volutpat pretium libero. Cras id dui. Aenean ut eros et nisl sagittis vestibulum. Nullam nulla eros, ultricies sit amet, nonummy id, imperdiet feugiat, pede. Sed lectus. Donec mollis hendrerit risus. Phasellus nec sem in justo pellentesque facilisis. Etiam imperdiet imperdiet orci. Nunc nec neque. Phasellus leo dolor, tempus non, auctor et, hendrerit quis, nisi. Curabitur ligula sapien, tincidunt non, euismod vitae, posuere imperdiet, leo. Maecenas malesuada. Praesent congue erat at massa. Sed cursus turpis vitae tortor. Donec posuere vulputate arcu. Phasellus accumsan cursus velit. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Sed aliquam, nisi quis porttitor congue, elit erat euismod orci, ac placerat dolor lectus quis orci. Phasellus consectetuer vestibulum elit. Aenean tellus metus, bibendum sed, posuere ac, mattis non, nunc. Vestibulum fringilla pede sit amet augue. In donkey turpis. Pellentesque posuere. Praesent turpis. Aenean posuere, tortor sed cursus feugiat, nunc augue blandit nunc, eu sollicitudin urna dolor sagittis lacus. Donec elit libero, sodales nec, volutpat a, suscipit non, turpis. Nullam sagittis. Suspendisse pulvinar, augue ac venenatis condimentum, sem libero volutpat nibh, nec pellentesque velit pede quis nunc. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Fusce id purus. Ut varius tincidunt libero. Phasellus dolor. Maecenas vestibulum mollis.' # 197 + 5 = 202

word = 'mattis'

from random import randrange

# def find(word: str, text: str) -> int:
#     """Find a word in a string."""
#     word_len = len(word)
#     text_len = len(text)
#     found = False
#     while not found:
#         i = randrange(text_len - word_len) # 200, 5
#         if text[i : i + word_len] == word:
#             found = True
#     return i

# # import datetime as dt


import time


def find(word: str, text: str) -> int:
    """Find a word in a string."""
    word_len = len(word)
    text_len = len(text)


    for i in range(text_len - word_len): # 200 - 5 = 195
        if text[i : i + word_len] == word: # 194: 199
            return i
        
    return -1


# num_list = [20, 30, 44, 1, 3342, 101, 5]

# num_list[0]

# num_list[1]


# start = time.time()

# for i in range(10000):
#     find(word, sample_text)

# end = time.time()

# run_time = end - start

# print(run_time)



#!/usr/bin/env python

# import random
# import time
# import re

# # from find import find


# def main():
#     # with open("sample.txt") as f:
#     #     sample_text = f.read()
#     words = re.split("\s|(?<!\d)[,.](?!\d)", sample_text)
#     index_error = False
#     timer = 0
#     for i in range(0, 10000):
#         word = random.choice(words)
#         start = time.perf_counter()
#         index = find(word, sample_text)
#         end = time.perf_counter()
#         timer = timer + end - start
#         index_control = [_.start() for _ in re.finditer(word, sample_text)]
#         if index not in index_control:
#             index_error = True
#             print({"word": word, "index": index, "index_control": index_control})
#     if index_error:
#         print(
#             "Unfortunately your algorithm did not always find the correct index number."
#         )
#     else:
#         print("Congratulations, your algorithm always found the word correctly.")
#         print(f"It only took {timer} seconds to run it 10000 times.")


# if __name__ == "__main__":
#     main()





