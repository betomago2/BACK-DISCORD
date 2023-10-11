USE discord;

INSERT INTO discord.servers (name, description, admin_user) VALUES ('Literatura Fantástica', 'Descripción del servidor 1', 1);
INSERT INTO discord.servers (name, description, admin_user) VALUES ('Programación Web', 'Descripción del servidor 2', 2);

INSERT INTO discord.users (email, username, password, first_name, last_name, birthdate, avatar) VALUES ('ivana@gmail.com', 'ivana', 'ivana123', 'María Ivana', 'Maidana', '2000-01-01', 'avatar1.png');
INSERT INTO discord.users (email, username, password, first_name, last_name, birthdate, avatar) VALUES ('nicole@gmail.com', 'nicole', 'nicole123', 'Paula Nicole', 'Cardozo Gómez', '2000-02-02', 'avatar1.png');
INSERT INTO discord.users (email, username, password, first_name, last_name, birthdate, avatar) VALUES ('beto@gmail.com', 'beto', 'beto123', 'Alberto', 'Pallares', '2000-03-03', 'avatar2.png');
INSERT INTO discord.users (email, username, password, first_name, last_name, birthdate, avatar) VALUES ('pablo@gmail.com', 'pablo', 'pablo123', 'Pablo', 'Rodriguez', '2000-03-03', 'avatar2.png');

INSERT INTO discord.server_user (server_id, user_id) VALUES (1, 1);
INSERT INTO discord.server_user (server_id, user_id) VALUES (1, 2);
INSERT INTO discord.server_user (server_id, user_id) VALUES (1, 3);
INSERT INTO discord.server_user (server_id, user_id) VALUES (1, 4);

INSERT INTO discord.channels (name, description, server_id) VALUES ('Chat único', 'Para socializar', 1);
INSERT INTO discord.channels (name, description, server_id) VALUES ('Club de lectura', 'Descripción del canal 1', 1);
INSERT INTO discord.channels (name, description, server_id) VALUES ('Escritores Emergentes', 'Descripción del canal 2', 1);
INSERT INTO discord.channels (name, description, server_id) VALUES ('Recomendaciones', 'Descripción del canal 3', 1);
INSERT INTO discord.channels (name, description, server_id) VALUES ('Chat único', 'Para socializar', 2);
INSERT INTO discord.channels (name, description, server_id) VALUES ('Preguntas técnicas', 'Descripción del canal 1', 2);
INSERT INTO discord.channels (name, description, server_id) VALUES ('Proyectos compartidos', 'Descripción del canal 2', 2);
INSERT INTO discord.channels (name, description, server_id) VALUES ('Recursos útiles', 'Descripción del canal 3', 2);

INSERT INTO discord.messages (message, user_id, channel_id) VALUES ('¡Hola a todos! Soy nueva', 1, 1);
INSERT INTO discord.messages (message, user_id, channel_id) VALUES ('¡Hola, Ivana! ¡Bienvenida!', 2, 1);
INSERT INTO discord.messages (message, user_id, channel_id) VALUES ('¡Hola, Nicole! Gracias por la bienvenida.', 1, 1);
INSERT INTO discord.messages (message, user_id, channel_id) VALUES ('¡Saludos, Ivana y Nicole!', 3, 1);
INSERT INTO discord.messages (message, user_id, channel_id) VALUES ('¿Como están?', 4, 1);