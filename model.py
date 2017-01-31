from sqlalchemy import Column,Integer,String, DateTime, ForeignKey, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine, func

Base = declarative_base()


from passlib.apps import custom_app_context as pwd_context
class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    address = Column(String(255))
    email = Column(String(255), unique=True)
    password_hash = Column(String(255))
    playlists = relationship("Playlist", back_populates="user")
    def hash_password(self, password):
        self.password_hash = pwd_context.encrypt(password)
    def verify_password(self, password):
        return pwd_context.verify(password, self.password_hash)


class Band(Base):
    __tablename__ = 'band'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    songs = relationship("Song", back_populates='band')



class Song(Base):
    __tablename__ = 'song'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    duration = Column(String)
    band_id = Column(Integer, ForeignKey('band.id'))
    band = relationship("Band", back_populates="songs")
    playlists = relationship("SongPlaylistAssociation", back_populates =
    'song')


class Playlist(Base):
    __tablename__ = 'playlist'
    name = Column(String)
    id = Column(Integer, primary_key=True)
    songs = relationship("SongPlaylistAssociation", back_populates="playlist")                                                                                                                                                                                                         
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship("User", back_populates="playlists")





class SongPlaylistAssociation(Base):
    __tablename__ = 'songPlaylistAssociation'
    song_id = Column(Integer, ForeignKey('song.id'), primary_key=True)
    playlist_id = Column(Integer, ForeignKey('playlist.id'),
    primary_key=True)
    playlist = relationship("Playlist", back_populates='songs')
    song = relationship("Song", back_populates="playlists")



engine = create_engine('sqlite:///playlists.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine, autoflush=False)
session = DBSession()








   





   
    