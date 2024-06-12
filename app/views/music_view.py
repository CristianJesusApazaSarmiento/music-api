def musica_lista(musicas):
    return[
        {
            "id": musica.id,
            "titulo":musica.titulo,
            "artista":musica.artista,
            "duracion":musica.duracion,
        }
        for musica in musicas
    ]
    
def musica_detalle(musica):
    return {
        "id": musica.id,
        "titulo":musica.titulo,
        "artista":musica.artista,
        "duracion":musica.duracion,
    }