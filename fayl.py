import sqlite3 as sql

boglash = sql.connect("database.db")

malumot = boglash.cursor()

malumot.execute("""
CREATE TABLE IF NOT EXISTS Students(
    ism TEXT,
    familiya TEXT,
    kurs INTEGER,
    yunalish TEXT
)
""")

malumot.execute("""
CREATE TABLE IF NOT EXISTS Programmist(
    ism TEXT,
    familiya TEXT,
    yunalish TEXT,
    staj INTEGER
)
""")

malumot.execute("""
CREATE TABLE IF NOT EXISTS Bekorchi(
    ism TEXT,
    familiya TEXT,
    qiziqishi TEXT,
    yoshi INTEGER
)
""")

malumot.execute("""
CREATE TABLE IF NOT EXISTS Uquvchi(
    ism TEXT,
    familiya TEXT,
    sinf INTEGER
    maktab INTEGER
)
""")

malumot.execute("""
CREATE TABLE IF NOT EXISTS Xaydovchi(
    ism TEXT,
    familiya TEXT,
    mashinasi TEXT,
    mashina_raqami INTEGER
)
""")