import wikipediaapi


def get_category(category_name):
    wiki_wiki = wikipediaapi.Wikipedia(language='ru', extract_format=wikipediaapi.ExtractFormat.HTML)
    category_items = wiki_wiki.page(category_name)
    return category_items.categorymembers.values()


def create_dict(category):
    dict_chars = {}
    for member in category:
        first_char = member.title[0]
        if first_char not in dict_chars.keys():
            dict_chars.update({first_char: 1})
        else:
            dict_chars[first_char] += 1
    return dict_chars.items()


if __name__ == '__main__':
    cat_name = 'Категория:Животные_по_алфавиту'
    dict_members = create_dict(category=get_category(cat_name))
    for key, values in dict_members:
        print(f'{key}: {values}')
