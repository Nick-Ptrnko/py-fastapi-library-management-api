'''
Create SQLAlchemy models for 'Author' and 'Book' in the `models.py` file.

4. The 'Author' model should have the following fields:
```
- id (integer, primary key)
- name (string, unique)
- bio (string)
- books (relationship with the 'Book' model, one-to-many)
```
5. The 'Book' model should have the following fields:
```
- id (integer, primary key)
- title (string)
- summary (string)
- publication_date (date)
- author_id (foreign key referencing 'Author' model)
'''

from database import Base
from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship

class Author(Base):
    __tablename__ = "authors"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), unique=True)
    bio = Column(String)
    books = relationship("Book", back_populates="author")

class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), unique=True)
    summary = Column(String)
    publication_date = Column(Date)
    author_id = Column(Integer, ForeignKey("authors.id"))
    author = relationship("Author", back_populates="books")
