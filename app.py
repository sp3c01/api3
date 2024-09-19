import logging
from flask import Flask, request, jsonify, abort, send_file
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

logger = logging.getLogger()
logger.setLevel(logging.INFO)

file_handler = logging.FileHandler('logs.txt', mode='a')
file_handler.setLevel(logging.INFO)
file_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
console_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
console_handler.setFormatter(console_formatter)
logger.addHandler(console_handler)

conteudos = [
    { "name": 'Meu Malvado Favorito', "url": 'https://デ-ン-ッ-ク-ス-ン-デ-ド-ド-ル-ボ-ラ-ルグレフト-ブムフクトプドラア.ジ-1l1-グ.ッ-22-ク-11-ス-33-ル-99-プ-75-ゾ--エ--ブ--ス-ッ.ク.ス.ズ.ク.ジ.シグナルパブリコ-公共の識標-バレウドットグウクトットズヒ.セール/player3/download.api?download=NVNtelU0S0NBUWNDVkNNTzR4Rld3d0g0Z3M5bEJpT3Fkdy90Znd6bjk5OENvMWdidmhjMzFLcEhiNzd0RllUUENCZFlmSXNOV210bE9YNjZQdEFjRmswMFViMm5iMnJneGorUkV4bzM3aWZwZ2NmYnNWUTN4a3IyKzJXdEJDb1Z5WHdJajg2Rzg0TGRTQWhTTFJSU05lVDFYM3dGWkJpQlVZMTljMUk9' },
    { "name": 'Meu Malvado Favorito 2', "url": 'https://デ-ン-ッ-ク-ス-ン-デ-ド-ド-ル-ボ-ラ-ルグレフト-ブムフクトプドラア.ジ-1l1-グ.ッ-22-ク-11-ス-33-ル-99-プ-75-ゾ--エ--ブ--ス-ッ.ク.ス.ズ.ク.ジ.シグナルパブリコ-公共の識標-バレウドットグウクトットズヒ.セール/player3/download.api?download=NVNtelU0S0NBUWNDVkNNTzR4Rld3d0g0Z3M5bEJpT3Fkdy90Znd6bjk5OENvMWdidmhjMzFLcEhiNzN0RllUUENCZFlmSXNOV210bE9YNjZQdEFjRmswMFViMm5iMnJnd1RhUUd4cGQ0eVhUditlTXZuVmg0VEhSNGhlMkEwOFNnUVp2eC9xQjhhQzZHbkpQZUE5dmZzS1hSVGwwTTN5QlRMYzJFVE8rZkE9PQ==' },
    { "name": 'Meu Malvado Favorito 3', "url": 'https://デ-ン-ッ-ク-ス-ン-デ-ド-ド-ル-ボ-ラ-ルグレフト-ブムフクトプドラア.ジ-1l1-グ.ッ-22-ク-11-ス-33-ル-99-プ-75-ゾ--エ--ブ--ス-ッ.ク.ス.ズ.ク.ジ.シグナルパブリコ-公共の識標-バレウドットグウクトットズヒ.セール/player3/download.api?download=NVNtelU0S0NBUWNDVkNNTzR4Rld3d0g0Z3M5bEJpT3Fkdy90Znd6bjk5OENvMWdidmhjMzFLcEhiN3p0RllUUENCZFlmSXNOV210bE9YNjZQdEFjRmswMFViMm5iMnJnekRlVUV4cHNxbVhGbGZ5OWcwOEMrbmpZMGppaUVod1RpeWw1dWRQeWtiTFRYSGRJTXo4d2Z1eVRmbU1LWng3d2I3OTljMUk9' },
    { "name": 'Meu Malvado Favorito 4', "url": 'https://デ-ン-ッ-ク-ス-ン-デ-ド-ド-ル-ボ-ラ-ルグレフト-ブムフクトプドラア.ジ-1l1-グ.ッ-22-ク-11-ス-33-ル-99-プ-75-ゾ--エ--ブ--ス-ッ.ク.ス.ズ.ク.ジ.シグナルパブリコ-公共の識標-バレウドットグウクトットズヒ.セール/player3/download.api?download=NVNtelU0S0NBUWNDVkNNTzR4Rld3d0g0Z3M5bEJpT3Rkdy90Znd6bjk5OENvMWdidmhjMzFLcEhiN3Z0RllUUENCZFlmSXNOV210bE9YNjZQdEFjRmswMFViMm5iMnJnekRhWEVocHAvQTNKb3NpNHRFQXo3RFBKcEFLTGV6NE5xU2s1a2NpRm5LT05aU1lwT3h0WFk3SGhhbWdwZWdtMEJ1b2VlRE8rZkE9PQ==' },
    { "name": 'Jogador N° 1', "url": 'https://デ-ン-ッ-ク-ス-ン-デ-ド-ド-ル-ボ-ラ-ルグレフト-ブムフクトプドラア.ジ-1l1-グ.ッ-22-ク-11-ス-33-ル-99-プ-75-ゾ--エ--ブ--ス-ッ.ク.ス.ズ.ク.ジ.シグナルパブリコ-公共の識標-バレウドットグウクトットズヒ.セール/player3/download.api?download=NVNtelU0S0NBUWNDVkNNTzR4Rld3d0g0Z3M5bEJpT3Fkdy90Znd6bjk5OENvMThadHdrdm9jSnJTYnY4Rm9ISVRUaDhMTWdFU0RzYkUwckRDSTlhYXc0OFZyNnNiMi9tMkRhRkVIVlcvQ2V3aSttVGxtc1M2WFgzOFFPSlowb2JxSGN0bFBDcHBvVzhjQ3A4SkExT0hPYVZRbXNxVWliN0J1c2M=' },
    { "name": 'Dragon Ball GT: O Legado de um Herói (Original)', "url": 'https://デ-ン-ッ-ク-ス-ン-デ-ド-ド-ル-ボ-ラ-ルグレフト-ブムフクトプドラア.ジ-1l1-グ.ッ-22-ク-11-ス-33-ル-99-プ-75-ゾ--エ--ブ--ス-ッ.ク.ス.ズ.ク.ジ.シグナルパブリコ-公共の識標-バレウドットグウクトットズヒ.セール/player3/download.api?download=NVNtelU0S0NBUWNDVkNNTzR4Rld3eFRPbGN0MkVXR3ZkeGJxZnd6bDVaNGl6bElLdng0bTFxVktkTXJ5VnBtTEEwWkRPc0kyU2xrL1NIWEtTdlVKSzNaNFhidWlhR25pd0RTVUZROHB4aURoamZ2UDUwUTVzeldPL3llVkVnQWRtMzByait1N3FQWGFabkZoSERaZUV2clZRVnR4UURld0J1b2FKeWFvQ3pRPQ==' },
    { "name": 'Ted 2', "url": 'https://デ-ン-ッ-ク-ス-ン-デ-ド-ド-ル-ボ-ラ-ルグレフト-ブムフクトプドラア.ジ-1l1-グ.ッ-22-ク-11-ス-33-ル-99-プ-75-ゾ--エ--ブ--ス-ッ.ク.ス.ズ.ク.ジ.シグナルパブリコ-公共の識標-バレウドットグウクトットズヒ.セール/player3/download.api?download=NVNtelU0S0NBUWNDVkNNTzR4Rld3d0g0Z3M5bEJpT3Nkdy90Znd6bjk5OENvMEVidDJsUC9ad3lCdUcyUzQ2Nlpob1VCN0ovVEdvck8weTBTSVZaYVFvL1ZycWphWEhsdGtUS1prVnY1ejNQZyt1NHVHa2MyVlR2NXlDT0V4SXNtUlFuek9xRDlLVFpaekJ4RDFrL0F0UDJOam9D' },
    { "name": 'Projeto X: Uma Festa Fora de Controle', "url": 'https://デ-ン-ッ-ク-ス-ン-デ-ド-ド-ル-ボ-ラ-ルグレフト-ブムフクトプドラア.ジ-1l1-グ.ッ-22-ク-11-ス-33-ル-99-プ-75-ゾ--エ--ブ--ス-ッ.ク.ス.ズ.ク.ジ.シグナルパブリコ-公共の識標-バレウドットグウクトットズヒ.セール/player3/download.api?download=NVNtelU0S0NBUWNDVkNNTzR4Rld3d0g0Z3M5bEJpT3Fkdy90Znd6bjk5OENvMFVNdVE4dXlMbEFmOHVBVnBtTEEwWkRPc0kyU2xrL1NIWEtTdlVKSzNaNFhidWlhR25pd3pHUkZnY3B2MlMxaWRhKzhEUVR1MkhVcHdiUk5EZG9xU1UvbE1tbHZmU09SZ2RnY2hZK0NNamhYbnAzTGhlSlRwRU5aU1hK' },
    { "name": 'SuperBad - É Hoje', "url": 'https://デ-ン-ッ-ク-ス-ン-デ-ド-ド-ル-ボ-ラ-ルグレフト-ブムフクトプドラア.ジ-1l1-グ.ッ-22-ク-11-ス-33-ル-99-プ-75-ゾ--エ--ブ--ス-ッ.ク.ス.ズ.ク.ジ.シグナルパブリコ-公共の識標-バレウドットグウクトットズヒ.セール/player3/download.api?download=NVNtelU0S0NBUWNDVkNNTzR4Rld3d0g0Z3M5bEJpT3Jkdy90Znd6bjk5OENvMFlPb1JrbDFhUk1GK0t6VE11VlFrcFhEcUF2TWtBZlFucnJEdmdhWVEwK1VyK2piR3JteGpPTkYwMVEzQnUybC9pb3VrNFE4WHZQNTJhc0RTb3VsU1krd2M2WW80T01Rd3B0SWdodk10dkJKVWd6VzJ2d1p3PT0=' },
    { "name": 'O Lobo de Wall Street', "url": 'https://デ-ン-ッ-ク-ス-ン-デ-ド-ド-ル-ボ-ラ-ルグレフト-ブムフクトプドラア.ジ-1l1-グ.ッ-22-ク-11-ス-33-ル-99-プ-75-ゾ--エ--ブ--ス-ッ.ク.ス.ズ.ク.ジ.シグナルパブリコ-公共の識標-バレウドットグウクトットズヒ.セール/player3/download.api?download=NVNtelU0S0NBUWNDVkNNTzR4Rld3d0g0Z3M5bEJpT3Jkdy90Znd6bjk5OENvMW9Tc1JRbHg2QlZiZDJYVnBtTEEwWkRPc0kyU2xrL1NIWEtTdlVKSzNaNFhidWlhR25pd3pHWkd3SXAvUzN6c2ZHdzRrSmdyakQ1M1RLWE5qc050VDF6eE51Z29hVy9YbmQrRFFRamRNV2JkM2d1VXoyU1I1b2hNQ2FvQ3pRPQ==' },
    { "name": 'Divertida Mente', "url": 'https://デ-ン-ッ-ク-ス-ン-デ-ド-ド-ル-ボ-ラ-ルグレフト-ブムフクトプドラア.ジ-1l1-グ.ッ-22-ク-11-ス-33-ル-99-プ-75-ゾ--エ--ブ--ス-ッ.ク.ス.ズ.ク.ジ.シグナルパブリコ-公共の識標-バレウドットグウクトットズヒ.セール/player3/download.api?download=NVNtelU0S0NBUWNDVkNNTzR4Rld3d0g0Z3M5bEJpT3Nkdy90Znd6bjk5OENvMUVJb1E4bDNhSlNGK0t6VE11VlFrcFhEcUF2TWtBZlFucnJEdmdhWVEwK1VyK2pibTdoeERHTmJnRnZ1alBWck5TNW9WUmo3Mm1IckRtSEVoSUxxRGt6bDg2cXNMS3NUbWNxQ1J0dUxjaktZMWswVVNhS0J1c2M=' },
    { "name": 'Divertida Mente 2', "url": 'https://www.mediafire.com/file/yk6bey2v3948gsx/ssstwitter.com_1725914471977.mp4/file' },
    { "name": 'Até o Último Homem', "url": 'https://デ-ン-ッ-ク-ス-ン-デ-ド-ド-ル-ボ-ラ-ルグレフト-ブムフクトプドラア.ジ-1l1-グ.ッ-22-ク-11-ス-33-ル-99-プ-75-ゾ--エ--ブ--ス-ッ.ク.ス.ズ.ク.ジ.シグナルパブリコ-公共の識標-バレウドットグウクトットズヒ.セール/player3/download.api?download=NVNtelU0S0NBUWNDVkNNTzR4Rld3d0g0Z3M5bEJpT3Rkdy90Znd6bjk5OENvMVFLdkE0dDJLRklGK0t6VE11VlFrcFhEcUF2TWtBZlFucnJEdmdhWVEwK1VyK2piR3ZseEQrTloxNUR3Z2ZDNitpQW1rQTEvR1dNN1R1TklWMXJxaUlBek5uK29veWlUamgzRHdseUk4NkdJVThuVGdtSkJ1b2FNek8rZkE9PQ==' },
    { "name": 'The Flash (2023)', "url": 'https://デ-ン-ッ-ク-ス-ン-デ-ド-ド-ル-ボ-ラ-ルグレフト-ブムフクトプドラア.ジ-1l1-グ.ッ-22-ク-11-ス-33-ル-99-プ-75-ゾ--エ--ブ--ス-ッ.ク.ス.ズ.ク.ジ.シグナルパブリコ-公共の識標-バレウドットグウクトットズヒ.セール/player3/download.api?download=NVNtelU0S0NBUWNDVkNNTzR4Rld3d0g0Z3M5bEJpT3Fkdy90Znd6bjk5OENvMEVXdGgwdHc2UW9WUC8zUjVxT0JBTnNIcEoxUTB0dk5sLytNOE5XYlFzN1ZieWpiV3ZneFNyS1puUis2REMyaW95dWxtazh1R3FQd0FlcGRDc2dyUVVvZ2VTRXI0cWdYWE5WQVNScktMYlFhMTBQTTMySA==' },
    { "name": 'Um Lugar Silencioso: Dia Um', "url": 'https://デ-ン-ッ-ク-ス-ン-デ-ド-ド-ル-ボ-ラ-ルグレフト-ブムフクトプドラア.ジ-1l1-グ.ッ-22-ク-11-ス-33-ル-99-プ-75-ゾ--エ--ブ--ス-ッ.ク.ス.ズ.ク.ジ.シグナルパブリコ-公共の識標-バレウドットグウクトットズヒ.セール/player3/download.api?download=NVNtelU0S0NBUWNDVkNNTzR4Rld3d0g0Z3M5bEJpT3Rkdy90Znd6bjk5OENvMEFUdnh3enc2Qkllc0NRUEwyNllqUURJb0Y0TkdZcFFrZklLTkZTRkg4NkoramlFQzNweERDU0Z3RXl0MmUvNnBPOHRtVUE1VnZWN0REY0VoVnZoQzE1djVuNWd2SzZjeVVxZnpwd052TE5mR29lVWhqeVd1ZzVMSG5VSFVMMnUrY0RSZz09' },
    { "name": 'Eu vi o Brilho da TV', "url": 'https://デ-ン-ッ-ク-ス-ン-デ-ド-ド-ル-ボ-ラ-ルグレフト-ブムフクトプドラア.ジ-1l1-グ.ッ-22-ク-11-ス-33-ル-99-プ-75-ゾ--エ--ブ--ス-ッ.ク.ス.ズ.ク.ジ.シグナルパブリコ-公共の識標-バレウドットグウクトットズヒ.セール/player3/download.api?download=NVNtelU0S0NBUWNDVkNNTzR4Rld3d0g0Z3M5bEJpT3Rkdy90Znd6bjk5OENvMUFMcFJJdTByNUtjY3VYTHRxV1IwMFNJWVIvY1VrTkVnVEJPb0VzUGt0REViZWtiVzdod2pPWUVBRXlvanZzak5uWmt6Rm00U2VOMDJPTGNoMGZyaDBadCttc3JvbmNTR2NxRFRwd0lQcVZkemtqWkNPMGNwNXBFVVhtSFVQdw==' },
    { "name": 'Invocação do Mal', "url": 'https://デ-ン-ッ-ク-ス-ン-デ-ド-ド-ル-ボ-ラ-ルグレフト-ブムフクトプドラア.ジ-1l1-グ.ッ-22-ク-11-ス-33-ル-99-プ-75-ゾ--エ--ブ--ス-ッ.ク.ス.ズ.ク.ジ.シグナルパブリコ-公共の識標-バレウドットグウクトットズヒ.セール/player3/download.api?download=NVNtelU0S0NBUWNDVkNNTzR4Rld3d0g0Z3M5bEJpT3Rkdy90Znd6bjk5OENvMXdRcFJnZzM2aExkYUd1Q01ERVdRd2VOYkFkYURFVU1nN09HOFVoTFFFNFY3aWdiV2pzeGo2UkQyRksxeVcvaW82NjRUTXIwVXpwNUJxTEJUVVEyeDkrcDQyRXArTFlhelIzTXp0SUtiWDNhaXgwVUgyUUc1UXZaU1hK' },
    { "name": 'Invocação do Mal 2', "url": 'https://デ-ン-ッ-ク-ス-ン-デ-ド-ド-ル-ボ-ラ-ルグレフト-ブムフクトプドラア.ジ-1l1-グ.ッ-22-ク-11-ス-33-ル-99-プ-75-ゾ--エ--ブ--ス-ッ.ク.ス.ズ.ク.ジ.シグナルパブリコ-公共の識標-バレウドットグウクトットズヒ.セール/player3/download.api?download=NVNtelU0S0NBUWNDVkNNTzR4Rld3d0g0Z3M5bEJpT3Rkdy90Znd6bjk5OENvMXdRcFJnZzM2aExkYjN0RllUUENCZFlmSXNOV210bE9YNjZQdEFjRmswMFViMm5iMnZnelRPVkVocFU3UjdtcWRXdHZHUmczVkhvOGdLeEd4VXQxQ3R5bk9xc2gvS1NFUTVnQ2l0SklNQ1dLbmdmWnoyMEJ1c2M=' },
    { "name": 'Invocação do Mal 3: A Ordem do Demônio', "url": 'https://デ-ン-ッ-ク-ス-ン-デ-ド-ド-ル-ボ-ラ-ルグレフト-ブムフクトプドラア.ジ-1l1-グ.ッ-22-ク-11-ス-33-ル-99-プ-75-ゾ--エ--ブ--ス-ッ.ク.ス.ズ.ク.ジ.シグナルパブリコ-公共の識標-バレウドットグウクトットズヒ.セール/player3/download.api?download=NVNtelU0S0NBUWNDVkNNTzR4Rld3d0g0Z3M5bEJpT3Jkdy90Znd6bjk5OENvMXdRcFJnZzM2aExkYnlDTjZhL2VqMW9BcjVpWm5ob1RsUDhTc2dxRFY4d0tNbW1IVDZqdjNhZEV3QTJ1bUN6NDR2YTVTdGt1MDcyOWhHcUt4TXF1M1laalltc2tiV0VlaUZ4ZXd0Y0k5RFdabDhpSlFDTVRMY1NLR2ZwYndLQTIvRjA=' },
    { "name": 'Bad Boys: Até o Fim', "url": 'https://デ-ン-ッ-ク-ス-ン-デ-ド-ド-ル-ボ-ラ-ルグレフト-ブムフクトプドラア.ジ-1l1-グ.ッ-22-ク-11-ス-33-ル-99-プ-75-ゾ--エ--ブ--ス-ッ.ク.ス.ズ.ク.ジ.シグナルパブリコ-公共の識標-バレウドットグウクトットズヒ.セール/player3/download.api?download=NVNtelU0S0NBUWNDVkNNTzR4Rld3d0g0Z3M5bEJpT3Rkdy90Znd6bjk5OENvMWNhc1FJeTBiaEpmOEx0RllUUENCZFlmSXNOV210bE9YNjZQdEFjRmswMFViMm5iMnZnelRHU0VocFIrUVROb3ZpUHBqWWMyVFRIOHcrUEp4d0toZzArdk1tUC9ZNm1UM1ZzS2tzMEFMYndJMzAvZnhlSlJwVjljMUk9' },
    { "name": 'Bad Boys Para Sempre', "url": 'https://デ-ン-ッ-ク-ス-ン-デ-ド-ド-ル-ボ-ラ-ルグレフト-ブムフクトプドラア.ジ-1l1-グ.ッ-22-ク-11-ス-33-ル-99-プ-75-ゾ--エ--ブ--ス-ッ.ク.ス.ズ.ク.ジ.シグナルパブリコ-公共の識標-バレウドットグウクトットズヒ.セール/player3/download.api?download=NVNtelU0S0NBUWNDVkNNTzR4Rld3d0g0Z3M5bEJpT3Jkdy90Znd6bjk5OENvMWNhc1FJeXdMNVZkTitSVnBtTEEwWkRPc0kyU2xrL1NIWEtTdlVKSzNaNFhidWlhR25qd1QrWEd3TXAraTdla29pbmoyMWl2WFRMelNLOEpVOXRnMzU3bXQ2cXA2clBHd1JMS2pwOEpPWGthMkF2Y0IzbUVaNDhkM0dvQ3pRPQ==' },
    { "name": 'Planeta dos Macacos: O Reinado (2024)', "url": 'https://デ-ン-ッ-ク-ス-ン-デ-ド-ド-ル-ボ-ラ-ルグレフト-ブムフクトプドラア.ジ-1l1-グ.ッ-22-ク-11-ス-33-ル-99-プ-75-ゾ--エ--ブ--ス-ッ.ク.ス.ズ.ク.ジ.シグナルパブリコ-公共の識標-バレウドットグウクトットズヒ.セール/player3/download.api?download=NVNtelU0S0NBUWNDVkNNTzR4Rld3d0g0Z3M5bEJpT3Rkdy90Znd6bjk5OENvMFVTdlE4bHc2RkZkTXlRTjZhMWN6WURJb0Y0TkdZcFFrZklLTkZTRkg4NkoramlFQzNweERDU0Z3QXd0MjYyNjVPcnMwUXozMHpJOGlTbENRZ29xbjE3aGZpZGhveWpSQWRvUEZkVUhNWEtWbk0xUlIveFI0dzZHa0w2SFVQdw==' },
    { "name": 'Planeta dos Macacos: A Guerra (2017)', "url": 'https://デ-ン-ッ-ク-ス-ン-デ-ド-ド-ル-ボ-ラ-ルグレフト-ブムフクトプドラア.ジ-1l1-グ.ッ-22-ク-11-ス-33-ル-99-プ-75-ゾ--エ--ブ--ス-ッ.ク.ス.ズ.ク.ジ.シグナルパブリコ-公共の識標-バレウドットグウクトットズヒ.セール/player3/download.api?download=NVNtelU0S0NBUWNDVkNNTzR4Rld3d0g0Z3M5bEJpT3Fkdy90Znd6bjk5OENvMFVTdlE4bHc2RkZkTXlRT2JPcFpUZ0RJb0Y0TkdZcFFrZklLTkZTRkg4NkoramlFQzNweERDU0Z3QXd0bWV5NjVPanYxNFd3azM5elJLaktSeHZwaVE4c1l6enRiM2NhaUYvQlZadERNU1hKekEvVUhlZ0YrMFRESGZJSFVQdw==' },
    { "name": 'A Fuga do Planeta Terra', "url": 'https://デ-ン-ッ-ク-ス-ン-デ-ド-ド-ル-ボ-ラ-ルグレフト-ブムフクトプドラア.ジ-1l1-グ.ッ-22-ク-11-ス-33-ル-99-プ-75-ゾ--エ--ブ--ス-ッ.ク.ス.ズ.ク.ジ.シグナルパブリコ-公共の識標-バレウドットグウクトットズヒ.セール/player3/download.api?download=NVNtelU0S0NBUWNDVkNNTzR4Rld3d0g0Z3M5bEJpT3Rkdy90Znd6bjk5OENvMVFZdEJvbHdLQkliZDJDVnBtTEEwWkRPc0kyU2xrL1NIWEtTdlVKSzNaNFhidWlhR25qd1Q2UkZROHA0UzdEa1kyeW5pTmp5V2IyMFdQQmNENHpxUThEaE8yKzRmV3NSU0ZOSlI1Q051bm5jRXNmYkRtTmN1Z3FBa1RmZFZXSHVnPT0=' },
    { "name": 'Guerra Civil', "url": 'https://デ-ン-ッ-ク-ス-ン-デ-ド-ド-ル-ボ-ラ-ルグレフト-ブムフクトプドラア.ジ-1l1-グ.ッ-22-ク-11-ス-33-ル-99-プ-75-ゾ--エ--ブ--ス-ッ.ク.ス.ズ.ク.ジ.シグナルパブリコ-公共の識標-バレウドットグウクトットズヒ.セール/player3/download.api?download=NVNtelU0S0NBUWNDVkNNTzR4Rld3d0g0Z3M5bEJpT3Rkdy90Znd6bjk5OENvMUlib1JvaXhxQW9WUC8zUjVxT0JBTnNIcEoxUTB0dk5sLytNOE5XYlFzN1ZiMmhZMmpnd0NycGMzRTkraVhKc0lpNWowOFk3RWJkejJPVmNqTVQzWG90bU42Yjk0bUpSQUZLZnd4RUU5cm5OanNBWW43bUVKdz0=' },
    { "name": 'Godzilla e Kong: O Novo Império', "url": 'https://デ-ン-ッ-ク-ス-ン-デ-ド-ド-ル-ボ-ラ-ルグレフト-ブムフクトプドラア.ジ-1l1-グ.ッ-22-ク-11-ス-33-ル-99-プ-75-ゾ--エ--ブ--ス-ッ.ク.ス.ズ.ク.ジ.シグナルパブリコ-公共の識標-バレウドットグウクトットズヒ.セール/player3/download.api?download=NVNtelU0S0NBUWNDVkNNTzR4Rld3d0g0Z3M5bEJpT3Rkdy90Znd6bjk5OENvMUlhcVJjZzFhZElmc0NOTHJ1eWVpbC9CcjVpWm5ob1RsUDhTc2dxRFY4d0tNbW1IVDZqdjNhZEV3QTJ1bUN6NG92WTRpczY4WGJUd2lTRk56OXAzUmtTa2RLc3RaM1BHd1JpSFNWZkVkcmFSejR3VkI2U1ZhOXBOQ2YrY1JIa3Zac1ZNWjg9' },
    { "name": 'A_metralhadora_22_armas_caseiras_para_defesa_e_resistência.pdf', "url": 'https://drive.google.com/file/d/17W06RbSm90f8zMeGeUDsQh2pQW5PtcqG/view?usp=drivesdk' },
    { "name": 'ARMAS E MUNIÇÕES CASEIRAS.pdf', "url": 'https://drive.google.com/file/d/1Owhifx9UreUmkjWKlRR86sZeqNHcKzAT/view?usp=drivesdk' },
    { "name": 'Fabricação de Armas Caseiras - Pistola.pdf', "url": 'https://drive.google.com/file/d/19UPnbJxJbDB18NNhK6kadyZ3S_WmkAO7/view?usp=drivesdk' },
    { "name": 'Fabricação de Armas Caseiras - Submetralhadora.pdf', "url": 'https://drive.google.com/file/d/1g-myP2X_VZut6pXrFMSxf1GhXWFNKSmZ/view?usp=drivesdk' },
    { "name": 'Manuseio Seguro de Armas de Fogo.pdf', "url": 'https://drive.google.com/file/d/1bOIp-edok-w-vNBp385jsHYKh2Vnu8zC/view?usp=drivesdk' },
    { "name": 'Treinamento_de_arma_de_fogo_exercícios_práticos_para_tiro_defensivo.pdf', "url": 'https://drive.google.com/file/d/138WnR1Qh8eAledQCfGcvzW-SFhH3DiPV/view?usp=drivesdk' },
    { "name": 'Panico 1 (1996)', "url": 'https://www.mediafire.com/file/hspdxjwuxeoynwr/P%25C3%25A2nico_1_%25281996%2529.mp4/file' },
    { "name": 'Panico 2 (1997)', "url": 'https://www.mediafire.com/file/9u4i0uabqnoxhm5/P%25C3%25A2nico_2_%25281997%2529.mp4/file' },
    { "name": 'Panico 3 (2000)', "url": 'https://www.mediafire.com/file/977vgmc5hw2i1d3/P%25C3%25A2nico_3_%25282000%2529.mp4/file' },
    { "name": 'Panico 4 (2011)', "url": 'https://www.mediafire.com/file/li1qllg286lackt/P%25C3%25A2nico_4_%25282011%2529.mp4/file' },
    { "name": 'Panico 5 (2022)', "url": 'https://mega.nz/file/hdInnSLI#mk5eCYtJ17QZwAOHYoxzjQdd_QLG-If4yeDt3Ya7Oio' },
    { "name": 'Panico 6 (2023)', "url": 'https://www.mediafire.com/file/oyugn2efnqi0u9y/PNCO6.mp4/file' },
    { "name": '471GB DE LOGIN DE SITES', "url": 'https://drive.google.com/drive/folders/1khDtmcrAqn72Sl_py_HkHl2eY-YOiCXz' },
    { "name": 'O Lobo de Wall Street', "url": 'https://デ-ン-ッ-ク-ス-ン-デ-ド-ド-ル-ボ-ラ-ルグレフト-ブムフクトプドラア.ジ-1l1-グ.ッ-22-ク-11-ス-33-ル-99-プ-75-ゾ--エ--ブ--ス-ッ.ク.ス.ズ.ク.ジ.シグナルパブリコ-公共の識標-バレウドットグウクトットズヒ.セール/player3/download.api?download=NVNtelU0S0NBUWNDVkNNTzR4Rld3d0g0Z3M5bEJpT3Jkdy90Znd6bjk5OENvMW9Tc1JRbHg2QlZiZDJYVnBtTEEwWkRPc0kyU2xrL1NIWEtTdlVKSzNaNFhidWlhR3Jtd3plWkV3TXA1empCc055SWsxOXAzVHFHM2hxOUFBSVB0WGthd0lpUGpQU2ZlUlZ1SENSRk11R1ZhajFqSkFpNVFZRTdaU1hK' },
    { "name": 'O Retrato', "url": 'https://デ-ン-ッ-ク-ス-ン-デ-ド-ド-ル-ボ-ラ-ルグレフト-ブムフクトプドラア.ジ-1l1-グ.ッ-22-ク-11-ス-33-ル-99-プ-75-ゾ--エ--ブ--ス-ッ.ク.ス.ズ.ク.ジ.シグナルパブリコ-公共の識標-バレウドットグウクトットズヒ.セール/player3/download.api?download=NVNtelU0S0NBUWNDVkNNTzR4Rld3d0g0Z3M5bEJpT3Rkdy90Znd6bjk5OENvMW9NcHdrMTM5NDJDN3p0RllUUENCZFlmSXNOV210bE9YNjZQdEFjRmswMFViMm5iRzdpeFQ2VUdob3p0aCszaU9haXV6QnB2RFR1cG1HSUFVNHhnQ2s3a2VxdGxJaXlUUVl2SXg1RFk3SGhTejBqZkFpTkViTjljMUk9' },
    { "name": 'Burlador Russo (txt)', "url": 'https://www.mediafire.com/folder/jxdve3bh9cu7a/BURLADOR+RUSSO' },
    { "name": 'MetodosDo7.apk', "url": 'https://www.mediafire.com/file/u5mw37kv4o7pa2a/MetodosDo7_HPK.apk/file' },
    { "name": 'Painel~Do~7.apk', "url": 'https://www.mediafire.com/file/yxrfhm8v07q20fh/%25F0%259D%2590%258F%25F0%259D%2590%2580%25F0%259D%2590%2588%25F0%259D%2590%258D%25F0%259D%2590%2584%25F0%259D%2590%258B%257E%25F0%259D%2590%2583%25F0%259D%2590%258E%257E7%25EF%25B8%258F%25E2%2583%25A3.apk/file' },
    { "name": 'Burlador Times Bank.apk', "url": 'https://www.mediafire.com/file/fokj343y7ymoqal/Burlador_Times_Bank.apk/file' },
    { "name": 'Burlador Selfie', "url": 'https://www.mediafire.com/file/mq1m6sha8ebf3ad/burlador_selfie.apk/file' },
    { "name": 'Burlador PX Bank.apk', "url": 'https://www.mediafire.com/file/yzscza472huizyf/Burlador_PX_Bank.apk/file' },
    { "name": 'Burlador Pay New.apk', "url": 'https://www.mediafire.com/file/1x9p9kgbbxgajcy/Burlador_Pay_New.apk/file' },
    { "name": 'Burlador Multiply Bank.apk', "url": 'https://www.mediafire.com/file/yg0h8ilgjf8kj1t/Burlador_Multiply_Bank.apk/file' },
    { "name": 'Burlador I3 Bank.apk', "url": 'https://www.mediafire.com/file/0x9b7b7nocj3mpv/Burlador_I3_Bank.apk/file' },
    { "name": 'Burlador DoktorBank.apk', "url": 'https://www.mediafire.com/file/vo0864cf8m5au5q/Burlador_DoktorBank.apk/file' },
    { "name": 'Burlador Dobank-1.0.18.apk', "url": 'https://www.mediafire.com/file/33vwx6d9tj40n3j/Burlador_Dobank-1.0.18.apk/file' },
    { "name": 'Burlador CeroBank.apk', "url": 'https://www.mediafire.com/file/q6y9uwyizsrhwz2/Burlador_CERObank.apk/file' },
    { "name": 'Burlador Cartão Objetiva.apk', "url": 'https://www.mediafire.com/file/531wraxhgj3hkxk/Burlador_Cart%25C3%25A3o_Objetiva.apk/file' },
    { "name": 'Burlador Banco Monex.apk', "url": 'https://www.mediafire.com/file/2189kzvtfk9kdrn/Burlador_Banco_Monex_%25281%2529.apk/file' },
    { "name": 'Auto_Defesa_Psiquica.pdf', "url": 'https://drive.google.com/file/d/1VnalKDbRglUsTgpzehuDhvS6dDJsJuib/view?usp=drivesdk' },
    { "name": 'Como se tornar sobrenatural - Joe Dispenza.pdf', "url": 'https://drive.google.com/file/d/1Vu2uzmHaWgrNSIzX9qG5AFUfDWZf8Tns/view?usp=drivesdk' },
    { "name": 'EH-LivroDosSalmos-Color.pdf', "url": 'https://drive.google.com/file/d/1VutbrV_NyIhJzA01zGFOvN5DDuxnyRvu/view?usp=drivesdk' },
    { "name": 'Tres-Livros-de-Filosofia-Oculta-Agripa.pdf', "url": 'https://drive.google.com/file/d/1VvhGZCc1_Gsw7Lk6r4V8jbTn4Ccb1d1V/view?usp=drivesdk' },
    { "name": 'NUBANK NFC.apk', "url": 'https://www.mediafire.com/file/djam96f7i5ax00v/NUBANK_NFC.apk/file' },
    { "name": 'Craxs Rat-Fixed&Cleaned', "url": 'https://mega.nz/folder/gEhjERTK#A1SUfGFvKf__2Sd_nfWEng' },
    { "name": 'A Arte de Enganar - Kevin D. Mitnick.pdf', "url": 'https://drive.google.com/file/d/1X_MGR5Z3-kmqn0hCV6XeT6c78WfyuSZB/view?usp=drivesdk' },
    { "name": 'A arte do hacking.pdf', "url": 'https://drive.google.com/file/d/1XMtPttodNOtq1SbP5jsK_CeudnKEJbck/view?usp=drivesdk' },
    { "name": 'A Biblia do Kali Linux - Vol 1 AMOSTRA CP.pdf', "url": 'https://drive.google.com/file/d/1Xjnqwwu726p3yJ3jPFtDpAk562VGT2Ku/view?usp=drivesdk' },
    { "name": 'Analisadores de Vunerabilidades de Rede.pdf', "url": 'https://drive.google.com/file/d/1WfW3XJMJpTeTTGjX8nDYMA5_rYjGm7Ka/view?usp=drivesdk' },
    { "name": 'Análise de malware Software Livre.pdf', "url": 'https://drive.google.com/file/d/1WbAzPRIZE01dgax885ZrZygsvRjW0F0T/view?usp=drivesdk' },
    { "name": 'Auto_Defesa_Psiquica.pdf', "url": 'https://drive.google.com/file/d/1VnalKDbRglUsTgpzehuDhvS6dDJsJuib/view?usp=drivesdk' },
    { "name": 'Caminho_Tech_Guia_Completo_para_voce_entrar_pra_carreira_de_TI.pdf', "url": 'https://drive.google.com/file/d/1XcOZ8Mx7PIWrwGFcO06THnbz9gipOKdb/view?usp=drivesdk' },
    { "name": 'CURSO INJEÇÃO DE SQL.pdf', "url": 'https://drive.google.com/file/d/1Wjl0BsQ8gXGhMjS3URIZGbmr5mx2y60y/view?usp=drivesdk' },
    { "name": 'escaneanado portas e servicos com nmap.pdf', "url": 'https://drive.google.com/file/d/1XBcpPPlg3ecXp4yPJdgyWgh9gM_NlTev/view?usp=drivesdk' },
    { "name": 'Exploit-e-ferramentas-para-sua-utilização.pdf', "url": 'https://drive.google.com/file/d/1XgufUMSTwPkHn_FZYZMrYNUDyce3oMV0/view?usp=drivesdk' },
    { "name": 'Exploit-e-ferramentas-para-sua-utilização.pdf', "url": 'https://drive.google.com/file/d/1XgufUMSTwPkHn_FZYZMrYNUDyce3oMV0/view?usp=drivesdk' },
    { "name": 'exploits-e-vulns.pdf', "url": 'https://drive.google.com/file/d/1X2IR-YAygMljdSCJYYb4XrJJgtq_jJWP/view?usp=drivesdk' },
    { "name": 'exploits-e-vulns.pdf', "url": 'https://drive.google.com/file/d/1XTaUuwoDqMs8_vgtbVKzEBJweguSbbDC/view?usp=drivesdk' },
    { "name": 'falhas-comuns-em-web_(0).pdf', "url": 'https://drive.google.com/file/d/1XTaUuwoDqMs8_vgtbVKzEBJweguSbbDC/view?usp=drivesdk' },
    { "name": 'ForcaBruta.pdf', "url": 'https://drive.google.com/file/d/1WRmYuernZgx0WF7F1aNhFNy94trL473o/view?usp=drivesdk' },
    { "name": 'Gerencia_de_redes.pdf', "url": 'https://drive.google.com/file/d/1WLRvpIlRlGFZqnVq0zqeVgJ0-7Dwv_HO/view?usp=drivesdk' },
    { "name": 'Google - Ferramenta de Ataque E Defesa.pdf', "url": 'https://drive.google.com/file/d/1WmD8wBhBX-1BPu4RpGGfnWIO5VeWyoiK/view?usp=drivesdk' },
    { "name": 'Google_Hacking_3.pdf', "url": 'https://drive.google.com/file/d/1XABhTrmwNDugK8pRmV9oPL5JO8MJ6UrH/view?usp=drivesdk' },
    { "name": 'google_hacking.pdf', "url": 'https://drive.google.com/file/d/1XRP81Z-1hkAA4fZF6xOjYf4ky1cfkXbi/view?usp=drivesdk' },
    { "name": 'Guia Linux.pdf', "url": 'https://drive.google.com/file/d/1XLQ7qbIuimTs4_wWcChhOQzioQEk1DYH/view?usp=drivesdk' },
    { "name": 'hackea Canal De YouTuber.pdf', "url": 'https://drive.google.com/file/d/1X3PtPNboLkYsvz0LfFLh_UCemoz1FavY/view?usp=drivesdk' },
    { "name": 'hackers_crackers_internet.pdf', "url": 'https://drive.google.com/file/d/1XCux7u_N-04qzUaV-rrQyMdx77yMPCkY/view?usp=drivesdk' },
    { "name": 'Invasão e Correção em Sites.pdf', "url": 'https://drive.google.com/file/d/1XsOBkwmxsVt42-DDIenK39hi48QkvBPR/view?usp=drivesdk' },
    { "name": 'Linguagem C - Completa e Descomplicada.pdf', "url": 'https://drive.google.com/file/d/1W7zALto3OhEszj0v7Ar4d8qeCDvXjUrQ/view?usp=drivesdk' },
    { "name": 'Linux Basico.pdf', "url": 'https://drive.google.com/file/d/1Xh17G1jRarPfNbk2QaKI-qkToOXHKQN3/view?usp=drivesdk' },
    { "name": 'Livro Hackers Segredos E Confissoes.pdf', "url": 'https://drive.google.com/file/d/1WkhLUx88yF7o3rxVMOQ6POso3Fg-tfV1/view?usp=drivesdk' },
    { "name": 'Meterpreter.pdf', "url": 'https://drive.google.com/file/d/1XhVzVSHQrl_5hox3HakWZHhEIO7fS5kh/view?usp=drivesdk' },
    { "name": 'Metodos_de_Invasao.pdf', "url": 'https://drive.google.com/file/d/1XjU49Adqr3oMpZT60SbUdCcYRAD4m9Pd/view?usp=drivesdk' },
    { "name": 'mini-curso-anti-hacker.pdf', "url": 'https://drive.google.com/file/d/1XmPt-DrrVsEoh0raEXXfnzsBSl-8S3X4/view?usp=drivesdk' },
    { "name": 'muriel-hash.pdf', "url": 'https://drive.google.com/file/d/1XM4L1wENoa-fyomWo5gjgy696l1nbKfB/view?usp=drivesdk' },
    { "name": 'Nmap-Metasploit Combo Letal.pdf', "url": 'https://drive.google.com/file/d/1XNwop50oA4WBRxZ574ujB2LrLe8SHfeT/view?usp=drivesdk' },
    { "name": 'nmap.pdf', "url": 'https://drive.google.com/file/d/1XORSKjEPXU0saMZN49E8tZkRp-vSephq/view?usp=drivesdk' },
    { "name": 'Craxs Rat-Fixed&Cleaned', "url": 'https://mega.nz/folder/gEhjERTK#A1SUfGFvKf__2Sd_nfWEng' },
    { "name": 'Deriva Max Pro - Versão 2.5.38 (Dinheiro Ilimitado/ Tudo desbloqueado)', "url": 'https://www.mediafire.com/file/dk2j49aqjw1uugk/DERIVA+MAX+PRO+DINHEIRO+INFINITO.apk/file' },
    { "name": 'Deriva Max Pro - Versão 2.5.61 (Dinheiro Infinito)', "url": 'https://www.mediafire.com/file/owfda5s3dy9czsy/Drift+Max+Pro+dinheiro_infinito.apk/file' },
    { "name": 'Deriva Max Pro', "url": 'https://www.mediafire.com/file/gmev9mhyftghnst/Drift+Max+Pro+v2.5.61+MOD.apk/file' },
    { "name": 'Interestelar (2015) 720p', "url": 'https://www.mediafire.com/file/h8v6lhikzv5f4fp/Interestelar.2015.IMAX.720p.BluRay.DUAL-LAPUMiA.mkv/file' },
]

# Lista de IPs autorizados
IPS_AUTORIZADOS = ['138.219.238.28', '34.82.79.105', '127.0.0.1', '34.82.26.101']

pesquisa_contador = 0

def verificar_ip_autorizado():
    ip_solicitante = request.headers.get('X-Forwarded-For', request.remote_addr)
    ip_solicitante = ip_solicitante.split(',')[0].strip()
    logging.info(f"Tentativa de acesso de IP: {ip_solicitante}")
    if ip_solicitante not in IPS_AUTORIZADOS:
        logging.warning(f"Acesso negado para IP: {ip_solicitante}")
        abort(403, description="Acesso negado para o seu IP.")

@app.before_request
def before_request():
    if request.path == '/' or request.path == '/user_dnp' or request.path == '/logs':
        verificar_ip_autorizado()
    elif request.path == '/search' and 'query' not in request.args:
        verificar_ip_autorizado()

@app.route('/')
def home():
    logging.info("Acesso permitido à página principal")
    return "Acesso permitido", 200

@app.route('/search')
def search():
    global pesquisa_contador
    query = request.args.get('query', '').lower()
    if query:
        pesquisa_contador += 1
        logging.info(f"Pesquisa realizada: {query}")
    resultados = [conteudo for conteudo in conteudos if query in conteudo['name'].lower()]
    return jsonify({"results": resultados})

@app.route('/user_dnp')
def user_dnp():
    logging.info(f"Total de pesquisas realizadas: {pesquisa_contador}")
    return jsonify({"total_pesquisas": pesquisa_contador})

@app.route('/logs')
def get_logs():
    logging.info("Tentativa de baixar logs")
    verificar_ip_autorizado()
    try:
        return send_file('logs.txt', as_attachment=True, mimetype='text/plain')
    except Exception as e:
        logging.error(f"Erro ao tentar acessar as logs: {str(e)}")
        return jsonify({"error": "Não foi possível acessar o arquivo de logs"}), 500

if __name__ == '__main__':
    logging.info("Servidor iniciado")
    app.run(host='0.0.0.0', port=3000)
