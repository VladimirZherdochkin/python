# some_text = "зафиксированная на забвение каком-либо материальном набвтеле человеческая мысль. Абв бабвгэдэ абв"
# splitted_text = some_text.split()
# text_rem=some_text.replace('абв',"")
# modified_text = []
# # print(text_rem)
# # print(splitted_text)
# for i in range(len(splitted_text)):
#     if 'абв' in splitted_text[i].lower():
#         continue
#     else: modified_text.append(splitted_text[i])
# print(modified_text)
# string_modified_text = " ".join(modified_text)
# print(string_modified_text)

# my_text = 'Напишите абв напиабв програбвмму программу, удаляющую из \
#     этого абв текста все вабвс слова, содерабващие содержащие "абв"'

# def del_some_words(my_text):
#     my_text = list(filter(lambda x: 'абв' not in x, my_text.split()))
#     return " ".join(my_text)


# my_text = del_some_words(my_text)
# print(my_text)

text = "Я знаю, что ничеабвго не знаю. "

text = list(filter(lambda x: "абв" not in x, text.split()))
text = " ".join(text)

print(text)
