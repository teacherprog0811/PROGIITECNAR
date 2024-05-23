-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Versión del servidor:         8.0.30 - MySQL Community Server - GPL
-- SO del servidor:              Win64
-- HeidiSQL Versión:             11.2.0.6213
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


-- Volcando estructura de base de datos para tecnarapp
CREATE DATABASE IF NOT EXISTS `tecnarapp` /*!40100 DEFAULT CHARACTER SET utf8mb3 */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `tecnarapp`;

-- Volcando estructura para tabla tecnarapp.usuarios
CREATE TABLE IF NOT EXISTS `usuarios` (
  `Id` int NOT NULL,
  `NombreCompleto` varchar(100) NOT NULL,
  `Username` varchar(100) NOT NULL,
  `Clave` varchar(100) NOT NULL,
  `Correo` varchar(100) NOT NULL,
  `Rol` varchar(25) DEFAULT NULL,
  PRIMARY KEY (`Id`),
  UNIQUE KEY `Username` (`Username`),
  UNIQUE KEY `Correo` (`Correo`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

-- Volcando datos para la tabla tecnarapp.usuarios: ~4 rows (aproximadamente)
/*!40000 ALTER TABLE `usuarios` DISABLE KEYS */;
INSERT INTO `usuarios` (`Id`, `NombreCompleto`, `Username`, `Clave`, `Correo`, `Rol`) VALUES
	(73456763, 'Clara Mejia', 'cmejia', '123', 'cmejia@gmail.com', 'Vendedor'),
	(91273799, 'Diana Lopez', 'dlopez', '12345678', 'dlopez@gmail.com', 'Vendedor'),
	(98765253, 'Dionisio Velez', 'dvelez', '123', 'dvelez@gmail.com', 'Vendedor'),
	(123456789, 'Ivan Narvaez', 'inarvaez', '123', 'ivan.narvaez@unitecnar.edu.co', 'Administrador');
/*!40000 ALTER TABLE `usuarios` ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
