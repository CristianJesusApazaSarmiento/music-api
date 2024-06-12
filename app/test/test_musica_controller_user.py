def test_get_musicas_as_user(test_client, user_auth_headers):
    response = test_client.get("/api/musicas", headers=user_auth_headers)
    assert response.status_code == 200
    assert response.json == []
    
def test_create_musica(test_client, admin_auth_headers):
    data = {
        "titulo": "Even",
        "artista": "Bad Omens",
        "duracion": 2.45,
    }
    response = test_client.post("/api/musicas", json=data, headers=admin_auth_headers)
    assert response.status_code == 201
    assert response.json["titulo"]=="Even"
    assert response.json["artista"]=="Bad Omens"
    assert response.json["duracion"]==2.45
    
def test_get_musica_as_user(test_client, user_auth_headers):
    response = test_client.get("/api/musicas/1", headers=user_auth_headers)
    assert response.status_code == 200
    assert "titulo" in response.json
    assert "artista" in response.json
    assert "duracion" in response.json

def test_create_musica_as_user(test_client, user_auth_headers):
    data = {
        "titulo": "Dragout",
        "artista": "Dexcore",
        "duracion": 4.25,
    }
    response = test_client.post("/api/musicas", json=data, headers=user_auth_headers)
    assert response.status_code == 403
    
def test_update_musica_as_user(test_client, user_auth_headers):
    data = {
        "titulo": "Dragout",
        "artista": "None", 
        "duracion": 1.40,
    }
    response = test_client.put("/api/musicas/1", json=data, headers=user_auth_headers)
    assert response.status_code==403
    
def test_delete_musica_as_user(test_client, user_auth_headers):
    response = test_client.delete("/api/musicas/1", headers=user_auth_headers)
    assert response.status_code == 403