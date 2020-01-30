from model import Base, Team


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine('sqlite:///database.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()



def add_Team( Name,score ):
	producta = Team(
		name=Name,
		score=score)
		
	session.add(producta)
	session.commit()