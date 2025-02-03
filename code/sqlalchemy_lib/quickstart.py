from sqlalchemy import Column, ForeignKey, Integer, String, create_engine
from sqlalchemy.orm import declarative_base, relationship, Session
from sqlalchemy import select

Base = declarative_base()

class User(Base):
    __tablename__ = "user_account"
    
    id = Column(Integer, primary_key=True)
    name = Column(String(30))
    fullname = Column(String)
    
    addresses = relationship(
        "Address", back_populates="user", cascade="all, delete-orphan"
    )
    
    def __repr__(self):
        return f"User(id={self.id!r}, name={self.name!r}, fullname={self.fullname!r})"

class Address(Base):
    __tablename__ = "address"
    
    id = Column(Integer, primary_key=True)
    email_address = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey("user_account.id"), nullable=False)
    user = relationship("User", back_populates="addresses")
    
    def __repr__(self):
        return f"Address(id={self.id!r}, email_address={self.email_address!r})"
    
engine = create_engine("sqlite://", echo=True, future=True)

Base.metadata.create_all(engine)

with Session(engine) as session:
    spongebob = User(
        name="spongebob",
        fullname="Spongebob Squarepants",
        addresses=[Address(email_address="spongebob@sqlalchemy.org")],
    )
    sandy = User(
        name="sandy",
        fullname="Sandy Cheeks",
        addresses=[
            Address(email_address="sandy@sqlalchemy.org"),
            Address(email_address="sandy@squirrelpower.org"),
        ],
    )
    patrick = User(name="patrick", fullname="Patrick Star")
    session.add_all([spongebob, sandy, patrick])
    session.commit()

session = Session(engine)

def simple_select():
    stmt = select(User).where(User.name.in_(["spongebob", "sandy"]))
    print("-"*50)
    for user in session.scalars(stmt):
        print(user)
    print("-"*50)

def select_with_join():
    stmt = (
        select(Address).join(Address.user).where(User.name=="sandy")\
            .where(Address.email_address == "sandy@sqlalchemy.org")
    )
    sandy_address = session.scalars(stmt).one()
    print(sandy_address)

def make_changes():
    print("-"*50)
    stmt = select(User).where(User.name == "patrick")
    patrick = session.scalars(stmt).one()
    patrick.addresses.append(
        Address(email_address="patrickstar@sqlalchemy.org")
    )

def some_deletes():
    print("-"*50)
    stmt = (
        select(Address).join(Address.user).where(User.name=="sandy")\
            .where(Address.email_address == "sandy@sqlalchemy.org")
    )
    sandy_address = session.scalars(stmt).one()
    sandy = session.get(User, 2)
    sandy.addresses.remove(sandy_address)
    session.flush()
    session.delete(patrick)
    session.commit()

simple_select()
select_with_join()
make_changes()
some_deletes()