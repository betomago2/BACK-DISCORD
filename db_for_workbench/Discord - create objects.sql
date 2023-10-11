-- Crear la base de datos 'discord'
CREATE DATABASE IF NOT EXISTS discord;

-- Usar la base de datos 'discord'
USE discord;

-- Crear la tabla 'servers'
CREATE TABLE IF NOT EXISTS discord.servers (
    server_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    description TEXT,
    admin_user INT
);

-- Crear la tabla 'users'
CREATE TABLE IF NOT EXISTS discord.users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(255) NOT NULL,
    username VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    birthdate DATE,
    avatar VARCHAR(255)
);

-- Crear la tabla 'server_user'
CREATE TABLE IF NOT EXISTS discord.server_user (
    user_server_id INT AUTO_INCREMENT PRIMARY KEY,
    server_id INT,
    user_id INT,
    FOREIGN KEY (server_id) REFERENCES servers(server_id) ON DELETE CASCADE,
	FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE
);

-- Crear la tabla 'channels'
CREATE TABLE IF NOT EXISTS discord.channels (
    channel_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    description TEXT,
    server_id INT,
    FOREIGN KEY (server_id) REFERENCES servers(server_id) ON DELETE CASCADE
);

-- Crear la tabla 'messages'
CREATE TABLE IF NOT EXISTS discord.messages (
    message_id INT AUTO_INCREMENT PRIMARY KEY,
    message TEXT NOT NULL,
    date_time DATETIME DEFAULT NOW(),
    user_id INT,
    channel_id INT,
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE SET NULL,
    FOREIGN KEY (channel_id) REFERENCES channels(channel_id) ON DELETE CASCADE
);