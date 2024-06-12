from app.database import db

class Musica(db.Model):
    __tablename__ = "musicas"
    
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(50), nullable=False)
    artista = db.Column(db.String(50), nullable=False)
    duracion = db.Column(db.Float, nullable=False)
    
    def __init__(self, titulo, artista, duracion):
        self.titulo = titulo
        self.artista = artista
        self.duracion = duracion
        
    def save(self):
        db.session.add(self)
        db.session.commit()
        
    def update(self, titulo=None, artista=None, duracion=None):
        if titulo is not None:
            self.titulo = titulo
        if artista is not None:
            self.artista = artista
        if duracion is not None:
            self.duracion = duracion
        db.session.commit()
        
    def delete(self):
        db.session.delete(self)
        db.session.commit()
        
    @staticmethod
    def get_all():
        return Musica.query.all()
        
    @staticmethod
    def get_by_id(id):
        return Musica.query.get(id)