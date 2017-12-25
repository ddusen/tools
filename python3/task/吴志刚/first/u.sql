CREATE DATABASE pc_data
USE `pc_data`;
DROP TABLE IF EXISTS `data`;
CREATE TABLE `data` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` char(200) DEFAULT NULL,
  `pubtime` char(30) DEFAULT NULL,
  `promulgator` varchar(300) DEFAULT NULL,
  `article` text DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
