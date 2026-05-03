-- MySQL dump 10.13  Distrib 9.7.0, for Win64 (x86_64)
--
-- Host: localhost    Database: twochic_cims
-- ------------------------------------------------------
-- Server version	9.7.0

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
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
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
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
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
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=57 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',3,'add_permission'),(6,'Can change permission',3,'change_permission'),(7,'Can delete permission',3,'delete_permission'),(8,'Can view permission',3,'view_permission'),(9,'Can add group',2,'add_group'),(10,'Can change group',2,'change_group'),(11,'Can delete group',2,'delete_group'),(12,'Can view group',2,'view_group'),(13,'Can add user',4,'add_user'),(14,'Can change user',4,'change_user'),(15,'Can delete user',4,'delete_user'),(16,'Can view user',4,'view_user'),(17,'Can add content type',5,'add_contenttype'),(18,'Can change content type',5,'change_contenttype'),(19,'Can delete content type',5,'delete_contenttype'),(20,'Can view content type',5,'view_contenttype'),(21,'Can add session',6,'add_session'),(22,'Can change session',6,'change_session'),(23,'Can delete session',6,'delete_session'),(24,'Can view session',6,'view_session'),(25,'Can add raw material',14,'add_rawmaterial'),(26,'Can change raw material',14,'change_rawmaterial'),(27,'Can delete raw material',14,'delete_rawmaterial'),(28,'Can view raw material',14,'view_rawmaterial'),(29,'Can add material unit',9,'add_materialunit'),(30,'Can change material unit',9,'change_materialunit'),(31,'Can delete material unit',9,'delete_materialunit'),(32,'Can view material unit',9,'view_materialunit'),(33,'Can add account',7,'add_account'),(34,'Can change account',7,'change_account'),(35,'Can delete account',7,'delete_account'),(36,'Can view account',7,'view_account'),(37,'Can add product',12,'add_product'),(38,'Can change product',12,'change_product'),(39,'Can delete product',12,'delete_product'),(40,'Can view product',12,'view_product'),(41,'Can add employee',8,'add_employee'),(42,'Can change employee',8,'change_employee'),(43,'Can delete employee',8,'delete_employee'),(44,'Can view employee',8,'view_employee'),(45,'Can add product material',13,'add_productmaterial'),(46,'Can change product material',13,'change_productmaterial'),(47,'Can delete product material',13,'delete_productmaterial'),(48,'Can view product material',13,'view_productmaterial'),(49,'Can add order',10,'add_order'),(50,'Can change order',10,'change_order'),(51,'Can delete order',10,'delete_order'),(52,'Can view order',10,'view_order'),(53,'Can add order item',11,'add_orderitem'),(54,'Can change order item',11,'change_orderitem'),(55,'Can delete order item',11,'delete_orderitem'),(56,'Can view order item',11,'view_orderitem');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `password` varchar(128) COLLATE utf8mb4_unicode_ci NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) COLLATE utf8mb4_unicode_ci NOT NULL,
  `first_name` varchar(150) COLLATE utf8mb4_unicode_ci NOT NULL,
  `last_name` varchar(150) COLLATE utf8mb4_unicode_ci NOT NULL,
  `email` varchar(254) COLLATE utf8mb4_unicode_ci NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$1200000$YmTk1KZS46hW4ylVz36fdn$nBPf8frah8wbrE/5UWAOkWaBM1d3/N8Kxy8ae0NU7WA=',NULL,1,'carlos','','','',1,1,'2026-05-01 22:49:41.879287'),(2,'pbkdf2_sha256$1200000$jiDOKGe5WGLVoMOYJGqHJt$KdaLhGznrroXq8BN8DCLxXC+JzkVk4Vu5vZEqzowD58=','2026-05-03 21:04:27.597115',1,'jceu61','','','',1,1,'2026-05-01 22:52:17.438588');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
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
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext COLLATE utf8mb4_unicode_ci,
  `object_repr` varchar(200) COLLATE utf8mb4_unicode_ci NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2026-05-01 22:55:52.694765','1','Meter (fabrics)',1,'[{\"added\": {}}]',9,2),(2,'2026-05-01 22:56:00.678338','2','Yard (fabrics)',1,'[{\"added\": {}}]',9,2),(3,'2026-05-01 22:56:09.492242','3','Centimeter (fabrics)',1,'[{\"added\": {}}]',9,2),(4,'2026-05-01 22:56:15.344814','4','Piece (trims)',1,'[{\"added\": {}}]',9,2),(5,'2026-05-01 22:56:25.901676','5','Roll (trims)',1,'[{\"added\": {}}]',9,2),(6,'2026-05-01 22:56:34.972327','6','Meter (trims)',1,'[{\"added\": {}}]',9,2),(7,'2026-05-01 22:56:43.017302','7','Yard (trims)',1,'[{\"added\": {}}]',9,2),(8,'2026-05-01 22:56:49.963294','8','Piece (accessories)',1,'[{\"added\": {}}]',9,2),(9,'2026-05-01 22:56:54.757300','9','Set (accessories)',1,'[{\"added\": {}}]',9,2),(10,'2026-05-01 22:57:00.698128','10','Pack (accessories)',1,'[{\"added\": {}}]',9,2);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `model` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(2,'auth','group'),(3,'auth','permission'),(4,'auth','user'),(5,'contenttypes','contenttype'),(6,'sessions','session'),(7,'system_app','account'),(8,'system_app','employee'),(9,'system_app','materialunit'),(10,'system_app','order'),(11,'system_app','orderitem'),(12,'system_app','product'),(13,'system_app','productmaterial'),(14,'system_app','rawmaterial');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `name` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=34 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2026-05-01 22:48:28.214146'),(2,'auth','0001_initial','2026-05-01 22:48:28.929984'),(3,'admin','0001_initial','2026-05-01 22:48:29.094277'),(4,'admin','0002_logentry_remove_auto_add','2026-05-01 22:48:29.105148'),(5,'admin','0003_logentry_add_action_flag_choices','2026-05-01 22:48:29.133255'),(6,'contenttypes','0002_remove_content_type_name','2026-05-01 22:48:29.257819'),(7,'auth','0002_alter_permission_name_max_length','2026-05-01 22:48:29.346801'),(8,'auth','0003_alter_user_email_max_length','2026-05-01 22:48:29.384818'),(9,'auth','0004_alter_user_username_opts','2026-05-01 22:48:29.398753'),(10,'auth','0005_alter_user_last_login_null','2026-05-01 22:48:29.480973'),(11,'auth','0006_require_contenttypes_0002','2026-05-01 22:48:29.485686'),(12,'auth','0007_alter_validators_add_error_messages','2026-05-01 22:48:29.501970'),(13,'auth','0008_alter_user_username_max_length','2026-05-01 22:48:29.598965'),(14,'auth','0009_alter_user_last_name_max_length','2026-05-01 22:48:29.704237'),(15,'auth','0010_alter_group_name_max_length','2026-05-01 22:48:29.732817'),(16,'auth','0011_update_proxy_permissions','2026-05-01 22:48:29.749606'),(17,'auth','0012_alter_user_first_name_max_length','2026-05-01 22:48:29.837796'),(18,'sessions','0001_initial','2026-05-01 22:48:29.892556'),(19,'system_app','0001_initial','2026-05-01 22:48:29.920219'),(20,'system_app','0002_rename_rawmaterials_rawmaterial','2026-05-01 22:48:29.967588'),(21,'system_app','0003_materialunit_alter_rawmaterial_material_category_and_more','2026-05-01 22:48:30.184556'),(22,'system_app','0004_account','2026-05-01 22:48:30.224959'),(23,'system_app','0005_rename_username_account_employee_id','2026-05-01 22:48:30.255422'),(24,'system_app','0006_product','2026-05-01 22:48:30.298348'),(25,'system_app','0007_employee','2026-05-01 22:48:30.328229'),(26,'system_app','0008_product_quantity','2026-05-01 22:48:30.414220'),(27,'system_app','0009_product_price','2026-05-01 22:48:30.491167'),(28,'system_app','0010_alter_rawmaterial_material_quantity_productmaterial','2026-05-01 22:48:30.786557'),(29,'system_app','0011_order_orderitem','2026-05-01 22:48:31.012929'),(30,'system_app','0012_rawmaterial_minimum_threshold','2026-05-01 22:48:31.099648'),(31,'system_app','0013_alter_employee_employee_id','2026-05-01 22:48:31.105517'),(32,'system_app','0014_orderitem_product_name_orderitem_product_price_and_more','2026-05-01 22:48:31.456010'),(33,'system_app','0015_orderitem_material_cost','2026-05-01 22:48:31.552057');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) COLLATE utf8mb4_unicode_ci NOT NULL,
  `session_data` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('5crzd03ebwjetuj8o2hqd0rb4e6ybq1g','.eJxVjMsOwiAQRf9l1k1ToKHSpa79BjIwg60imFJijPHfjY-FLu85J_cOtczpYIkD1rjaC5ZyzQvBGDAWbgC9zzWtdiYY-wb4fIn5xvzeIPpOwA9MeGYYYYdLzAUasFjXydbCy6eX_8yhP3F6CTpiOuTW57Qus2tfSfu1pd1n4rj9tn8HE5YJRghyE4ynrlOenBJeoyJv9OA4yF5oJTWxkZtBo5DaOaMHI6nrSRuhXDABHk9QaVe7:1wJdzH:MjXQdCN5EqcVjf7ztBSB7iPSwIY4PqBcpLo1T0r3ZbQ','2026-05-17 21:04:27.605505'),('d3hhqax3lblqsj6gsmyett4phyy9i9xw','.eJyrViotzsxLj09JTUsszSmJL0gsLi7PL0pRskpLzClO1VFKTE7OL80ric8ECpnpKKXmFuTkV6amgvlKhgbmJkpIgnmJualA4ZDU4hKlWgD5sx_r:1wJbrs:gGi4zzSJwkKElZzmcsYkhYPywjU7Kt0c66CBtmyaCto','2026-05-17 18:48:40.613936'),('o0blu7k4w4f87bjwqe5fywtsou3cs1ns','.eJxVjEEOgyAQAP-y54YImFU89t43kIUFtTXQgKSHpn9vTLx4nZnMF1pd02w5RGrbbt9U6ycXhinSVsMNLLV9sa2GYleGCRRcmCP_CukQ_KQ0Z-Fz2svqxJGI01bxyBy2-9leBgvVBSaIaozGc9dpz05Lj6TZGxxciKqXqBVyMGockKRC5wwORnHXMxqpXTQRfn-vr0PS:1wIwjx:S6YiEiNfYvYib0IjXDGwdmG1phKdmUHWG2OvRZ1h3-s','2026-05-15 22:53:45.404186');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `system_app_account`
--

DROP TABLE IF EXISTS `system_app_account`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `system_app_account` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `employee_id` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `password` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`employee_id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `system_app_account`
--

LOCK TABLES `system_app_account` WRITE;
/*!40000 ALTER TABLE `system_app_account` DISABLE KEYS */;
INSERT INTO `system_app_account` VALUES (1,'0','00000'),(2,'1753','1111'),(3,'2120','2345'),(4,'1401','12345'),(6,'1074','1234');
/*!40000 ALTER TABLE `system_app_account` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `system_app_employee`
--

DROP TABLE IF EXISTS `system_app_employee`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `system_app_employee` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `employee_id` varchar(10) COLLATE utf8mb4_unicode_ci NOT NULL,
  `employee_name` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `employee_role` varchar(30) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `employee_id` (`employee_id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `system_app_employee`
--

LOCK TABLES `system_app_employee` WRITE;
/*!40000 ALTER TABLE `system_app_employee` DISABLE KEYS */;
INSERT INTO `system_app_employee` VALUES (1,'1753','Ryan','production_manager'),(2,'2120','Drea','production_employee'),(3,'1401','Carlos','production_manager'),(5,'1074','Test','production_manager');
/*!40000 ALTER TABLE `system_app_employee` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `system_app_materialunit`
--

DROP TABLE IF EXISTS `system_app_materialunit`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `system_app_materialunit` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `unit_name` varchar(20) COLLATE utf8mb4_unicode_ci NOT NULL,
  `category` varchar(15) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `system_app_materialunit`
--

LOCK TABLES `system_app_materialunit` WRITE;
/*!40000 ALTER TABLE `system_app_materialunit` DISABLE KEYS */;
INSERT INTO `system_app_materialunit` VALUES (1,'Meter','fabrics'),(2,'Yard','fabrics'),(3,'Centimeter','fabrics'),(4,'Piece','trims'),(5,'Roll','trims'),(6,'Meter','trims'),(7,'Yard','trims'),(8,'Piece','accessories'),(9,'Set','accessories'),(10,'Pack','accessories');
/*!40000 ALTER TABLE `system_app_materialunit` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `system_app_order`
--

DROP TABLE IF EXISTS `system_app_order`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `system_app_order` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `created_at` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `system_app_order`
--

LOCK TABLES `system_app_order` WRITE;
/*!40000 ALTER TABLE `system_app_order` DISABLE KEYS */;
INSERT INTO `system_app_order` VALUES (1,'2026-05-03 16:45:48.290511'),(2,'2026-05-03 17:05:08.213027');
/*!40000 ALTER TABLE `system_app_order` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `system_app_orderitem`
--

DROP TABLE IF EXISTS `system_app_orderitem`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `system_app_orderitem` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `quantity` int unsigned NOT NULL,
  `order_id` bigint NOT NULL,
  `product_id` bigint DEFAULT NULL,
  `product_name` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `product_price` double NOT NULL,
  `material_cost` double NOT NULL,
  PRIMARY KEY (`id`),
  KEY `system_app_orderitem_order_id_7130e9c7_fk_system_app_order_id` (`order_id`),
  KEY `system_app_orderitem_product_id_04e928e9_fk_system_ap` (`product_id`),
  CONSTRAINT `system_app_orderitem_order_id_7130e9c7_fk_system_app_order_id` FOREIGN KEY (`order_id`) REFERENCES `system_app_order` (`id`),
  CONSTRAINT `system_app_orderitem_product_id_04e928e9_fk_system_ap` FOREIGN KEY (`product_id`) REFERENCES `system_app_product` (`id`),
  CONSTRAINT `system_app_orderitem_chk_1` CHECK ((`quantity` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `system_app_orderitem`
--

LOCK TABLES `system_app_orderitem` WRITE;
/*!40000 ALTER TABLE `system_app_orderitem` DISABLE KEYS */;
INSERT INTO `system_app_orderitem` VALUES (1,1,1,NULL,'White Hoodie',3499,1024),(2,1,2,2,'Sweatshirt',2400,0);
/*!40000 ALTER TABLE `system_app_orderitem` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `system_app_product`
--

DROP TABLE IF EXISTS `system_app_product`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `system_app_product` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `product_id` varchar(10) COLLATE utf8mb4_unicode_ci NOT NULL,
  `product_name` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `product_category` varchar(20) COLLATE utf8mb4_unicode_ci NOT NULL,
  `product_collection` varchar(20) COLLATE utf8mb4_unicode_ci NOT NULL,
  `quantity` int unsigned NOT NULL,
  `price` double NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `product_id` (`product_id`),
  CONSTRAINT `system_app_product_chk_1` CHECK ((`quantity` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `system_app_product`
--

LOCK TABLES `system_app_product` WRITE;
/*!40000 ALTER TABLE `system_app_product` DISABLE KEYS */;
INSERT INTO `system_app_product` VALUES (2,'#00002','Sweatshirt','tops','summer',0,0),(3,'#00003','Santa\'s Fit','bottoms','holiday',0,-1999);
/*!40000 ALTER TABLE `system_app_product` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `system_app_productmaterial`
--

DROP TABLE IF EXISTS `system_app_productmaterial`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `system_app_productmaterial` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `quantity_per_garment` double NOT NULL,
  `fabric_length` double DEFAULT NULL,
  `fabric_width` double DEFAULT NULL,
  `product_id` bigint NOT NULL,
  `raw_material_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `system_app_productmateri_product_id_raw_material__a12fc333_uniq` (`product_id`,`raw_material_id`),
  KEY `system_app_productma_raw_material_id_7991ab41_fk_system_ap` (`raw_material_id`),
  CONSTRAINT `system_app_productma_product_id_7d9850e4_fk_system_ap` FOREIGN KEY (`product_id`) REFERENCES `system_app_product` (`id`),
  CONSTRAINT `system_app_productma_raw_material_id_7991ab41_fk_system_ap` FOREIGN KEY (`raw_material_id`) REFERENCES `system_app_rawmaterial` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `system_app_productmaterial`
--

LOCK TABLES `system_app_productmaterial` WRITE;
/*!40000 ALTER TABLE `system_app_productmaterial` DISABLE KEYS */;
INSERT INTO `system_app_productmaterial` VALUES (4,1,NULL,NULL,3,5),(6,10,10,NULL,2,1);
/*!40000 ALTER TABLE `system_app_productmaterial` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `system_app_rawmaterial`
--

DROP TABLE IF EXISTS `system_app_rawmaterial`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `system_app_rawmaterial` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `material_name` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `material_category` varchar(15) COLLATE utf8mb4_unicode_ci NOT NULL,
  `material_quantity` double NOT NULL,
  `material_unit_id` bigint NOT NULL,
  `material_unitprice` double NOT NULL,
  `minimum_threshold` double NOT NULL,
  PRIMARY KEY (`id`),
  KEY `system_app_rawmaterial_material_unit_id_88700166` (`material_unit_id`),
  CONSTRAINT `system_app_rawmateri_material_unit_id_88700166_fk_system_ap` FOREIGN KEY (`material_unit_id`) REFERENCES `system_app_materialunit` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `system_app_rawmaterial`
--

LOCK TABLES `system_app_rawmaterial` WRITE;
/*!40000 ALTER TABLE `system_app_rawmaterial` DISABLE KEYS */;
INSERT INTO `system_app_rawmaterial` VALUES (1,'Red Cloth','fabrics',1000,2,1000,10),(4,'Grey Cloth','fabrics',900,2,100,10),(5,'Frills','trims',980,6,10,10),(9,'Frills','trims',1,6,10,10),(10,'aaaa','fabrics',0,3,0,0);
/*!40000 ALTER TABLE `system_app_rawmaterial` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2026-05-04  5:05:50
