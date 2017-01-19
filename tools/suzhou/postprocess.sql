CREATE DATABASE  IF NOT EXISTS `postprocess` /*!40100 DEFAULT CHARACTER SET utf8 */;
USE `postprocess`;
-- MySQL dump 10.13  Distrib 5.5.53, for debian-linux-gnu (x86_64)
--
-- Host: 127.0.0.1    Database: postprocess
-- ------------------------------------------------------
-- Server version	5.5.53-0+deb8u1

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
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissi_permission_id_84c5c92e_fk_auth_permission_id` (`permission_id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_group_permissi_permission_id_84c5c92e_fk_auth_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permissi_content_type_id_2f476e4b_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=118 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can add permission',2,'add_permission'),(5,'Can change permission',2,'change_permission'),(6,'Can delete permission',2,'delete_permission'),(7,'Can add user',3,'add_user'),(8,'Can change user',3,'change_user'),(9,'Can delete user',3,'delete_user'),(10,'Can add group',4,'add_group'),(11,'Can change group',4,'change_group'),(12,'Can delete group',4,'delete_group'),(13,'Can add content type',5,'add_contenttype'),(14,'Can change content type',5,'change_contenttype'),(15,'Can delete content type',5,'delete_contenttype'),(16,'Can add session',6,'add_session'),(17,'Can change session',6,'change_session'),(18,'Can delete session',6,'delete_session'),(19,'Can add work type',7,'add_worktype'),(20,'Can change work type',7,'change_worktype'),(21,'Can delete work type',7,'delete_worktype'),(22,'Can add area',8,'add_area'),(23,'Can change area',8,'change_area'),(24,'Can delete area',8,'delete_area'),(25,'Can add enterprise',9,'add_enterprise'),(26,'Can change enterprise',9,'change_enterprise'),(27,'Can delete enterprise',9,'delete_enterprise'),(28,'Can add institution',10,'add_institution'),(29,'Can change institution',10,'change_institution'),(30,'Can delete institution',10,'delete_institution'),(31,'Can add bureau',11,'add_bureau'),(32,'Can change bureau',11,'change_bureau'),(33,'Can delete bureau',11,'delete_bureau'),(34,'Can add user',12,'add_user'),(35,'Can change user',12,'change_user'),(36,'Can delete user',12,'delete_user'),(37,'Can add economy',13,'add_economy'),(38,'Can change economy',13,'change_economy'),(39,'Can delete economy',13,'delete_economy'),(40,'Can add product',14,'add_product'),(41,'Can change product',14,'change_product'),(42,'Can delete product',14,'delete_product'),(43,'Can add manufacturer',15,'add_manufacturer'),(44,'Can change manufacturer',15,'change_manufacturer'),(45,'Can delete manufacturer',15,'delete_manufacturer'),(46,'Can add group',16,'add_group'),(47,'Can change group',16,'change_group'),(48,'Can delete group',16,'delete_group'),(49,'Can add category',17,'add_category'),(50,'Can change category',17,'change_category'),(51,'Can delete category',17,'delete_category'),(52,'Can add nosample reason',18,'add_nosamplereason'),(53,'Can change nosample reason',18,'change_nosamplereason'),(54,'Can delete nosample reason',18,'delete_nosamplereason'),(55,'Can add task',19,'add_task'),(56,'Can change task',19,'change_task'),(57,'Can delete task',19,'delete_task'),(58,'Can add assignment',20,'add_assignment'),(59,'Can change assignment',20,'change_assignment'),(60,'Can delete assignment',20,'delete_assignment'),(61,'Can add inspect',21,'add_inspect'),(62,'Can change inspect',21,'change_inspect'),(63,'Can delete inspect',21,'delete_inspect'),(64,'Can add review',22,'add_review'),(65,'Can change review',22,'change_review'),(66,'Can delete review',22,'delete_review'),(67,'Can add test',23,'add_test'),(68,'Can change test',23,'change_test'),(69,'Can delete test',23,'delete_test'),(70,'Can add express',24,'add_express'),(71,'Can change express',24,'change_express'),(72,'Can delete express',24,'delete_express'),(73,'Can add correction',25,'add_correction'),(74,'Can change correction',25,'change_correction'),(75,'Can delete correction',25,'delete_correction'),(76,'Can add product grade',26,'add_productgrade'),(77,'Can change product grade',26,'change_productgrade'),(78,'Can delete product grade',26,'delete_productgrade'),(79,'Can add agreement',27,'add_agreement'),(80,'Can change agreement',27,'change_agreement'),(81,'Can delete agreement',27,'delete_agreement'),(82,'Can add task status',28,'add_taskstatus'),(83,'Can change task status',28,'change_taskstatus'),(84,'Can delete task status',28,'delete_taskstatus'),(85,'Can add inspection type',29,'add_inspectiontype'),(86,'Can change inspection type',29,'change_inspectiontype'),(87,'Can delete inspection type',29,'delete_inspectiontype'),(88,'Can add inspection category',30,'add_inspectioncategory'),(89,'Can change inspection category',30,'change_inspectioncategory'),(90,'Can delete inspection category',30,'delete_inspectioncategory'),(91,'Can add objection notice',31,'add_objectionnotice'),(92,'Can change objection notice',31,'change_objectionnotice'),(93,'Can delete objection notice',31,'delete_objectionnotice'),(94,'Can add check sample',32,'add_checksample'),(95,'Can change check sample',32,'change_checksample'),(96,'Can delete check sample',32,'delete_checksample'),(97,'Can add no sample',33,'add_nosample'),(98,'Can change no sample',33,'change_nosample'),(99,'Can delete no sample',33,'delete_nosample'),(100,'Can add check notice',34,'add_checknotice'),(101,'Can change check notice',34,'change_checknotice'),(102,'Can delete check notice',34,'delete_checknotice'),(103,'Can add reform notice',35,'add_reformnotice'),(104,'Can change reform notice',35,'change_reformnotice'),(105,'Can delete reform notice',35,'delete_reformnotice'),(106,'Can add check proxy',36,'add_checkproxy'),(107,'Can change check proxy',36,'change_checkproxy'),(108,'Can delete check proxy',36,'delete_checkproxy'),(109,'Can add postpone notice',37,'add_postponenotice'),(110,'Can change postpone notice',37,'change_postponenotice'),(111,'Can delete postpone notice',37,'delete_postponenotice'),(112,'Can add rejects',38,'add_rejects'),(113,'Can change rejects',38,'change_rejects'),(114,'Can delete rejects',38,'delete_rejects'),(115,'Can add objection accept',39,'add_objectionaccept'),(116,'Can change objection accept',39,'change_objectionaccept'),(117,'Can delete objection accept',39,'delete_objectionaccept');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'admin','2016-12-04 07:41:32',1,'admin','','','',1,1,'2016-11-30 09:01:23');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_perm_permission_id_1fbb5f2c_fk_auth_permission_id` (`permission_id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `auth_user_user_perm_permission_id_1fbb5f2c_fk_auth_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `base_area`
--

DROP TABLE IF EXISTS `base_area`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `base_area` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `level` int(11) NOT NULL,
  `parent_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `base_area_parent_id_54c457f4_fk_base_area_id` (`parent_id`),
  CONSTRAINT `base_area_parent_id_54c457f4_fk_base_area_id` FOREIGN KEY (`parent_id`) REFERENCES `base_area` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `base_area`
--

LOCK TABLES `base_area` WRITE;
/*!40000 ALTER TABLE `base_area` DISABLE KEYS */;
INSERT INTO `base_area` VALUES (1,'中国',1,NULL),(2,'河南',2,1);
/*!40000 ALTER TABLE `base_area` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `base_bureau`
--

DROP TABLE IF EXISTS `base_bureau`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `base_bureau` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `address` varchar(255) NOT NULL,
  `postcode` int(11) NOT NULL,
  `contact` varchar(255) NOT NULL,
  `telephone` varchar(255) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `group_id` (`group_id`),
  CONSTRAINT `base_bureau_group_id_514a249e_fk_base_group_id` FOREIGN KEY (`group_id`) REFERENCES `base_group` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `base_bureau`
--

LOCK TABLES `base_bureau` WRITE;
/*!40000 ALTER TABLE `base_bureau` DISABLE KEYS */;
INSERT INTO `base_bureau` VALUES (2,'小明','test',1001,'小明','10011',4),(3,'小白','test',1001,'小白','10011',5),(4,'小红','test',1001,'小红','10011',6);
/*!40000 ALTER TABLE `base_bureau` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `base_category`
--

DROP TABLE IF EXISTS `base_category`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `base_category` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `level` int(11) NOT NULL,
  `parent_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `base_category_parent_id_42ca2e66_fk_base_category_id` (`parent_id`),
  CONSTRAINT `base_category_parent_id_42ca2e66_fk_base_category_id` FOREIGN KEY (`parent_id`) REFERENCES `base_category` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `base_category`
--

LOCK TABLES `base_category` WRITE;
/*!40000 ALTER TABLE `base_category` DISABLE KEYS */;
INSERT INTO `base_category` VALUES (1,'产品类别',1,NULL),(2,'产品类别A',2,1);
/*!40000 ALTER TABLE `base_category` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `base_economy`
--

DROP TABLE IF EXISTS `base_economy`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `base_economy` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `base_economy`
--

LOCK TABLES `base_economy` WRITE;
/*!40000 ALTER TABLE `base_economy` DISABLE KEYS */;
INSERT INTO `base_economy` VALUES (1,'餐饮');
/*!40000 ALTER TABLE `base_economy` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `base_enterprise`
--

DROP TABLE IF EXISTS `base_enterprise`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `base_enterprise` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `address` varchar(255) NOT NULL,
  `representative` varchar(255) NOT NULL,
  `postcode` int(11) NOT NULL,
  `contact` varchar(255) NOT NULL,
  `telephone` varchar(255) NOT NULL,
  `industry` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `base_enterprise`
--

LOCK TABLES `base_enterprise` WRITE;
/*!40000 ALTER TABLE `base_enterprise` DISABLE KEYS */;
INSERT INTO `base_enterprise` VALUES (1,'憨憨包','银河之汉堡王宫','1111',1001,'admin','10011','食品');
/*!40000 ALTER TABLE `base_enterprise` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `base_group`
--

DROP TABLE IF EXISTS `base_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `base_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `level` bigint(20) NOT NULL,
  `parent_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `base_group_parent_id_0d032969_fk_base_group_id` (`parent_id`),
  CONSTRAINT `base_group_parent_id_0d032969_fk_base_group_id` FOREIGN KEY (`parent_id`) REFERENCES `base_group` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `base_group`
--

LOCK TABLES `base_group` WRITE;
/*!40000 ALTER TABLE `base_group` DISABLE KEYS */;
INSERT INTO `base_group` VALUES (1,'质监局',1,NULL),(2,'区县质监局',1,NULL),(3,'检测机构',2,3),(4,'市质监局B',2,1),(5,'市质监局C',2,1),(6,'市质监局A',2,1),(7,'区县质监局B',2,2),(8,'区县质监局C',2,2),(9,'区县质监局A',2,2),(10,'检测机构B',2,2),(11,'检测机构C',2,2),(12,'检测机构A',2,2),(13,'吴江质监',2,15),(14,'相城质监',2,15),(15,'苏州质量技术监督局',2,1);
/*!40000 ALTER TABLE `base_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `base_institution`
--

DROP TABLE IF EXISTS `base_institution`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `base_institution` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `address` varchar(255) NOT NULL,
  `postcode` int(11) NOT NULL,
  `contact` varchar(255) NOT NULL,
  `telephone` varchar(255) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `group_id` (`group_id`),
  CONSTRAINT `base_institution_group_id_4fcd1ed3_fk_base_group_id` FOREIGN KEY (`group_id`) REFERENCES `base_group` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `base_institution`
--

LOCK TABLES `base_institution` WRITE;
/*!40000 ALTER TABLE `base_institution` DISABLE KEYS */;
INSERT INTO `base_institution` VALUES (2,'白白','test',1001,'白白','10011',7),(3,'红红','test',1001,'红红','10011',8),(4,'明明','test',1001,'明明','10011',9);
/*!40000 ALTER TABLE `base_institution` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `base_manufacturer`
--

DROP TABLE IF EXISTS `base_manufacturer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `base_manufacturer` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `authority` varchar(255) NOT NULL,
  `address` varchar(255) NOT NULL,
  `postcode` int(11) NOT NULL,
  `representative` varchar(255) NOT NULL,
  `contact` varchar(255) NOT NULL,
  `telephone` varchar(255) NOT NULL,
  `license` varchar(15) NOT NULL,
  `code` int(11) NOT NULL,
  `scale` varchar(2) NOT NULL,
  `authentication` tinyint(1) NOT NULL,
  `certificate` varchar(255) NOT NULL,
  `economy_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `base_manufacturer_economy_id_55ddebdd_fk_base_economy_id` (`economy_id`),
  CONSTRAINT `base_manufacturer_economy_id_55ddebdd_fk_base_economy_id` FOREIGN KEY (`economy_id`) REFERENCES `base_economy` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `base_manufacturer`
--

LOCK TABLES `base_manufacturer` WRITE;
/*!40000 ALTER TABLE `base_manufacturer` DISABLE KEYS */;
INSERT INTO `base_manufacturer` VALUES (1,'制造商A','河南','address',1001,'法人代表A','联系人','10011','营业执照',1111,'10',1,'2222',1);
/*!40000 ALTER TABLE `base_manufacturer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `base_nosamplereason`
--

DROP TABLE IF EXISTS `base_nosamplereason`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `base_nosamplereason` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `reason` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `base_nosamplereason`
--

LOCK TABLES `base_nosamplereason` WRITE;
/*!40000 ALTER TABLE `base_nosamplereason` DISABLE KEYS */;
/*!40000 ALTER TABLE `base_nosamplereason` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `base_product`
--

DROP TABLE IF EXISTS `base_product`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `base_product` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `specifications` varchar(255) NOT NULL,
  `date` date NOT NULL,
  `category_id` int(11) NOT NULL,
  `origin_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `base_product_category_id_2193a903_fk_base_category_id` (`category_id`),
  KEY `base_product_origin_id_f01748d5_fk_base_area_id` (`origin_id`),
  CONSTRAINT `base_product_category_id_2193a903_fk_base_category_id` FOREIGN KEY (`category_id`) REFERENCES `base_category` (`id`),
  CONSTRAINT `base_product_origin_id_f01748d5_fk_base_area_id` FOREIGN KEY (`origin_id`) REFERENCES `base_area` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `base_product`
--

LOCK TABLES `base_product` WRITE;
/*!40000 ALTER TABLE `base_product` DISABLE KEYS */;
INSERT INTO `base_product` VALUES (1,'汉堡王','超超超级大','2016-11-30',2,2);
/*!40000 ALTER TABLE `base_product` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `base_user`
--

DROP TABLE IF EXISTS `base_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `base_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `last_login` datetime DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `base_user_group_id_e6559cc5_fk_base_group_id` (`group_id`),
  CONSTRAINT `base_user_group_id_e6559cc5_fk_base_group_id` FOREIGN KEY (`group_id`) REFERENCES `base_group` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `base_user`
--

LOCK TABLES `base_user` WRITE;
/*!40000 ALTER TABLE `base_user` DISABLE KEYS */;
INSERT INTO `base_user` VALUES (1,'admin','admin',NULL,1,1,'2016-11-30 17:23:32',1),(3,'bureau','bureau',NULL,1,1,'2016-11-30 17:23:32',2),(4,'institution','institution','2016-12-04 08:07:03',1,1,'2016-11-30 17:23:32',3),(5,'sz_wjzj_1','sz_wjzj_1','2016-11-30 12:37:12',1,1,'2016-11-30 12:37:16',13),(6,'sz_xczj_1','sz_xczj_1','2016-11-30 12:37:59',1,1,'2016-11-30 12:38:00',14),(7,'szzj_1','szzj_1','2016-11-30 12:40:55',1,1,'2016-11-30 12:40:56',15),(8,'szzj_2','szzj_2','2016-11-30 12:41:40',1,1,'2016-11-30 12:41:42',15);
/*!40000 ALTER TABLE `base_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `base_worktype`
--

DROP TABLE IF EXISTS `base_worktype`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `base_worktype` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `base_worktype`
--

LOCK TABLES `base_worktype` WRITE;
/*!40000 ALTER TABLE `base_worktype` DISABLE KEYS */;
/*!40000 ALTER TABLE `base_worktype` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin__content_type_id_c4bce8eb_fk_django_content_type_id` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `django_admin__content_type_id_c4bce8eb_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=37 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2016-11-30 12:37:33','13','吴江质监',1,'Added.',16,1),(2,'2016-11-30 12:37:35','5','sj_wjzj_1',1,'Added.',12,1),(3,'2016-11-30 12:40:38','14','相城质监',1,'Added.',16,1),(4,'2016-11-30 12:40:39','6','zs_xczj_1',1,'Added.',12,1),(5,'2016-11-30 12:41:30','15','苏州质量技术监督局',1,'Added.',16,1),(6,'2016-11-30 12:41:32','7','szzj_1',1,'Added.',12,1),(7,'2016-11-30 12:41:47','8','szzj_2',1,'Added.',12,1),(8,'2016-11-30 12:41:55','7','szzj_1',2,'Changed is_superuser and is_active.',12,1),(9,'2016-11-30 12:42:00','6','zs_xczj_1',2,'Changed is_superuser and is_active.',12,1),(10,'2016-12-01 04:32:54','1','质监局',2,'Changed name.',16,1),(11,'2016-12-01 04:32:56','15','苏州质量技术监督局',2,'No fields changed.',16,1),(12,'2016-12-04 08:01:05','3','检测机构',2,'No fields changed.',16,1),(13,'2016-12-04 08:01:07','4','institution',2,'No fields changed.',12,1),(14,'2016-12-04 08:01:56','4','institution',2,'No fields changed.',12,1),(15,'2016-12-04 08:07:05','4','institution',2,'Changed last_login.',12,1),(16,'2016-12-04 08:17:56','3','检测机构',2,'Changed level and parent.',16,1),(17,'2016-12-04 08:17:59','4','institution',2,'No fields changed.',12,1),(18,'2016-12-04 13:34:28','14','相城质监',2,'Changed parent.',16,1),(19,'2016-12-04 13:34:29','6','zs_xczj_1',2,'No fields changed.',12,1),(20,'2016-12-04 13:34:39','13','吴江质监',2,'Changed parent.',16,1),(21,'2016-12-04 13:34:41','5','sj_wjzj_1',2,'No fields changed.',12,1),(22,'2016-12-04 13:35:52','6','sz_xczj_1',2,'Changed username and password.',12,1),(23,'2016-12-04 13:36:04','5','sz_wjzj_1',2,'Changed username and password.',12,1),(24,'2016-12-05 01:14:29','9','不能整改任务',3,'',28,1),(25,'2016-12-05 01:14:38','2','已完成整改任务',2,'Changed code.',28,1),(26,'2016-12-05 02:39:08','2','已完成整改任务',2,'Changed code.',28,1),(27,'2016-12-05 02:39:16','6','正在整改任务',2,'Changed code.',28,1),(28,'2016-12-05 02:39:32','8','待整改任务',2,'Changed code.',28,1),(29,'2016-12-05 02:39:56','21','能否整改',1,'Added.',28,1),(30,'2016-12-05 02:45:00','21','整改任务',2,'Changed name.',28,1),(31,'2016-12-05 03:40:21','1','28932751276871',2,'Changed status.',19,1),(32,'2016-12-05 03:40:23','1','28932751276871',1,'Added.',25,1),(33,'2016-12-05 03:43:41','1','28932751276871',2,'No fields changed.',25,1),(34,'2016-12-05 03:58:44','1','28932751276871',2,'Changed status.',19,1),(35,'2016-12-05 03:58:46','1','28932751276871',2,'No fields changed.',25,1),(36,'2016-12-05 05:41:11','22','后处理任务',1,'Added.',28,1);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=40 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(4,'auth','group'),(2,'auth','permission'),(3,'auth','user'),(8,'base','area'),(11,'base','bureau'),(17,'base','category'),(13,'base','economy'),(9,'base','enterprise'),(16,'base','group'),(10,'base','institution'),(15,'base','manufacturer'),(18,'base','nosamplereason'),(14,'base','product'),(12,'base','user'),(7,'base','worktype'),(5,'contenttypes','contenttype'),(34,'paper','checknotice'),(36,'paper','checkproxy'),(32,'paper','checksample'),(33,'paper','nosample'),(39,'paper','objectionaccept'),(31,'paper','objectionnotice'),(37,'paper','postponenotice'),(35,'paper','reformnotice'),(38,'paper','rejects'),(27,'postprocess','agreement'),(20,'postprocess','assignment'),(25,'postprocess','correction'),(24,'postprocess','express'),(21,'postprocess','inspect'),(30,'postprocess','inspectioncategory'),(29,'postprocess','inspectiontype'),(26,'postprocess','productgrade'),(22,'postprocess','review'),(19,'postprocess','task'),(28,'postprocess','taskstatus'),(23,'postprocess','test'),(6,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2016-11-30 08:59:47'),(2,'auth','0001_initial','2016-11-30 08:59:49'),(3,'admin','0001_initial','2016-11-30 08:59:50'),(4,'admin','0002_logentry_remove_auto_add','2016-11-30 08:59:50'),(5,'contenttypes','0002_remove_content_type_name','2016-11-30 08:59:50'),(6,'auth','0002_alter_permission_name_max_length','2016-11-30 08:59:50'),(7,'auth','0003_alter_user_email_max_length','2016-11-30 08:59:51'),(8,'auth','0004_alter_user_username_opts','2016-11-30 08:59:51'),(9,'auth','0005_alter_user_last_login_null','2016-11-30 08:59:51'),(10,'auth','0006_require_contenttypes_0002','2016-11-30 08:59:51'),(11,'auth','0007_alter_validators_add_error_messages','2016-11-30 08:59:51'),(12,'auth','0008_alter_user_username_max_length','2016-11-30 08:59:51'),(13,'base','0001_initial','2016-11-30 08:59:54'),(14,'postprocess','0001_initial','2016-11-30 09:00:02'),(15,'paper','0001_initial','2016-11-30 09:00:07'),(16,'sessions','0001_initial','2016-11-30 09:00:07'),(17,'postprocess','0002_auto_20161205_1201','2016-12-05 04:01:16');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_de54fa62` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('1dug6wwsinoqq7r4enirpl208pal6cds','YjQwYTQ2ZTA0MGYyNTEzY2RkMThlODg0MmQ3ZDk5MjkxYTE3Zjc0MDp7Il9hdXRoX3VzZXJfaGFzaCI6IjEwNTE0NTkzNGU1YjA2MTA1NWY1MjBlNzYxYzEwMjExZDkyNDIxOGMiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJhZG1pbi51dGlscy5teWJhY2tlbmQuTXlCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6IjEifQ==','2016-12-15 04:28:29'),('6gne134iu1u8lh4g27pobh7kc0d02z3h','YjQwYTQ2ZTA0MGYyNTEzY2RkMThlODg0MmQ3ZDk5MjkxYTE3Zjc0MDp7Il9hdXRoX3VzZXJfaGFzaCI6IjEwNTE0NTkzNGU1YjA2MTA1NWY1MjBlNzYxYzEwMjExZDkyNDIxOGMiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJhZG1pbi51dGlscy5teWJhY2tlbmQuTXlCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6IjEifQ==','2016-12-15 03:24:28'),('6zonde7fsqm3lwvi6l6ms8fzsuag3j78','YjQwYTQ2ZTA0MGYyNTEzY2RkMThlODg0MmQ3ZDk5MjkxYTE3Zjc0MDp7Il9hdXRoX3VzZXJfaGFzaCI6IjEwNTE0NTkzNGU1YjA2MTA1NWY1MjBlNzYxYzEwMjExZDkyNDIxOGMiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJhZG1pbi51dGlscy5teWJhY2tlbmQuTXlCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6IjEifQ==','2016-12-14 13:27:58'),('8tjxvqgh87sahgky842ejusk8qzqlhkk','YjQwYTQ2ZTA0MGYyNTEzY2RkMThlODg0MmQ3ZDk5MjkxYTE3Zjc0MDp7Il9hdXRoX3VzZXJfaGFzaCI6IjEwNTE0NTkzNGU1YjA2MTA1NWY1MjBlNzYxYzEwMjExZDkyNDIxOGMiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJhZG1pbi51dGlscy5teWJhY2tlbmQuTXlCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6IjEifQ==','2016-12-14 09:07:54'),('des6wx48pualkesmvgtfru59pf1rukon','YjQwYTQ2ZTA0MGYyNTEzY2RkMThlODg0MmQ3ZDk5MjkxYTE3Zjc0MDp7Il9hdXRoX3VzZXJfaGFzaCI6IjEwNTE0NTkzNGU1YjA2MTA1NWY1MjBlNzYxYzEwMjExZDkyNDIxOGMiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJhZG1pbi51dGlscy5teWJhY2tlbmQuTXlCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6IjEifQ==','2016-12-18 07:41:32'),('j28vlazghh716cf0x61pehmbnl6kz8np','YjQwYTQ2ZTA0MGYyNTEzY2RkMThlODg0MmQ3ZDk5MjkxYTE3Zjc0MDp7Il9hdXRoX3VzZXJfaGFzaCI6IjEwNTE0NTkzNGU1YjA2MTA1NWY1MjBlNzYxYzEwMjExZDkyNDIxOGMiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJhZG1pbi51dGlscy5teWJhY2tlbmQuTXlCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6IjEifQ==','2016-12-18 07:15:58'),('mvnsdtfn65rbu9qs06chmafz1djqklih','YjQwYTQ2ZTA0MGYyNTEzY2RkMThlODg0MmQ3ZDk5MjkxYTE3Zjc0MDp7Il9hdXRoX3VzZXJfaGFzaCI6IjEwNTE0NTkzNGU1YjA2MTA1NWY1MjBlNzYxYzEwMjExZDkyNDIxOGMiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJhZG1pbi51dGlscy5teWJhY2tlbmQuTXlCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6IjEifQ==','2016-12-14 12:36:33'),('sqnt6efvj4lasu4vkkctu1yzdn0c8l2g','YjQwYTQ2ZTA0MGYyNTEzY2RkMThlODg0MmQ3ZDk5MjkxYTE3Zjc0MDp7Il9hdXRoX3VzZXJfaGFzaCI6IjEwNTE0NTkzNGU1YjA2MTA1NWY1MjBlNzYxYzEwMjExZDkyNDIxOGMiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJhZG1pbi51dGlscy5teWJhY2tlbmQuTXlCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6IjEifQ==','2016-12-18 07:26:55'),('st10cqb7ri6rr0p3acyo756r7xu8tzx4','YjQwYTQ2ZTA0MGYyNTEzY2RkMThlODg0MmQ3ZDk5MjkxYTE3Zjc0MDp7Il9hdXRoX3VzZXJfaGFzaCI6IjEwNTE0NTkzNGU1YjA2MTA1NWY1MjBlNzYxYzEwMjExZDkyNDIxOGMiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJhZG1pbi51dGlscy5teWJhY2tlbmQuTXlCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6IjEifQ==','2016-12-16 13:49:38');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `paper_checknotice`
--

DROP TABLE IF EXISTS `paper_checknotice`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `paper_checknotice` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `number` varchar(255) NOT NULL,
  `sample_people` varchar(255) NOT NULL,
  `sample_date` date NOT NULL,
  `issue_time` date NOT NULL,
  `effective_date` date NOT NULL,
  `group_id` int(11) NOT NULL,
  `task_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `paper_checknotice_group_id_c6defe1b_fk_base_group_id` (`group_id`),
  KEY `paper_checknotice_task_id_191fccaf_fk_postprocess_task_id` (`task_id`),
  CONSTRAINT `paper_checknotice_group_id_c6defe1b_fk_base_group_id` FOREIGN KEY (`group_id`) REFERENCES `base_group` (`id`),
  CONSTRAINT `paper_checknotice_task_id_191fccaf_fk_postprocess_task_id` FOREIGN KEY (`task_id`) REFERENCES `postprocess_task` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `paper_checknotice`
--

LOCK TABLES `paper_checknotice` WRITE;
/*!40000 ALTER TABLE `paper_checknotice` DISABLE KEYS */;
/*!40000 ALTER TABLE `paper_checknotice` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `paper_checkproxy`
--

DROP TABLE IF EXISTS `paper_checkproxy`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `paper_checkproxy` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `number` varchar(255) NOT NULL,
  `operator` varchar(255) NOT NULL,
  `check_number` int(11) NOT NULL,
  `issue_time` date NOT NULL,
  `effective_date` date NOT NULL,
  `deadline` date NOT NULL,
  `pick_task_people` varchar(255) NOT NULL,
  `category_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  `worktype_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `paper_checkproxy_category_id_dcd3cc66_fk_base_category_id` (`category_id`),
  KEY `paper_checkproxy_group_id_fa422918_fk_base_group_id` (`group_id`),
  KEY `paper_checkproxy_worktype_id_3e7e41eb_fk_base_worktype_id` (`worktype_id`),
  CONSTRAINT `paper_checkproxy_category_id_dcd3cc66_fk_base_category_id` FOREIGN KEY (`category_id`) REFERENCES `base_category` (`id`),
  CONSTRAINT `paper_checkproxy_group_id_fa422918_fk_base_group_id` FOREIGN KEY (`group_id`) REFERENCES `base_group` (`id`),
  CONSTRAINT `paper_checkproxy_worktype_id_3e7e41eb_fk_base_worktype_id` FOREIGN KEY (`worktype_id`) REFERENCES `base_worktype` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `paper_checkproxy`
--

LOCK TABLES `paper_checkproxy` WRITE;
/*!40000 ALTER TABLE `paper_checkproxy` DISABLE KEYS */;
/*!40000 ALTER TABLE `paper_checkproxy` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `paper_checksample`
--

DROP TABLE IF EXISTS `paper_checksample`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `paper_checksample` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `number` varchar(255) NOT NULL,
  `sample_count` int(11) NOT NULL,
  `store_count` int(11) NOT NULL,
  `storage_at` varchar(255) NOT NULL,
  `sample_batch` int(11) NOT NULL,
  `sample_date` date NOT NULL,
  `sample_at` varchar(255) NOT NULL,
  `sample_status` varchar(255) NOT NULL,
  `technical_docu` varchar(255) NOT NULL,
  `iseligible` tinyint(1) NOT NULL,
  `saleroom` decimal(19,2) NOT NULL,
  `group_id` int(11) NOT NULL,
  `task_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `paper_checksample_group_id_6250ee33_fk_base_group_id` (`group_id`),
  KEY `paper_checksample_task_id_bfa73344_fk_postprocess_task_id` (`task_id`),
  CONSTRAINT `paper_checksample_group_id_6250ee33_fk_base_group_id` FOREIGN KEY (`group_id`) REFERENCES `base_group` (`id`),
  CONSTRAINT `paper_checksample_task_id_bfa73344_fk_postprocess_task_id` FOREIGN KEY (`task_id`) REFERENCES `postprocess_task` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `paper_checksample`
--

LOCK TABLES `paper_checksample` WRITE;
/*!40000 ALTER TABLE `paper_checksample` DISABLE KEYS */;
/*!40000 ALTER TABLE `paper_checksample` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `paper_nosample`
--

DROP TABLE IF EXISTS `paper_nosample`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `paper_nosample` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `number` varchar(255) NOT NULL,
  `storage_at` varchar(255) NOT NULL,
  `sample_date` date NOT NULL,
  `reason_other` varchar(255) NOT NULL,
  `reason_id` int(11) NOT NULL,
  `task_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `paper_nosample_reason_id_eb5775ae_fk_base_nosamplereason_id` (`reason_id`),
  KEY `paper_nosample_task_id_5469c514_fk_postprocess_task_id` (`task_id`),
  CONSTRAINT `paper_nosample_reason_id_eb5775ae_fk_base_nosamplereason_id` FOREIGN KEY (`reason_id`) REFERENCES `base_nosamplereason` (`id`),
  CONSTRAINT `paper_nosample_task_id_5469c514_fk_postprocess_task_id` FOREIGN KEY (`task_id`) REFERENCES `postprocess_task` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `paper_nosample`
--

LOCK TABLES `paper_nosample` WRITE;
/*!40000 ALTER TABLE `paper_nosample` DISABLE KEYS */;
/*!40000 ALTER TABLE `paper_nosample` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `paper_objectionaccept`
--

DROP TABLE IF EXISTS `paper_objectionaccept`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `paper_objectionaccept` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `number` varchar(255) NOT NULL,
  `accept` tinyint(1) NOT NULL,
  `accept_policy` varchar(255) NOT NULL,
  `objection_reason` varchar(255) NOT NULL,
  `contact_people` varchar(255) NOT NULL,
  `contact_address` varchar(255) NOT NULL,
  `contact_number` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  `task_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `paper_objectionaccept_group_id_07570019_fk_base_group_id` (`group_id`),
  KEY `paper_objectionaccept_task_id_790914b6_fk_postprocess_task_id` (`task_id`),
  CONSTRAINT `paper_objectionaccept_group_id_07570019_fk_base_group_id` FOREIGN KEY (`group_id`) REFERENCES `base_group` (`id`),
  CONSTRAINT `paper_objectionaccept_task_id_790914b6_fk_postprocess_task_id` FOREIGN KEY (`task_id`) REFERENCES `postprocess_task` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `paper_objectionaccept`
--

LOCK TABLES `paper_objectionaccept` WRITE;
/*!40000 ALTER TABLE `paper_objectionaccept` DISABLE KEYS */;
/*!40000 ALTER TABLE `paper_objectionaccept` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `paper_objectionnotice`
--

DROP TABLE IF EXISTS `paper_objectionnotice`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `paper_objectionnotice` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `number` varchar(255) NOT NULL,
  `treatment` tinyint(1) NOT NULL,
  `suggestion` varchar(255) NOT NULL,
  `suggestion_reason` longtext NOT NULL,
  `group_id` int(11) NOT NULL,
  `task_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `paper_objectionnotice_group_id_49fe40fe_fk_base_group_id` (`group_id`),
  KEY `paper_objectionnotice_task_id_6527a92c_fk_postprocess_task_id` (`task_id`),
  CONSTRAINT `paper_objectionnotice_group_id_49fe40fe_fk_base_group_id` FOREIGN KEY (`group_id`) REFERENCES `base_group` (`id`),
  CONSTRAINT `paper_objectionnotice_task_id_6527a92c_fk_postprocess_task_id` FOREIGN KEY (`task_id`) REFERENCES `postprocess_task` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `paper_objectionnotice`
--

LOCK TABLES `paper_objectionnotice` WRITE;
/*!40000 ALTER TABLE `paper_objectionnotice` DISABLE KEYS */;
/*!40000 ALTER TABLE `paper_objectionnotice` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `paper_postponenotice`
--

DROP TABLE IF EXISTS `paper_postponenotice`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `paper_postponenotice` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `number` varchar(255) NOT NULL,
  `apply_date` date NOT NULL,
  `agree_or_not` tinyint(1) NOT NULL,
  `task_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `paper_postponenotice_task_id_e2a5336a_fk_postprocess_task_id` (`task_id`),
  CONSTRAINT `paper_postponenotice_task_id_e2a5336a_fk_postprocess_task_id` FOREIGN KEY (`task_id`) REFERENCES `postprocess_task` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `paper_postponenotice`
--

LOCK TABLES `paper_postponenotice` WRITE;
/*!40000 ALTER TABLE `paper_postponenotice` DISABLE KEYS */;
/*!40000 ALTER TABLE `paper_postponenotice` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `paper_reformnotice`
--

DROP TABLE IF EXISTS `paper_reformnotice`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `paper_reformnotice` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `number` varchar(255) NOT NULL,
  `complete_at` datetime NOT NULL,
  `contact_address` varchar(255) NOT NULL,
  `contact_number` int(11) NOT NULL,
  `task_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `paper_reformnotice_task_id_c964e6a3_fk_postprocess_task_id` (`task_id`),
  CONSTRAINT `paper_reformnotice_task_id_c964e6a3_fk_postprocess_task_id` FOREIGN KEY (`task_id`) REFERENCES `postprocess_task` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `paper_reformnotice`
--

LOCK TABLES `paper_reformnotice` WRITE;
/*!40000 ALTER TABLE `paper_reformnotice` DISABLE KEYS */;
/*!40000 ALTER TABLE `paper_reformnotice` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `paper_rejects`
--

DROP TABLE IF EXISTS `paper_rejects`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `paper_rejects` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `sample_date` date NOT NULL,
  `fact_describe` longtext NOT NULL,
  `task_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `paper_rejects_task_id_58c4b584_fk_postprocess_task_id` (`task_id`),
  CONSTRAINT `paper_rejects_task_id_58c4b584_fk_postprocess_task_id` FOREIGN KEY (`task_id`) REFERENCES `postprocess_task` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `paper_rejects`
--

LOCK TABLES `paper_rejects` WRITE;
/*!40000 ALTER TABLE `paper_rejects` DISABLE KEYS */;
/*!40000 ALTER TABLE `paper_rejects` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `postprocess_agreement`
--

DROP TABLE IF EXISTS `postprocess_agreement`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `postprocess_agreement` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `number` varchar(255) NOT NULL,
  `record_date` date NOT NULL,
  `start_date` date NOT NULL,
  `end_date` date NOT NULL,
  `money` decimal(19,2) NOT NULL,
  `enterprise_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  `product_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `postprocess_agreeme_enterprise_id_34e44c05_fk_base_enterprise_id` (`enterprise_id`),
  KEY `postprocess_agreement_group_id_9a64f67b_fk_base_group_id` (`group_id`),
  KEY `postprocess_agreement_product_id_6ec2d2dd_fk_base_product_id` (`product_id`),
  CONSTRAINT `postprocess_agreement_group_id_9a64f67b_fk_base_group_id` FOREIGN KEY (`group_id`) REFERENCES `base_group` (`id`),
  CONSTRAINT `postprocess_agreement_product_id_6ec2d2dd_fk_base_product_id` FOREIGN KEY (`product_id`) REFERENCES `base_product` (`id`),
  CONSTRAINT `postprocess_agreeme_enterprise_id_34e44c05_fk_base_enterprise_id` FOREIGN KEY (`enterprise_id`) REFERENCES `base_enterprise` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `postprocess_agreement`
--

LOCK TABLES `postprocess_agreement` WRITE;
/*!40000 ALTER TABLE `postprocess_agreement` DISABLE KEYS */;
/*!40000 ALTER TABLE `postprocess_agreement` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `postprocess_assignment`
--

DROP TABLE IF EXISTS `postprocess_assignment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `postprocess_assignment` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `document1` varchar(255) NOT NULL,
  `document2` varchar(255) NOT NULL,
  `document3` varchar(255) NOT NULL,
  `group_id` int(11) DEFAULT NULL,
  `task_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `task_id` (`task_id`),
  KEY `postprocess_assignment_group_id_7f394a22_fk_base_group_id` (`group_id`),
  CONSTRAINT `postprocess_assignment_group_id_7f394a22_fk_base_group_id` FOREIGN KEY (`group_id`) REFERENCES `base_group` (`id`),
  CONSTRAINT `postprocess_assignment_task_id_ce7d84ec_fk_postprocess_task_id` FOREIGN KEY (`task_id`) REFERENCES `postprocess_task` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `postprocess_assignment`
--

LOCK TABLES `postprocess_assignment` WRITE;
/*!40000 ALTER TABLE `postprocess_assignment` DISABLE KEYS */;
/*!40000 ALTER TABLE `postprocess_assignment` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `postprocess_correction`
--

DROP TABLE IF EXISTS `postprocess_correction`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `postprocess_correction` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `start_at` date DEFAULT NULL,
  `complete_at` date DEFAULT NULL,
  `check_at` date DEFAULT NULL,
  `check_situ` varchar(255) DEFAULT NULL,
  `reform_situ` varchar(255) DEFAULT NULL,
  `investigation` varchar(255) DEFAULT NULL,
  `closed_at` date DEFAULT NULL,
  `suggestion` varchar(255) NOT NULL,
  `unable_reform` varchar(255) DEFAULT NULL,
  `document` varchar(255) DEFAULT NULL,
  `unqualified_info` longtext,
  `productgrade_id` int(11),
  `task_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `postprocess_correction_3c0413f3` (`productgrade_id`),
  KEY `postprocess_correction_57746cc8` (`task_id`),
  CONSTRAINT `postprocess_correction_task_id_8cb80bbe_fk_postprocess_task_id` FOREIGN KEY (`task_id`) REFERENCES `postprocess_task` (`id`),
  CONSTRAINT `postproc_productgrade_id_4bcecd3d_fk_postprocess_productgrade_id` FOREIGN KEY (`productgrade_id`) REFERENCES `postprocess_productgrade` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `postprocess_correction`
--

LOCK TABLES `postprocess_correction` WRITE;
/*!40000 ALTER TABLE `postprocess_correction` DISABLE KEYS */;
INSERT INTO `postprocess_correction` VALUES (1,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'chuli',NULL,'/home/sdu/Project/post-process/app/src/main/resources/static/file/鱼c小甲鱼零基础学python全套课后题3b49840b-1314-465c-bcff-00369dc23a59.doc','不合格',2,1);
/*!40000 ALTER TABLE `postprocess_correction` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `postprocess_express`
--

DROP TABLE IF EXISTS `postprocess_express`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `postprocess_express` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `number` varchar(255) NOT NULL,
  `express_is` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `postprocess_express`
--

LOCK TABLES `postprocess_express` WRITE;
/*!40000 ALTER TABLE `postprocess_express` DISABLE KEYS */;
/*!40000 ALTER TABLE `postprocess_express` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `postprocess_inspect`
--

DROP TABLE IF EXISTS `postprocess_inspect`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `postprocess_inspect` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `genre` int(11) NOT NULL,
  `report` longtext NOT NULL,
  `document` varchar(255) NOT NULL,
  `task_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `task_id` (`task_id`),
  CONSTRAINT `postprocess_inspect_task_id_380329c4_fk_postprocess_task_id` FOREIGN KEY (`task_id`) REFERENCES `postprocess_task` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `postprocess_inspect`
--

LOCK TABLES `postprocess_inspect` WRITE;
/*!40000 ALTER TABLE `postprocess_inspect` DISABLE KEYS */;
/*!40000 ALTER TABLE `postprocess_inspect` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `postprocess_inspectioncategory`
--

DROP TABLE IF EXISTS `postprocess_inspectioncategory`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `postprocess_inspectioncategory` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `postprocess_inspectioncategory`
--

LOCK TABLES `postprocess_inspectioncategory` WRITE;
/*!40000 ALTER TABLE `postprocess_inspectioncategory` DISABLE KEYS */;
INSERT INTO `postprocess_inspectioncategory` VALUES (1,'抽查大类A'),(2,'抽查大类B');
/*!40000 ALTER TABLE `postprocess_inspectioncategory` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `postprocess_inspectiontype`
--

DROP TABLE IF EXISTS `postprocess_inspectiontype`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `postprocess_inspectiontype` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `postprocess_inspectiontype`
--

LOCK TABLES `postprocess_inspectiontype` WRITE;
/*!40000 ALTER TABLE `postprocess_inspectiontype` DISABLE KEYS */;
INSERT INTO `postprocess_inspectiontype` VALUES (1,'抽查类型A'),(2,'抽查类型B');
/*!40000 ALTER TABLE `postprocess_inspectiontype` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `postprocess_productgrade`
--

DROP TABLE IF EXISTS `postprocess_productgrade`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `postprocess_productgrade` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `level` int(11) NOT NULL,
  `is_qualified` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `postprocess_productgrade`
--

LOCK TABLES `postprocess_productgrade` WRITE;
/*!40000 ALTER TABLE `postprocess_productgrade` DISABLE KEYS */;
INSERT INTO `postprocess_productgrade` VALUES (1,'残次品',1,0),(2,'有毒',1,0);
/*!40000 ALTER TABLE `postprocess_productgrade` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `postprocess_review`
--

DROP TABLE IF EXISTS `postprocess_review`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `postprocess_review` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `review_type` varchar(255) NOT NULL,
  `review_batch` varchar(255) NOT NULL,
  `review_at` date NOT NULL,
  `delay_apply_at` date DEFAULT NULL,
  `delay_review_at` date DEFAULT NULL,
  `review_situ` varchar(255) DEFAULT NULL,
  `suggestion` varchar(255) NOT NULL,
  `unable_review` varchar(255) DEFAULT NULL,
  `document` varchar(255) DEFAULT NULL,
  `unqualified_info` longtext NOT NULL,
  `number` varchar(255) DEFAULT NULL,
  `report` varchar(255) DEFAULT NULL,
  `express_id` int(11) DEFAULT NULL,
  `group_id` int(11) DEFAULT NULL,
  `productgrade_id` int(11) DEFAULT NULL,
  `status_id` int(11),
  `task_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `express_id` (`express_id`),
  KEY `postprocess_review_group_id_d53852fa_fk_base_group_id` (`group_id`),
  KEY `postproc_productgrade_id_664560ba_fk_postprocess_productgrade_id` (`productgrade_id`),
  KEY `postprocess_review_dc91ed4b` (`status_id`),
  KEY `postprocess_review_57746cc8` (`task_id`),
  CONSTRAINT `postprocess_review_express_id_df564879_fk_postprocess_express_id` FOREIGN KEY (`express_id`) REFERENCES `postprocess_express` (`id`),
  CONSTRAINT `postprocess_review_group_id_d53852fa_fk_base_group_id` FOREIGN KEY (`group_id`) REFERENCES `base_group` (`id`),
  CONSTRAINT `postprocess_review_task_id_ddb58d12_fk_postprocess_task_id` FOREIGN KEY (`task_id`) REFERENCES `postprocess_task` (`id`),
  CONSTRAINT `postprocess_revi_status_id_fc100f01_fk_postprocess_taskstatus_id` FOREIGN KEY (`status_id`) REFERENCES `postprocess_taskstatus` (`id`),
  CONSTRAINT `postproc_productgrade_id_664560ba_fk_postprocess_productgrade_id` FOREIGN KEY (`productgrade_id`) REFERENCES `postprocess_productgrade` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `postprocess_review`
--

LOCK TABLES `postprocess_review` WRITE;
/*!40000 ALTER TABLE `postprocess_review` DISABLE KEYS */;
/*!40000 ALTER TABLE `postprocess_review` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `postprocess_task`
--

DROP TABLE IF EXISTS `postprocess_task`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `postprocess_task` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `number` varchar(255) NOT NULL,
  `inspect_at` date NOT NULL,
  `batch` varchar(255) NOT NULL,
  `enterprise_id` int(11) NOT NULL,
  `inspection_category_id` int(11) NOT NULL,
  `inspection_type_id` int(11) NOT NULL,
  `manufacturer_id` int(11) NOT NULL,
  `product_id` int(11) NOT NULL,
  `status_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `number` (`number`),
  UNIQUE KEY `batch` (`batch`),
  KEY `postprocess_task_enterprise_id_94bc54ea_fk_base_enterprise_id` (`enterprise_id`),
  KEY `D2ea647e3d6ccbd6c635463d9026d17a` (`inspection_category_id`),
  KEY `pos_inspection_type_id_668a1542_fk_postprocess_inspectiontype_id` (`inspection_type_id`),
  KEY `postprocess_tas_manufacturer_id_39f41ff9_fk_base_manufacturer_id` (`manufacturer_id`),
  KEY `postprocess_task_product_id_374eed73_fk_base_product_id` (`product_id`),
  KEY `postprocess_task_dc91ed4b` (`status_id`),
  CONSTRAINT `D2ea647e3d6ccbd6c635463d9026d17a` FOREIGN KEY (`inspection_category_id`) REFERENCES `postprocess_inspectioncategory` (`id`),
  CONSTRAINT `postprocess_task_enterprise_id_94bc54ea_fk_base_enterprise_id` FOREIGN KEY (`enterprise_id`) REFERENCES `base_enterprise` (`id`),
  CONSTRAINT `postprocess_task_product_id_374eed73_fk_base_product_id` FOREIGN KEY (`product_id`) REFERENCES `base_product` (`id`),
  CONSTRAINT `postprocess_task_status_id_d4788781_fk_postprocess_taskstatus_id` FOREIGN KEY (`status_id`) REFERENCES `postprocess_taskstatus` (`id`),
  CONSTRAINT `postprocess_tas_manufacturer_id_39f41ff9_fk_base_manufacturer_id` FOREIGN KEY (`manufacturer_id`) REFERENCES `base_manufacturer` (`id`),
  CONSTRAINT `pos_inspection_type_id_668a1542_fk_postprocess_inspectiontype_id` FOREIGN KEY (`inspection_type_id`) REFERENCES `postprocess_inspectiontype` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `postprocess_task`
--

LOCK TABLES `postprocess_task` WRITE;
/*!40000 ALTER TABLE `postprocess_task` DISABLE KEYS */;
INSERT INTO `postprocess_task` VALUES (1,'28932751276871','2011-11-20','66929632407480',1,1,2,1,1,17);
/*!40000 ALTER TABLE `postprocess_task` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `postprocess_taskstatus`
--

DROP TABLE IF EXISTS `postprocess_taskstatus`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `postprocess_taskstatus` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `code` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`),
  UNIQUE KEY `code` (`code`)
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `postprocess_taskstatus`
--

LOCK TABLES `postprocess_taskstatus` WRITE;
/*!40000 ALTER TABLE `postprocess_taskstatus` DISABLE KEYS */;
INSERT INTO `postprocess_taskstatus` VALUES (1,'已分配任务',1002),(2,'已完成整改任务',4004),(3,'标签、其他复查任务',5003),(4,'正在复查任务',5004),(5,'延期复查任务',5002),(6,'正在整改任务',4003),(7,'无法检测任务',2003),(8,'待整改任务',4002),(10,'待分配任务',1001),(11,'正在检测任务',2002),(12,'待复查任务',5001),(13,'不能复查任务',5005),(14,'复查审查',3002),(15,'已完成复查任务',5006),(16,'已完成检测任务',2004),(17,'后处理审查',3003),(18,'制定任务',1000),(19,'复检审查',3001),(20,'待检测任务',2001),(21,'整改任务',4001),(22,'后处理任务',3004);
/*!40000 ALTER TABLE `postprocess_taskstatus` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `postprocess_test`
--

DROP TABLE IF EXISTS `postprocess_test`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `postprocess_test` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `unable_check` varchar(255) DEFAULT NULL,
  `unqualified_info` longtext,
  `document` varchar(255) DEFAULT NULL,
  `number` varchar(255) DEFAULT NULL,
  `report` varchar(255) DEFAULT NULL,
  `test_type` int(11) DEFAULT NULL,
  `express_id` int(11) DEFAULT NULL,
  `group_id` int(11) NOT NULL,
  `productgrade_id` int(11) DEFAULT NULL,
  `status_id` int(11) NOT NULL,
  `task_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `express_id` (`express_id`),
  KEY `postprocess_test_group_id_7257fdfe_fk_base_group_id` (`group_id`),
  KEY `postproc_productgrade_id_73572bce_fk_postprocess_productgrade_id` (`productgrade_id`),
  KEY `postprocess_test_status_id_74d6f0fb_fk_postprocess_taskstatus_id` (`status_id`),
  KEY `postprocess_test_task_id_f51c07fa_fk_postprocess_task_id` (`task_id`),
  CONSTRAINT `postprocess_test_express_id_3a52a091_fk_postprocess_express_id` FOREIGN KEY (`express_id`) REFERENCES `postprocess_express` (`id`),
  CONSTRAINT `postprocess_test_group_id_7257fdfe_fk_base_group_id` FOREIGN KEY (`group_id`) REFERENCES `base_group` (`id`),
  CONSTRAINT `postprocess_test_status_id_74d6f0fb_fk_postprocess_taskstatus_id` FOREIGN KEY (`status_id`) REFERENCES `postprocess_taskstatus` (`id`),
  CONSTRAINT `postprocess_test_task_id_f51c07fa_fk_postprocess_task_id` FOREIGN KEY (`task_id`) REFERENCES `postprocess_task` (`id`),
  CONSTRAINT `postproc_productgrade_id_73572bce_fk_postprocess_productgrade_id` FOREIGN KEY (`productgrade_id`) REFERENCES `postprocess_productgrade` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `postprocess_test`
--

LOCK TABLES `postprocess_test` WRITE;
/*!40000 ALTER TABLE `postprocess_test` DISABLE KEYS */;
/*!40000 ALTER TABLE `postprocess_test` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2016-12-06 14:42:05