from model import *


engine = create_engine('sqlite:///model.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine, autoflush=False)
session = DBSession()

#Band

ds = Band(name='Destinys Child')

session.add(ds)

session.commit()

ml = Band(name='Mashrou Leila')

session.add(ml)

session.commit()

rhcp = Band(name='Red Hot Chili Peppers')

session.add(rhcp)

session.commit()

jd = Band(name='Jadal')

session.add(jd)

session.commit()

az = Band(name='Akher Zapheer')

session.add(az)

session.commit()

aus = Band(name='Autostrad')

session.add(aus)

session.add(aus)

session.commit()


#songs

session.commit()
smn = Song(name='Say My Name',duration="3.00", band_id = ds.id)

session.add(smn)

session.commit()

bbb = Song(name='Bills, Bills Bills',duration="2.85", band_id = ds.id)

session.add(bbb)

session.commit()

sy = Song(name='Shim el Yasmine',duration="3.50", band_id = ml.id)

session.add(sy)

session.commit()

aw = Song(name='Al Watan',duration="3.80", band_id = ml.id)

session.add(aw)

session.commit()

btw = Song(name='By the Way',duration="4.80", band_id = rhcp.id)

session.add(btw)

session.commit()

toc = Song(name='The Other Side',duration="3.20", band_id = rhcp.id)

session.add(toc)

session.commit()

ma = Song(name ='Malyoun', duration="4.58", band_id = jd.id)

session.add(ma)

session.commit()

at = Song(name='Al Tobah', duration='5.10', band_id = jd.id)

session.add(at)

session.commit()

alh = Song(name='Akherto Lahez Hazeen', duration="4.20", band_id = az.id)

session.add(alh)

session.commit()

fe = Song(name='Feekee', duration="3.55", band_id = az.id)

session.add(fe)

session.commit()     




