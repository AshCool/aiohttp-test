-- MySQL dump 10.13  Distrib 8.0.19, for Win64 (x86_64)
--
-- Host: localhost    Database: main_db
-- ------------------------------------------------------
-- Server version	8.0.19

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `user_data`
--

DROP TABLE IF EXISTS `user_data`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user_data` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `login` varchar(50) NOT NULL,
  `link` varchar(255) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `login` (`login`),
  CONSTRAINT `user_data_ibfk_1` FOREIGN KEY (`login`) REFERENCES `user_info` (`login`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_data`
--

LOCK TABLES `user_data` WRITE;
/*!40000 ALTER TABLE `user_data` DISABLE KEYS */;
INSERT INTO `user_data` VALUES (2,'local_god','https://docs.google.com/spreadsheets/d/1oUiA_QfbOmpm9FM3GtyYtoH0wamPDXWlGaKbZ_WgOGI/edit#gid=10538321'),(3,'local_god','https://docs.google.com/spreadsheets/d/1tQBOAIrUUo4NcL-mb66LZCMT6Vkft13JNMGDXVmAcmE/edit#gid=0'),(4,'mortal1','https://docs.google.com/spreadsheets/d/1oUiA_QfbOmpm9FM3GtyYtoH0wamPDXWlGaKbZ_WgOGI/edit#gid=10538321'),(5,'mortal2','https://docs.google.com/spreadsheets/d/1tQBOAIrUUo4NcL-mb66LZCMT6Vkft13JNMGDXVmAcmE/edit#gid=0'),(8,'mortal4','https://docs.google.com/spreadsheets/d/1Nbff-HkcYRO4nNqJY9SNyQtMxoso1GXws46-Q-615zs/edit#gid=0'),(9,'local_god','https://docs.google.com/spreadsheets/d/1Nbff-HkcYRO4nNqJY9SNyQtMxoso1GXws46-Q-615zs/edit#gid=0'),(10,'mortal4','https://docs.google.com/spreadsheets/d/1Nbff-HkcYRO4nNqJY9SNyQtMxoso1GXws46-Q-615zs/edit#gid=0'),(11,'mortal3','https://docs.google.com/spreadsheets/d/1Nbff-HkcYRO4nNqJY9SNyQtMxoso1GXws46-Q-615zs/edit#gid=0'),(12,'local_god','https://docs.google.com/spreadsheets/d/1Nbff-HkcYRO4nNqJY9SNyQtMxoso1GXws46-Q-615zs/edit#gid=0');
/*!40000 ALTER TABLE `user_data` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-04-09  0:45:21
