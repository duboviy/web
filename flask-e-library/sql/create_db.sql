CREATE TABLE books (
	id INTEGER NOT NULL,
	title VARCHAR(120),
	PRIMARY KEY (id)
);
CREATE TABLE authors (
	id INTEGER NOT NULL,
	name VARCHAR(120),
	PRIMARY KEY (id)
);
CREATE TABLE association (
	book_id INTEGER,
	author_id INTEGER,
	FOREIGN KEY(book_id) REFERENCES books (id),
	FOREIGN KEY(author_id) REFERENCES authors (id)
);
CREATE TABLE user (
	id INTEGER NOT NULL,
	username VARCHAR(80),
	email VARCHAR(120),
	PRIMARY KEY (id),
	UNIQUE (username),
	UNIQUE (email)
);
CREATE TABLE migrate_version (
	repository_id VARCHAR(250) NOT NULL,
	repository_path TEXT,
	version INTEGER,
	PRIMARY KEY (repository_id)
);
