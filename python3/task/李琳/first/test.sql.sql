/*
SQLyog Ultimate v11.27 (32 bit)
MySQL - 10.1.26-MariaDB-0+deb9u1 : Database - tt
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`tt` /*!40100 DEFAULT CHARACTER SET utf8mb4 */;

USE `tt`;

/*Table structure for table `aa` */

DROP TABLE IF EXISTS `aa`;

CREATE TABLE `aa` (
  `title` varchar(225) NOT NULL,
  `url` varchar(225) NOT NULL,
  `pubtime` varchar(225) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

/*Table structure for table `bb` */

DROP TABLE IF EXISTS `bb`;

CREATE TABLE `bb` (
  `p_title` varchar(225) NOT NULL,
  `pubtime` varchar(225) NOT NULL,
  `author` varchar(225) NOT NULL,
  `p_article` varchar(225) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
