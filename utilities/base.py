import re
import html


patterns = {
    '[àáảãạăắằẵặẳâầấậẫẩ]': 'a',
    '[đ]': 'd',
    '[èéẻẽẹêềếểễệ]': 'e',
    '[ìíỉĩị]': 'i',
    '[òóỏõọôồốổỗộơờớởỡợ]': 'o',
    '[ùúủũụưừứửữự]': 'u',
    '[ỳýỷỹỵ]': 'y'
}


def convert_text(text):
    """

    Convert from 'Tieng Viet co dau' thanh 'Tieng Viet khong dau'

    text: input string to be converted

    :return: string converted
    """

    output = text
    for regex, replace in patterns.items():
        output = re.sub(regex, replace, output)
        # deal with upper case
        output = re.sub(regex.upper(), replace.upper(), output)
    return output.lower()


def convert_file_name(file_name):
    file_name = file_name.replace('\n', ' ')
    file_name = file_name.replace(':', '_')
    file_name = file_name.strip()
    file_name = file_name.replace(' ', '_')
    file_name = file_name.replace('/', '_')
    file_name = file_name.replace('*', '_')
    file_name = file_name.replace('?', '_')
    file_name = file_name.replace('<', '_')
    file_name = file_name.replace('>', '_')
    file_name = file_name.replace('"', "'")
    return file_name


def convert_pixel_to_number(pixel):
    num = re.sub(r'[(a-z)*]', '', pixel)
    num = float(num) if '.' in num else int(num)
    return num


def get_avatar_from_src(href):
    return href.split('/', 5)[-1]


def get_title_from_src(href):
    return href.rsplit('/', 1)[-1]


def remove_space(before_str):
    return ' '.join(before_str.split())


def convert_html_to_string(before_str):
    return html.unescape(before_str)
