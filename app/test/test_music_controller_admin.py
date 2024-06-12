import pytest

def test_get_musicas(test_client, admin_auth_headers):
    response = test_client.get("/api/musicas", headers=admin_auth_headers)
    assert response.status_code==200
    assert response.json == []
    
def test_create_musica(test_client, admin_auth_headers):
    data = {
        "titulo": "Gray",
        "artista": "Bad Omens",
        "duracion": 3.25,
    }
    response = test_client.post("/api/musicas", json=data, headers=admin_auth_headers)
    assert response.status_code ==201
    assert response.json["titulo"]=="Gray"
    assert response.json["artista"]=="Bad Omens"
    assert response.json["duracion"]==3.25
    
def test_get_musica(test_client, admin_auth_headers):
    response = test_client.get("/api/musicas/1", headers=admin_auth_headers)
    assert response.status_code==200
    assert "titulo" in response.json
    
def test_get_nonexistent_musica(test_client, admin_auth_headers):
    response = test_client.get("/api/musicas/999", headers=admin_auth_headers)
    assert response.status_code==404
    assert response.json["error"]=="Musica no encontrada"
    
def test_create_musica_invalid_data(test_client, admin_auth_headers):
    data = {"titulo": "Exit Wounds"}
    response = test_client.post("/api/musicas", json=data, headers=admin_auth_headers)
    assert response.status_code == 400
    assert response.json["error"] == "Faltan datos requeridos"
    
def test_update_musca(test_client, admin_auth_headers):
    data = {
        "titulo": "V.A.N",
        "artista": "Bad Omens",
        "duracion": 4.35,
    }
    response = test_client.put("/api/musicas/1", json=data, headers=admin_auth_headers)
    assert response.status_code == 200
    assert response.json["titulo"]=="V.A.N"
    assert response.json["artista"]=="Bad Omens"
    assert response.json["duracion"]==4.35

def test_update_nonexistent_musica(test_client, admin_auth_headers):
    data = {
        "titulo": "Concrete Jungle",
        "artista": "Bad Omens",
        "duracion": 4.55 
    }
    response=test_client.put("/api/musicas/999", json=data, headers=admin_auth_headers)
    assert response.status_code == 404
    assert response.json["error"] == "Musica no encontrada"
    
def test_delete_musica(test_client, admin_auth_headers):
    response = test_client.delete("/api/musicas/1", headers=admin_auth_headers)
    assert response.status_code == 204
    
    response = test_client.delete("/api/musicas/1", headers=admin_auth_headers)
    assert response.json["error"]=="Musica no encontrada"
    
def test_delete_nonexisten_musica(test_client, admin_auth_headers):
    response = test_client.delete("/api/musicas/999", headers=admin_auth_headers)
    assert response.status_code == 404
    assert response.json["error"]=="Musica no encontrada"