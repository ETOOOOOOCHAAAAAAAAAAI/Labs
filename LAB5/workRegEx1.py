# re.match(pattern, string) - Проверяет, соответствует ли начало строки шаблону.
# re.search(pattern, string) - Ищет по всей строке, но возвращает только первое найденное совпадение.
# re.findall(pattern, string) - Находит все совпадения с шаблоном в строке и возвращает их в виде списка.
# re.finditer(pattern, string) - Находит все совпадения с шаблоном в строке и возвращает их в виде итератора совпадений.
# re.sub(pattern, repl, string) - Заменяет все совпадения шаблона в строке на другую подстроку.
import re


def find_ab(string):
        return re.fullmatch("ab*", string) is not None


print(find_ab("a"))
print(find_ab("abbbb"))
print(find_ab("cacacaabbbb"))