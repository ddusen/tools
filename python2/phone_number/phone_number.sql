USE test;

DROP TABLE phone_number;

CREATE TABLE `phone_number`(
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `number` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3199 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
