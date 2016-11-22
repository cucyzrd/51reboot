-- MySQL dump 10.13  Distrib 5.5.52, for Win64 (x86)
--
-- Host: 127.0.0.1    Database: zrd
-- ------------------------------------------------------
-- Server version	5.5.52

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `asset`
--

DROP TABLE IF EXISTS `asset`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `asset` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `sn` varchar(125) NOT NULL COMMENT '资产标号',
  `hostname` varchar(64) DEFAULT NULL COMMENT '主机名',
  `os` varchar(64) DEFAULT NULL COMMENT '操作系统',
  `ip` varchar(256) DEFAULT NULL COMMENT 'ip地址',
  `machine_room_id` int(11) DEFAULT NULL COMMENT '机房ID',
  `vendor` varchar(256) DEFAULT NULL COMMENT '生产厂商',
  `model` varchar(64) DEFAULT NULL COMMENT '型号',
  `ram` int(11) DEFAULT NULL COMMENT '内存, 单位G',
  `cpu` int(11) DEFAULT NULL COMMENT 'cpu核数',
  `disk` int(11) DEFAULT NULL COMMENT '硬盘，单位G',
  `time_on_shelves` date DEFAULT NULL COMMENT '上架时间',
  `over_guaranteed_date` date DEFAULT NULL COMMENT '过保时间',
  `buiness` varchar(256) DEFAULT NULL COMMENT '业务',
  `admin` varchar(256) DEFAULT NULL COMMENT '使用者',
  `status` int(11) DEFAULT NULL COMMENT '0正在使用, 1 维护, 2 删除',
  PRIMARY KEY (`id`),
  UNIQUE KEY `sn` (`sn`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `asset`
--

LOCK TABLES `asset` WRITE;
/*!40000 ALTER TABLE `asset` DISABLE KEYS */;
INSERT INTO `asset` VALUES (1,'sn1','host11','centos 7.2 x64','192.168.1.21',2,'dell1','至强',123,53,234,'2016-11-24','2023-11-27','12','xxx',1),(2,'sn2','host2','bsd1','192.168.1.21',2,'hp','380',33,4,398,'2016-11-02','2016-11-23','2','test',0),(3,'sn3','host3','windows10','192.168.1.23',2,'ibm','test',211,31,256,'2016-11-16','2016-11-20','test','test',1);
/*!40000 ALTER TABLE `asset` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `log`
--

DROP TABLE IF EXISTS `log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `log` (
  `ip` varchar(15) DEFAULT NULL,
  `url` text,
  `status` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `log`
--

LOCK TABLES `log` WRITE;
/*!40000 ALTER TABLE `log` DISABLE KEYS */;
INSERT INTO `log` VALUES ('1.1.1.1','http://localhost/',200),('1.1.1.1','http://localhost/',400),('1.1.1.1','http://localhost/',400),('1.1.1.1','http://localhost/',400),('1.1.1.2','http://localhost/',400),('1.1.1.22','http://localhost/users/',200);
/*!40000 ALTER TABLE `log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `machine_room`
--

DROP TABLE IF EXISTS `machine_room`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `machine_room` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `room_name` varchar(64) DEFAULT NULL,
  `addr` varchar(128) DEFAULT NULL,
  `ip_ranges` text,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `machine_room`
--

LOCK TABLES `machine_room` WRITE;
/*!40000 ALTER TABLE `machine_room` DISABLE KEYS */;
INSERT INTO `machine_room` VALUES (1,'北京亦庄机房','北京市XXXXXX','192.168.1.1/25'),(3,'北京海淀机房','北京市XXXXXX','192.168.2.1/24'),(6,'海南xxx','xxx','xxx'),(7,'成都电信','成都','xxx'),(8,'wqqqqq','wqqqqqqq','333333333333333333333333');
/*!40000 ALTER TABLE `machine_room` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(32) DEFAULT NULL,
  `password` varchar(32) DEFAULT NULL,
  `age` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (1,'zrd','e10adc3949ba59abbe56e057f20f883e',23),(2,'kk','e10adc3949ba59abbe56e057f20f883e',29),(3,'kk12345','e10adc3949ba59abbe56e057f20f883e',29),(4,'test','e10adc3949ba59abbe56e057f20f883e',24);
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2016-11-22 17:41:20
