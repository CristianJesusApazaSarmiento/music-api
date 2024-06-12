def user_lista(users):
    return[
        {
            "id": user.id,
            "username":user.username,
            "password_hash":user.password_hash,
            "roles":user.roles,
        }
        for user in users
    ]
    
def user_detalle(user):
    return {
        "id": user.id,
        "username":user.username,
        "password_hash":user.password_hash,
        "roles":user.roles,
    }