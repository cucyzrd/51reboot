-- --------------------------------------------------------
-- 主机:                           127.0.0.1
-- 服务器版本:                        5.5.52-log - MySQL Community Server (GPL)
-- 服务器操作系统:                      Win64
-- HeidiSQL 版本:                 
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;


-- 导出 zrd 的数据库结构
CREATE DATABASE IF NOT EXISTS `zrd` /*!40100 DEFAULT CHARACTER SET utf8 */;
USE `zrd`;

-- 导出  表 zrd.user 结构
DROP TABLE IF EXISTS `user`;
CREATE TABLE IF NOT EXISTS `user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(32) DEFAULT NULL,
  `age` int(11) DEFAULT NULL,
  `password` varchar(32) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `Index 2` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8;

-- 正在导出表  zrd.user 的数据：~4 rows (大约)
DELETE FROM `user`;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` (`id`, `name`, `age`, `password`) VALUES
	(1, 'zrd', 25, 'e10adc3949ba59abbe56e057f20f883e'),
	(2, 'tomcat', 35, 'md5(\'123456\')'),
	(3, 'fly', 55, 'e10adc3949ba59abbe56e057f20f883e'),
	(4, 'deg', 12, 'e10adc3949ba59abbe56e057f20f883e'),
	(5, 'sadfasdf22dfsdaf', 1, '96451e9723d1f3137eef7e14a5697d3e'),
	(6, 'DSDSSDSD', 22, '0aae6ee3625405a30177c365c33cef26'),
	(7, 'saddsa', 32, 'bd0ab3c7149c3cc9ea7cb95c39a8cf34'),
	(11, '3223', 22, '373a58b944a42d4b8ec784604c8c45a5');
/*!40000 ALTER TABLE `user` ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
