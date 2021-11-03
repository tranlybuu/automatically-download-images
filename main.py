import folder, web
import os

os.system('cls')

""" tạo thư mục DATA """
path = folder.setup_folder()

""" nhập keyword và tạo thư mục chứa ảnh chuẩn bị tải về """
keyword = str(input("> Keyword: ")).strip()
anpath = folder.create_keyword_folder(path, keyword)
if path == False:
    print("\n- Already have data for this keyword - \n")
else:
    keyword = keyword.replace(" ", "+")
    url = f'https://www.google.com/search?q={keyword}&source=lnms&tbm=isch'
    web.open_web(url)