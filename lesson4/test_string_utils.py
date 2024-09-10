import pytest
from StringUtils import StringUtils


@pytest.fixture
def string_utils():
    return StringUtils()


# Позитивные тесты
@pytest.mark.positive
@pytest.mark.parametrize(
    "input_str, expected",
    [
        ("skypro", "Skypro"),  # обычное слово
        ("python", "Python"),  # строка с маленькими буквами
        ("skypro academy", "Skypro academy"),  # строка с несколькими словами
    ],
)
def test_capitalize_positive(string_utils, input_str, expected):
    assert string_utils.capitilize(input_str) == expected


# Негативные тесты
@pytest.mark.negative
@pytest.mark.parametrize(
    "input_str, expected",
    [
        ("", ""),  # пустая строка
        ("   ", "   "),  # строка, состоящая из пробелов
        (
            None,
            None,
        ),  # значение None (но тут потребуется изменение метода для обработки None)
    ],
)
def test_capitalize_negative(string_utils, input_str, expected):
    if input_str is None:
        with pytest.raises(AttributeError):
            string_utils.capitilize(input_str)
    else:
        assert string_utils.capitilize(input_str) == expected


@pytest.fixture
def string_utils():
    return StringUtils()


# Позитивные тесты
@pytest.mark.positive
@pytest.mark.parametrize(
    "input_str, expected",
    [
        ("   skypro", "skypro"),  # удаление пробелов в начале строки
        (
            "   skypro academy",
            "skypro academy",
        ),  # удаление пробелов только в начале строки
        ("skypro", "skypro"),  # строка без пробелов в начале
    ],
)
def test_trim_positive(string_utils, input_str, expected):
    assert string_utils.trim(input_str) == expected


# Негативные тесты
@pytest.mark.negative
@pytest.mark.parametrize(
    "input_str, expected",
    [
        ("", ""),  # пустая строка, результат пустая строка
        ("   ", ""),  # строка с только пробелами, результат пустая строка
        ("text", "text"),  # строка без пробелов, результат такая же строка
    ],
)
def test_trim_negative(string_utils, input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.fixture
def string_utils():
    return StringUtils()


# Позитивные тесты
@pytest.mark.positive
@pytest.mark.parametrize(
    "input_str, delimeter, expected",
    [
        ("a,b,c,d", ",", ["a", "b", "c", "d"]),  # разделение строки по запятой
        ("1:2:3", ":", ["1", "2", "3"]),  # разделение строки по двоеточию
        (
            "apple orange banana",
            " ",
            ["apple", "orange", "banana"],
        ),  # разделение строки по пробелу
    ],
)
def test_to_list_positive(string_utils, input_str, delimeter, expected):
    assert string_utils.to_list(input_str, delimeter) == expected


# Негативные тесты
@pytest.mark.negative
@pytest.mark.parametrize(
    "input_str, delimeter, expected",
    [
        ("", ",", []),  # пустая строка с разделителем, результат пустой список
        (
            "",
            "",
            [],
        ),  # пустая строка с пустым разделителем, результат пустой список
        (
            "a,b,c",
            None,
            ["a,b,c"],
        ),  # разделитель не найден, результат - исходная строка в списке
    ],
)
def test_to_list_negative(string_utils, input_str, delimeter, expected):
    if input_str is None:
        assert string_utils.to_list(input_str, delimeter) == expected
    else:
        assert string_utils.to_list(input_str, delimeter) == expected


@pytest.fixture
def string_utils():
    return StringUtils()


# Позитивные тесты
@pytest.mark.positive
@pytest.mark.parametrize(
    "input_str, symbol, expected",
    [
        ("SkyPro", "S", True),  # символ найден в строке
        ("SkyPro", "o", True),  # символ найден в строке
        ("SkyPro", "U", False),  # символ не найден в строке
    ],
)
def test_contains_positive(string_utils, input_str, symbol, expected):
    assert string_utils.contains(input_str, symbol) == expected


# Негативные тесты
@pytest.mark.negative
@pytest.mark.parametrize(
    "input_str, symbol, expected",
    [
        ("", "", False),  # пустая строка и пустой символ, результат False
        (
            "SkyPro",
            "",
            False,
        ),  # непустая строка и пустой символ, результат False
        ("SkyPro", "z", False),  # символ не найден в строке, результат False
    ],
)
def test_contains_negative(string_utils, input_str, symbol, expected):
    assert string_utils.contains(input_str, symbol) == expected


@pytest.fixture
def string_utils():
    return StringUtils()


# Позитивные тесты
@pytest.mark.positive
@pytest.mark.parametrize(
    "input_str, symbol, expected",
    [
        ("SkyPro", "k", "SyPro"),  # удаление одиночного символа
        ("hello world", "o", "hell wrld"),  # удаление всех вхождений символа
        ("abcabcabc", "abc", ""),  # удаление всей подстроки
    ],
)
def test_delete_symbol_positive(string_utils, input_str, symbol, expected):
    assert string_utils.delete_symbol(input_str, symbol) == expected


# Негативные тесты
@pytest.mark.negative
@pytest.mark.parametrize(
    "input_str, symbol, expected",
    [
        (
            "SkyPro",
            "",
            "SkyPro",
        ),  # удаление пустого символа, строка не изменяется
        ("SkyPro", "z", "SkyPro"),  # символ отсутствует, строка не изменяется
        (
            "",
            "a",
            "",
        ),  # удаление символа из пустой строки, результат пустая строка
    ],
)
def test_delete_symbol_negative(string_utils, input_str, symbol, expected):
    assert string_utils.delete_symbol(input_str, symbol) == expected


@pytest.fixture
def string_utils():
    return StringUtils()


# Позитивные тесты
@pytest.mark.positive
@pytest.mark.parametrize(
    "input_str, symbol, expected",
    [
        ("SkyPro", "S", True),  # строка начинается с символа "S"
        ("SkyPro", "Sk", True),  # строка начинается с символов "Sk"
        ("SkyPro", "P", False),  # строка не начинается с символа "P"
    ],
)
def test_starts_with_positive(string_utils, input_str, symbol, expected):
    assert string_utils.starts_with(input_str, symbol) == expected


# Негативные тесты
@pytest.mark.negative
@pytest.mark.parametrize(
    "input_str, symbol, expected",
    [
        ("", "S", False),  # пустая строка не начинается с символа "S"
        (
            "SkyPro",
            "",
            True,
        ),  # строка начинается с пустой строки, что всегда True
        ("Hello", "H", True),  # строка начинается с символа "H"
    ],
)
def test_starts_with_negative(string_utils, input_str, symbol, expected):
    assert string_utils.starts_with(input_str, symbol) == expected


@pytest.fixture
def string_utils():
    return StringUtils()


# Позитивные тесты
@pytest.mark.positive
@pytest.mark.parametrize(
    "input_str, symbol, expected",
    [
        ("SkyPro", "o", True),  # строка заканчивается символом "o"
        ("SkyPro", "Pro", True),  # строка заканчивается подстрокой "Pro"
        ("SkyPro", "P", False),  # строка не заканчивается символом "P"
    ],
)
def test_end_with_positive(string_utils, input_str, symbol, expected):
    assert string_utils.end_with(input_str, symbol) == expected


# Негативные тесты
@pytest.mark.negative
@pytest.mark.parametrize(
    "input_str, symbol, expected",
    [
        ("", "o", False),  # пустая строка не заканчивается на символ "o"
        (
            "SkyPro",
            "",
            True,
        ),  # строка заканчивается на пустую строку, что всегда True
        (
            "HelloWorld",
            "World",
            True,
        ),  # строка заканчивается на подстроку "World"
    ],
)
def test_end_with_negative(string_utils, input_str, symbol, expected):
    assert string_utils.end_with(input_str, symbol) == expected


@pytest.fixture
def string_utils():
    return StringUtils()


# Позитивные тесты
@pytest.mark.positive
@pytest.mark.parametrize(
    "input_str, expected",
    [
        ("", True),  # пустая строка
        (
            "   ",
            True,
        ),  # строка состоит только из пробелов (после триммирования)
        (
            " \t\n",
            True,
        ),  # строка содержит пробелы, табуляцию и перевод строки (после триммирования)
    ],
)
def test_is_empty_positive(string_utils, input_str, expected):
    assert string_utils.is_empty(input_str) == expected


# Негативные тесты
@pytest.mark.negative
@pytest.mark.parametrize(
    "input_str, expected",
    [
        ("SkyPro", False),  # непустая строка
        (" a ", False),  # строка с пробелами, но не пустая
        ("123", False),  # строка с числовыми символами
    ],
)
def test_is_empty_negative(string_utils, input_str, expected):
    assert string_utils.is_empty(input_str) == expected


@pytest.fixture
def string_utils():
    return StringUtils()


# Позитивные тесты
@pytest.mark.positive
@pytest.mark.parametrize(
    "input_list, joiner, expected",
    [
        (
            [1, 2, 3, 4],
            ", ",
            "1, 2, 3, 4",
        ),  # список чисел с разделителем по умолчанию
        (
            ["Sky", "Pro"],
            ", ",
            "Sky, Pro",
        ),  # список строк с разделителем по умолчанию
        (
            ["Sky", "Pro"],
            "-",
            "Sky-Pro",
        ),  # список строк с пользовательским разделителем
    ],
)
def test_list_to_string_positive(string_utils, input_list, joiner, expected):
    assert string_utils.list_to_string(input_list, joiner) == expected


# Негативные тесты
@pytest.mark.negative
@pytest.mark.parametrize(
    "input_list, joiner, expected",
    [
        ([], ", ", ""),  # пустой список
        ([1], ", ", "1"),  # список с одним элементом
        (
            [1, 2, 3],
            "",
            "123",
        ),  # список с несколькими элементами и пустой разделитель
    ],
)
def test_list_to_string_negative(string_utils, input_list, joiner, expected):
    assert string_utils.list_to_string(input_list, joiner) == expected
