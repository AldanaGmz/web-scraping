import requests
import urllib.parse
import json

url="https://mfwkweb-api.clarovideo.net/services/nav/data?device_id=web&device_category=web&device_model=web&device_type=web&device_so=Chrome&format=json&device_manufacturer=generic&authpn=webclient&authpt=tfg1h3j4k6fd7&api_version=v5.92&region=argentina&HKS=gfcvrn7j10n1llbdht9k2pdqr7"
res=requests.get(url)
subcategorias=json.loads(res.text)

for subcategoria in subcategorias["response"]["nodes"]:
    if subcategoria["code"]=="nv_peliculas":
        for child in subcategoria["childs"]:
            if child["code"]=="nv_catalogo":
                data={}
                data["categorias"] = []
                for seccion in child["childs"]:
                    url2 = "https://mfwkweb-api.clarovideo.net/services/content/list?device_id=web&device_category=web&device_model=web&device_type=web&device_so=Chrome&format=json&device_manufacturer=generic&authpn=webclient&authpt=tfg1h3j4k6fd7&api_version=v5.92&region=argentina&HKS=gfcvrn7j10n1llbdht9k2pdqr7&order_id=200&order_way=DESC&level_id=GPS&from=0&quantity=200&node_id=75889"
                    params = {'node_id': seccion["id"]}
                    url_parts = list(urllib.parse.urlparse(url2))
                    query = dict(urllib.parse.parse_qsl(url_parts[4]))
                    query.update(params)
                    url_parts[4] = urllib.parse.urlencode(query)
                    link_seccion=urllib.parse.urlunparse(url_parts)
                    res=requests.get(link_seccion)
                    peliculas=json.loads(res.text)
                    data['peliculas'] = []
                    for pelicula in peliculas["response"]["groups"]:
                        data['peliculas'].append({
                            "id": pelicula["id"],
                            "titulo": pelicula["title"],
                            "descripcion": pelicula["description"],
                            "duracion": pelicula["duration"],
                            "formato_tipo": pelicula["format_types"],
                            "puntuacion": pelicula["votes_average"],
                        })
                    data['categorias'].append({
                        "categoria": seccion["text"],
                        "peliculas": data["peliculas"]
                    })
                data = {
                    "peliculas_catalogo":  data['categorias']
                }

            elif child["code"]=="nv_renta":
                data2={}
                data2["categorias"] = []
                for seccion in child["childs"]:
                    url2 = "https://mfwkweb-api.clarovideo.net/services/content/list?device_id=web&device_category=web&device_model=web&device_type=web&device_so=Chrome&format=json&device_manufacturer=generic&authpn=webclient&authpt=tfg1h3j4k6fd7&api_version=v5.92&region=argentina&HKS=gfcvrn7j10n1llbdht9k2pdqr7&order_id=200&order_way=DESC&level_id=GPS&from=0&quantity=200&node_id=75380"
                    params = {"node_id": seccion["id"]}
                    url_parts = list(urllib.parse.urlparse(url2))
                    query = dict(urllib.parse.parse_qsl(url_parts[4]))
                    query.update(params)
                    url_parts[4] = urllib.parse.urlencode(query)
                    link_seccion = urllib.parse.urlunparse(url_parts)
                    res = requests.get(link_seccion)
                    peliculas_renta = json.loads(res.text)
                    data2["peliculas_renta"] = []
                    for pelicula in peliculas_renta["response"]["groups"]:
                        data2["peliculas_renta"].append(
                            {
                                "Id": pelicula["id"],
                                "Titulo": pelicula["title"],
                                "Descripcion": pelicula["description"],
                                "Duracion": pelicula["duration"],
                                "formato_tipo": pelicula["format_types"],
                                "Puntuacion": pelicula["votes_average"],
                            }
                        )
                    data2['categorias'].append({
                        "categoria": seccion["text"],
                        "peliculas": data2["peliculas_renta"]
                    })
                data2 = {
                    "peliculas_alquiler":  data2['categorias']
                }

    elif subcategoria["code"] == "nv_series":
        for child in subcategoria["childs"]:
            data3={}
            if child["code"] == "nv_se_catalogo":
                data3["seccion"] = []
                for seccion in child["childs"]:
                    url3 = "https://mfwkweb-api.clarovideo.net/services/content/list?device_id=web&device_category=web&device_model=web&device_type=web&device_so=Chrome&format=json&device_manufacturer=generic&authpn=webclient&authpt=tfg1h3j4k6fd7&api_version=v5.92&region=argentina&HKS=9n5jk2prp8rqk71cjngflfo0u6&order_id=200&order_way=DESC&level_id=GPS&from=0&quantity=200&node_id=75743"
                    params = {"node_id": seccion["id"]}
                    url_parts = list(urllib.parse.urlparse(url3))
                    query = dict(urllib.parse.parse_qsl(url_parts[4]))
                    query.update(params)
                    url_parts[4] = urllib.parse.urlencode(query)
                    link_seccion = urllib.parse.urlunparse(url_parts)
                    res = requests.get(link_seccion)
                    series = json.loads(res.text)
                    data3["serie_data"] = []
                    for serie in series["response"]["groups"]:
                        url4 = "https://mfwkweb-api.clarovideo.net/services/content/serie?device_id=web&device_category=web&device_model=web&device_type=web&device_so=Chrome&format=json&device_manufacturer=generic&authpn=webclient&authpt=tfg1h3j4k6fd7&api_version=v5.92&region=argentina&HKS=9n5jk2prp8rqk71cjngflfo0u6&group_id=889068"
                        params = {"group_id": serie["id"]}
                        url_parts = list(urllib.parse.urlparse(url4))
                        query = dict(urllib.parse.parse_qsl(url_parts[4]))
                        query.update(params)
                        url_parts[4] = urllib.parse.urlencode(query)
                        link_series = urllib.parse.urlunparse(url_parts)
                        res = requests.get(link_series)
                        temporadas = json.loads(res.text)
                        data3["serie"] = []
                        data3["episodios"] = []
                        for temporada in temporadas["response"]["seasons"]:
                            for episodio in temporada["episodes"]:
                                data3["episodios"].append(
                                    {
                                        "Id": episodio["id"],
                                        "Titulo": episodio["title_episode"],
                                        "Descripcion": episodio["description"],
                                        "Duracion": episodio["duration"],
                                        "Formato": episodio["format_types"],
                                        "Puntuacion": episodio["votes_average"],
                                    }
                                )
                            data3['serie'].append({
                                "temporada": temporada["title"],
                                "episodios": data3["episodios"]
                            })
                        data3["serie_data"].append({
                            "titulo": serie['title'],
                            "serie":  data3['serie']
                        })
                    data3["seccion"].append({
                        "categoria": seccion["text"],
                        "series": data3["serie_data"]
                    })
                data3 = {
                    "series":  data3['seccion']
                }
                with open('claro-video.json', "w", encoding="utf-8") as file:
                    str((data, data2, data3)).encode('utf-8')
                    json.dump((data, data2, data3), file, indent=4, ensure_ascii=False)
