-- MySQL dump 10.13  Distrib 8.0.46, for Win64 (x86_64)
--
-- Host: localhost    Database: projectp1
-- ------------------------------------------------------
-- Server version	8.0.46

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
-- Table structure for table `alembic_version`
--

DROP TABLE IF EXISTS `alembic_version`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `alembic_version` (
  `version_num` varchar(32) NOT NULL,
  PRIMARY KEY (`version_num`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `alembic_version`
--

LOCK TABLES `alembic_version` WRITE;
/*!40000 ALTER TABLE `alembic_version` DISABLE KEYS */;
INSERT INTO `alembic_version` VALUES ('35ac004b588a');
/*!40000 ALTER TABLE `alembic_version` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `feedback`
--

DROP TABLE IF EXISTS `feedback`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `feedback` (
  `id` int NOT NULL AUTO_INCREMENT,
  `ticket_id` int NOT NULL,
  `user_id` int NOT NULL,
  `rating` int NOT NULL,
  `comment` text,
  `created_at` datetime NOT NULL DEFAULT (now()),
  PRIMARY KEY (`id`),
  UNIQUE KEY `ticket_id` (`ticket_id`),
  KEY `user_id` (`user_id`),
  CONSTRAINT `feedback_ibfk_1` FOREIGN KEY (`ticket_id`) REFERENCES `tickets` (`id`),
  CONSTRAINT `feedback_ibfk_2` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `feedback`
--

LOCK TABLES `feedback` WRITE;
/*!40000 ALTER TABLE `feedback` DISABLE KEYS */;
INSERT INTO `feedback` VALUES (1,5,3,5,'The issue was resolved quickly and professionally.','2026-08-23 12:29:08'),(8,38,3,5,'Good Expreince','2026-08-23 23:51:25');
/*!40000 ALTER TABLE `feedback` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `roles`
--

DROP TABLE IF EXISTS `roles`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `roles` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `roles`
--

LOCK TABLES `roles` WRITE;
/*!40000 ALTER TABLE `roles` DISABLE KEYS */;
INSERT INTO `roles` VALUES (3,'ADMIN'),(1,'EMPLOYEE'),(2,'SUPPORT_AGENT');
/*!40000 ALTER TABLE `roles` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sla_rules`
--

DROP TABLE IF EXISTS `sla_rules`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `sla_rules` (
  `id` int NOT NULL AUTO_INCREMENT,
  `priority` varchar(20) NOT NULL,
  `response_time_hours` int NOT NULL,
  `resolution_time_hours` int NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `priority` (`priority`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sla_rules`
--

LOCK TABLES `sla_rules` WRITE;
/*!40000 ALTER TABLE `sla_rules` DISABLE KEYS */;
INSERT INTO `sla_rules` VALUES (1,'Low',24,72,1),(2,'Medium',8,48,1),(3,'High',2,8,1),(4,'Critical',1,4,1);
/*!40000 ALTER TABLE `sla_rules` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ticket_assignments`
--

DROP TABLE IF EXISTS `ticket_assignments`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ticket_assignments` (
  `id` int NOT NULL AUTO_INCREMENT,
  `ticket_id` int NOT NULL,
  `agent_id` int NOT NULL,
  `assigned_at` datetime NOT NULL DEFAULT (now()),
  `assigned_by` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `agent_id` (`agent_id`),
  KEY `assigned_by` (`assigned_by`),
  KEY `ticket_id` (`ticket_id`),
  CONSTRAINT `ticket_assignments_ibfk_1` FOREIGN KEY (`agent_id`) REFERENCES `users` (`id`),
  CONSTRAINT `ticket_assignments_ibfk_2` FOREIGN KEY (`assigned_by`) REFERENCES `users` (`id`),
  CONSTRAINT `ticket_assignments_ibfk_3` FOREIGN KEY (`ticket_id`) REFERENCES `tickets` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=32 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ticket_assignments`
--

LOCK TABLES `ticket_assignments` WRITE;
/*!40000 ALTER TABLE `ticket_assignments` DISABLE KEYS */;
INSERT INTO `ticket_assignments` VALUES (1,1,5,'2026-08-21 14:38:10',4),(2,1,5,'2026-08-21 14:48:32',4),(3,1,5,'2026-08-23 10:35:15',4),(4,1,5,'2026-08-23 10:38:22',4),(5,3,5,'2026-08-23 11:39:22',4),(6,3,5,'2026-08-23 12:18:23',4),(7,5,5,'2026-08-23 12:26:26',4),(22,38,5,'2026-08-23 23:18:55',4),(23,34,5,'2026-08-23 23:20:10',4),(24,36,5,'2026-08-23 23:22:18',4),(25,32,5,'2026-08-23 23:25:38',4),(26,30,6,'2026-08-23 23:27:11',4),(27,43,6,'2026-08-24 11:58:35',4),(28,44,6,'2026-08-24 12:00:36',4),(29,45,5,'2026-08-24 14:28:40',4),(30,46,9,'2026-08-25 19:24:31',4);
/*!40000 ALTER TABLE `ticket_assignments` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ticket_attachments`
--

DROP TABLE IF EXISTS `ticket_attachments`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ticket_attachments` (
  `id` int NOT NULL AUTO_INCREMENT,
  `ticket_id` int NOT NULL,
  `uploaded_by` int NOT NULL,
  `filename` varchar(255) NOT NULL,
  `filepath` varchar(500) NOT NULL,
  `file_size` int NOT NULL,
  `uploaded_at` datetime NOT NULL DEFAULT (now()),
  PRIMARY KEY (`id`),
  KEY `ticket_id` (`ticket_id`),
  KEY `uploaded_by` (`uploaded_by`),
  CONSTRAINT `ticket_attachments_ibfk_1` FOREIGN KEY (`ticket_id`) REFERENCES `tickets` (`id`),
  CONSTRAINT `ticket_attachments_ibfk_2` FOREIGN KEY (`uploaded_by`) REFERENCES `users` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ticket_attachments`
--

LOCK TABLES `ticket_attachments` WRITE;
/*!40000 ALTER TABLE `ticket_attachments` DISABLE KEYS */;
INSERT INTO `ticket_attachments` VALUES (1,2,2,'Screenshot_28.png','uploads\\091899af-9944-4397-9ce2-b87d0eaad911.png',581393,'2026-08-23 11:01:17'),(2,7,3,'Screenshot_28.png','uploads\\80bf47ce-180e-429a-9710-36d623d1847f.png',581393,'2026-08-23 23:02:15'),(3,38,3,'Screenshot_29.png','uploads\\62614f63-af41-417e-8146-6de729946464.png',236208,'2026-08-23 23:09:26'),(4,42,7,'Screenshot_42.png','uploads\\59b0e6a6-ba24-4a6e-b7b1-1df46fa6e830.png',38305,'2026-08-23 23:31:39'),(5,46,9,'1371407.jpeg','uploads\\638170f6-2f83-42f9-bb6a-4dc4c9ef7d72.jpeg',2129368,'2026-08-25 19:26:28');
/*!40000 ALTER TABLE `ticket_attachments` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ticket_categories`
--

DROP TABLE IF EXISTS `ticket_categories`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ticket_categories` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `description` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ticket_categories`
--

LOCK TABLES `ticket_categories` WRITE;
/*!40000 ALTER TABLE `ticket_categories` DISABLE KEYS */;
INSERT INTO `ticket_categories` VALUES (1,'Hardware','Laptop, desktop, printer and hardware issues'),(2,'Software','Application and software issues'),(3,'Network','Wi-Fi, LAN and internet issues'),(4,'Email','Email and mailbox issues'),(5,'Access','Account and access problems');
/*!40000 ALTER TABLE `ticket_categories` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ticket_comments`
--

DROP TABLE IF EXISTS `ticket_comments`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ticket_comments` (
  `id` int NOT NULL AUTO_INCREMENT,
  `ticket_id` int NOT NULL,
  `user_id` int NOT NULL,
  `comment` text NOT NULL,
  `created_at` datetime NOT NULL DEFAULT (now()),
  PRIMARY KEY (`id`),
  KEY `ticket_id` (`ticket_id`),
  KEY `user_id` (`user_id`),
  CONSTRAINT `ticket_comments_ibfk_1` FOREIGN KEY (`ticket_id`) REFERENCES `tickets` (`id`),
  CONSTRAINT `ticket_comments_ibfk_2` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ticket_comments`
--

LOCK TABLES `ticket_comments` WRITE;
/*!40000 ALTER TABLE `ticket_comments` DISABLE KEYS */;
INSERT INTO `ticket_comments` VALUES (1,1,4,'Test comment','2026-08-21 14:48:42'),(2,38,3,'test comment','2026-08-23 23:08:39'),(3,42,7,'the software take a lot to load','2026-08-23 23:31:56'),(4,44,8,'I am using TP link1','2026-08-24 12:10:44');
/*!40000 ALTER TABLE `ticket_comments` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ticket_history`
--

DROP TABLE IF EXISTS `ticket_history`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ticket_history` (
  `id` int NOT NULL AUTO_INCREMENT,
  `ticket_id` int NOT NULL,
  `user_id` int NOT NULL,
  `action` varchar(100) NOT NULL,
  `old_value` text,
  `new_value` text,
  `created_at` datetime NOT NULL DEFAULT (now()),
  PRIMARY KEY (`id`),
  KEY `ticket_id` (`ticket_id`),
  KEY `user_id` (`user_id`),
  CONSTRAINT `ticket_history_ibfk_1` FOREIGN KEY (`ticket_id`) REFERENCES `tickets` (`id`),
  CONSTRAINT `ticket_history_ibfk_2` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=94 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ticket_history`
--

LOCK TABLES `ticket_history` WRITE;
/*!40000 ALTER TABLE `ticket_history` DISABLE KEYS */;
INSERT INTO `ticket_history` VALUES (1,1,4,'Ticket Assigned','Open','Assigned to Support Agent','2026-08-21 14:48:32'),(2,1,4,'Status Changed','Assigned','In Progress','2026-08-21 14:48:50'),(3,1,4,'Status Changed','In Progress','Resolved','2026-08-21 14:48:54'),(4,1,4,'Status Changed','Resolved','Closed','2026-08-21 14:48:56'),(5,1,4,'Ticket Assigned','Closed','Assigned to Support Agent','2026-08-23 10:35:15'),(6,1,4,'Ticket Assigned','Assigned','Assigned to Support Agent','2026-08-23 10:38:22'),(7,1,5,'Status Changed','Assigned','In Progress','2026-08-23 10:42:51'),(8,1,5,'Status Changed','In Progress','Resolved','2026-08-23 10:43:33'),(9,3,5,'Ticket Created',NULL,'Open','2026-08-23 11:29:51'),(10,3,4,'Ticket Assigned','Open','Assigned to Support Agent','2026-08-23 11:39:22'),(11,3,5,'Response SLA Breached',NULL,'Escalated','2026-08-23 11:58:31'),(12,3,5,'Resolution SLA Breached',NULL,'Escalated','2026-08-23 11:58:31'),(13,4,3,'Ticket Created',NULL,'Open','2026-08-23 12:15:30'),(14,3,4,'Ticket Assigned','Open','Assigned to Support Agent','2026-08-23 12:18:23'),(15,3,5,'Status Changed','Assigned','In Progress','2026-08-23 12:19:49'),(16,3,5,'Status Changed','In Progress','Resolved','2026-08-23 12:20:03'),(17,3,5,'Status Changed','Resolved','Closed','2026-08-23 12:20:13'),(18,5,3,'Ticket Created',NULL,'Open','2026-08-23 12:25:08'),(19,5,4,'Ticket Assigned','Open','Assigned to Support Agent','2026-08-23 12:26:26'),(20,5,5,'Status Changed','Assigned','In Progress','2026-08-23 12:27:34'),(21,5,5,'Status Changed','In Progress','Resolved','2026-08-23 12:27:54'),(22,5,5,'Status Changed','Resolved','Closed','2026-08-23 12:28:07'),(23,5,3,'Feedback Submitted',NULL,'Rating: 5/5','2026-08-23 12:29:08'),(24,6,3,'Ticket Created',NULL,'Open','2026-08-23 21:58:45'),(25,7,3,'Ticket Created',NULL,'Open','2026-08-23 22:00:16'),(26,8,3,'Ticket Created',NULL,'Open','2026-08-23 22:01:24'),(27,9,3,'Ticket Created',NULL,'Open','2026-08-23 22:01:56'),(28,1,1,'Status Changed','Resolved','Closed','2026-08-23 22:01:56'),(29,10,3,'Ticket Created',NULL,'Open','2026-08-23 22:03:27'),(30,11,3,'Ticket Created',NULL,'Open','2026-08-23 22:04:08'),(31,12,3,'Ticket Created',NULL,'Open','2026-08-23 22:04:50'),(32,13,3,'Ticket Created',NULL,'Open','2026-08-23 22:06:09'),(33,14,3,'Ticket Created',NULL,'Open','2026-08-23 22:07:18'),(34,15,3,'Ticket Created',NULL,'Open','2026-08-23 22:08:13'),(35,16,3,'Ticket Created',NULL,'Open','2026-08-23 22:09:02'),(37,18,3,'Ticket Created',NULL,'Open','2026-08-23 22:10:11'),(39,20,3,'Ticket Created',NULL,'Open','2026-08-23 22:10:50'),(41,22,3,'Ticket Created',NULL,'Open','2026-08-23 22:36:24'),(43,24,3,'Ticket Created',NULL,'Open','2026-08-23 22:37:02'),(45,26,3,'Ticket Created',NULL,'Open','2026-08-23 22:38:12'),(47,28,3,'Ticket Created',NULL,'Open','2026-08-23 22:40:35'),(49,30,3,'Ticket Created',NULL,'Open','2026-08-23 22:42:13'),(51,32,3,'Ticket Created',NULL,'Open','2026-08-23 22:43:13'),(53,34,3,'Ticket Created',NULL,'Open','2026-08-23 22:43:46'),(54,1,3,'Feedback Submitted',NULL,'Rating: 5/5','2026-08-23 22:43:46'),(56,36,3,'Ticket Created',NULL,'Open','2026-08-23 22:44:48'),(57,1,3,'Feedback Submitted',NULL,'Rating: 5/5','2026-08-23 22:44:48'),(59,38,3,'Ticket Created',NULL,'Open','2026-08-23 22:46:10'),(60,1,3,'Feedback Submitted',NULL,'Rating: 5/5','2026-08-23 22:46:11'),(62,1,3,'Feedback Submitted',NULL,'Rating: 5/5','2026-08-23 22:46:48'),(64,1,3,'Feedback Submitted',NULL,'Rating: 5/5','2026-08-23 22:47:48'),(66,38,4,'Ticket Assigned','Open','Assigned to Support Agent','2026-08-23 23:18:55'),(67,38,4,'Status Changed','Assigned','In Progress','2026-08-23 23:19:05'),(68,34,4,'Ticket Assigned','Open','Assigned to Support Agent','2026-08-23 23:20:10'),(69,36,4,'Ticket Assigned','Open','Assigned to Support Agent','2026-08-23 23:22:18'),(70,32,4,'Ticket Assigned','Open','Assigned to Support Agent','2026-08-23 23:25:38'),(71,30,4,'Ticket Assigned','Open','Assigned to Lokesh','2026-08-23 23:27:11'),(72,42,7,'Ticket Created',NULL,'Open','2026-08-23 23:31:20'),(73,36,5,'Status Changed','Assigned','In Progress','2026-08-23 23:43:47'),(74,36,5,'Status Changed','In Progress','Resolved','2026-08-23 23:43:50'),(75,36,5,'Status Changed','Resolved','Closed','2026-08-23 23:43:52'),(76,34,5,'Status Changed','Assigned','In Progress','2026-08-23 23:44:19'),(77,34,5,'Status Changed','In Progress','Resolved','2026-08-23 23:44:21'),(78,34,5,'Status Changed','Resolved','Closed','2026-08-23 23:44:22'),(79,1,3,'Feedback Submitted',NULL,'Rating: 5/5','2026-08-23 23:46:10'),(80,38,5,'Status Changed','In Progress','Resolved','2026-08-23 23:50:28'),(81,38,5,'Status Changed','Resolved','Closed','2026-08-23 23:50:33'),(82,38,3,'Feedback Submitted',NULL,'Rating: 5/5','2026-08-23 23:51:25'),(83,30,4,'Status Changed','Assigned','In Progress','2026-08-24 10:55:56'),(84,43,4,'Ticket Created',NULL,'Open','2026-08-24 11:58:13'),(85,43,4,'Ticket Assigned','Open','Assigned to Lokesh','2026-08-24 11:58:35'),(86,44,8,'Ticket Created',NULL,'Open','2026-08-24 12:00:04'),(87,44,4,'Ticket Assigned','Open','Assigned to Lokesh','2026-08-24 12:00:36'),(88,45,8,'Ticket Created',NULL,'Open','2026-08-24 14:27:25'),(89,45,4,'Ticket Assigned','Open','Assigned to Support Agent','2026-08-24 14:28:40'),(90,46,8,'Ticket Created',NULL,'Open','2026-08-25 19:19:43'),(91,46,4,'Ticket Assigned','Open','Assigned to Aryan','2026-08-25 19:24:31'),(92,1,3,'Feedback Submitted',NULL,'Rating: 5/5','2026-08-25 19:31:21');
/*!40000 ALTER TABLE `ticket_history` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tickets`
--

DROP TABLE IF EXISTS `tickets`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tickets` (
  `id` int NOT NULL AUTO_INCREMENT,
  `title` varchar(100) NOT NULL,
  `description` text NOT NULL,
  `priority` varchar(20) NOT NULL,
  `severity` varchar(20) NOT NULL,
  `status` varchar(20) NOT NULL,
  `requester_id` int DEFAULT NULL,
  `category_id` int NOT NULL,
  `created_at` datetime NOT NULL DEFAULT (now()),
  `updated_at` datetime NOT NULL DEFAULT (now()),
  `response_due_at` datetime DEFAULT NULL,
  `resolution_due_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `category_id` (`category_id`),
  KEY `requester_id` (`requester_id`),
  CONSTRAINT `tickets_ibfk_1` FOREIGN KEY (`category_id`) REFERENCES `ticket_categories` (`id`),
  CONSTRAINT `tickets_ibfk_2` FOREIGN KEY (`requester_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=48 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tickets`
--

LOCK TABLES `tickets` WRITE;
/*!40000 ALTER TABLE `tickets` DISABLE KEYS */;
INSERT INTO `tickets` VALUES (1,'Laptop Wifi not working','My laptop cannot connect to the office Wi-Fi.','High','High','Closed',3,3,'2026-08-20 21:13:50','2026-08-23 22:01:56',NULL,NULL),(2,'Display Screen Flicker','My display screen is flickering','High','Medium','Open',2,1,'2026-08-23 10:53:31','2026-08-23 10:53:31',NULL,NULL),(3,'VPN connection problem','Unable to connect to the company VPN.','High','High','Closed',5,2,'2026-08-23 11:29:51','2026-08-23 12:20:13','2026-08-23 09:45:32','2026-08-23 10:45:32'),(4,'Keyboard issue','Several keyboard keys are not working.','Medium','Medium','Open',3,1,'2026-08-23 12:15:30','2026-08-23 12:15:30','2026-08-23 20:15:30','2026-08-25 12:15:30'),(5,'Printer not working','The printer on the second floor is not printing documents.','Medium','Medium','Closed',3,1,'2026-08-23 12:25:08','2026-08-23 12:28:07','2026-08-23 20:25:08','2026-08-25 12:25:08'),(6,'Test ticket','Created from pytest','Medium','Medium','Open',3,1,'2026-08-23 21:58:45','2026-08-23 21:58:45','2026-08-24 05:58:45','2026-08-25 21:58:45'),(7,'Test ticket','Created from pytest','Medium','Medium','Open',3,1,'2026-08-23 22:00:16','2026-08-23 22:00:16','2026-08-24 06:00:17','2026-08-25 22:00:17'),(8,'Test ticket','Created from pytest','Medium','Medium','Open',3,1,'2026-08-23 22:01:24','2026-08-23 22:01:24','2026-08-24 06:01:24','2026-08-25 22:01:24'),(9,'Test ticket','Created from pytest','Medium','Medium','Open',3,1,'2026-08-23 22:01:56','2026-08-23 22:01:56','2026-08-24 06:01:56','2026-08-25 22:01:56'),(10,'Test ticket','Created from pytest','Medium','Medium','Open',3,1,'2026-08-23 22:03:27','2026-08-23 22:03:27','2026-08-24 06:03:27','2026-08-25 22:03:27'),(11,'Test ticket','Created from pytest','Medium','Medium','Open',3,1,'2026-08-23 22:04:08','2026-08-23 22:04:08','2026-08-24 06:04:08','2026-08-25 22:04:08'),(12,'Test ticket','Created from pytest','Medium','Medium','Open',3,1,'2026-08-23 22:04:50','2026-08-23 22:04:50','2026-08-24 06:04:51','2026-08-25 22:04:51'),(13,'Test ticket','Created from pytest','Medium','Medium','Open',3,1,'2026-08-23 22:06:09','2026-08-23 22:06:09','2026-08-24 06:06:10','2026-08-25 22:06:10'),(14,'Test ticket','Created from pytest','Medium','Medium','Open',3,1,'2026-08-23 22:07:18','2026-08-23 22:07:18','2026-08-24 06:07:18','2026-08-25 22:07:18'),(15,'Test ticket','Created from pytest','Medium','Medium','Open',3,1,'2026-08-23 22:08:13','2026-08-23 22:08:13','2026-08-24 06:08:13','2026-08-25 22:08:13'),(16,'Test ticket','Created from pytest','Medium','Medium','Open',3,1,'2026-08-23 22:09:02','2026-08-23 22:09:02','2026-08-24 06:09:02','2026-08-25 22:09:02'),(18,'Test ticket','Created from pytest','Medium','Medium','Open',3,1,'2026-08-23 22:10:11','2026-08-23 22:10:11','2026-08-24 06:10:11','2026-08-25 22:10:11'),(20,'Test ticket','Created from pytest','Medium','Medium','Open',3,1,'2026-08-23 22:10:50','2026-08-23 22:10:50','2026-08-24 06:10:50','2026-08-25 22:10:50'),(22,'Test ticket','Created from pytest','Medium','Medium','Open',3,1,'2026-08-23 22:36:24','2026-08-23 22:36:24','2026-08-24 06:36:25','2026-08-25 22:36:25'),(24,'Test ticket','Created from pytest','Medium','Medium','Open',3,1,'2026-08-23 22:37:02','2026-08-23 22:37:02','2026-08-24 06:37:02','2026-08-25 22:37:02'),(26,'Test ticket','Created from pytest','Medium','Medium','Open',3,1,'2026-08-23 22:38:12','2026-08-23 22:38:12','2026-08-24 06:38:12','2026-08-25 22:38:12'),(28,'Test ticket','Created from pytest','Medium','Medium','Open',3,1,'2026-08-23 22:40:35','2026-08-23 22:40:35','2026-08-24 06:40:36','2026-08-25 22:40:36'),(30,'Test ticket','Created from pytest','Medium','Medium','In Progress',3,1,'2026-08-23 22:42:13','2026-08-24 10:55:56','2026-08-24 06:42:14','2026-08-25 22:42:14'),(32,'Test ticket','Created from pytest','Medium','Medium','Assigned',3,1,'2026-08-23 22:43:13','2026-08-23 23:25:38','2026-08-24 06:43:13','2026-08-25 22:43:13'),(34,'Test ticket','Created from pytest','Medium','Medium','Closed',3,1,'2026-08-23 22:43:46','2026-08-23 23:44:22','2026-08-24 06:43:47','2026-08-25 22:43:47'),(36,'Test ticket','Created from pytest','Medium','Medium','Closed',3,1,'2026-08-23 22:44:48','2026-08-23 23:43:52','2026-08-24 06:44:48','2026-08-25 22:44:48'),(38,'Test ticket','Created from pytest','Medium','Medium','Closed',3,1,'2026-08-23 22:46:10','2026-08-23 23:50:33','2026-08-24 06:46:11','2026-08-25 22:46:11'),(42,'Software reloading','Software reloading in 10 sec','Medium','Medium','Open',7,2,'2026-08-23 23:31:20','2026-08-23 23:31:20','2026-08-24 07:31:20','2026-08-25 23:31:20'),(43,'PC not turning On','My PC is not turning on .Power supply is working CPU not turning on','Medium','Medium','Assigned',4,1,'2026-08-24 11:58:13','2026-08-24 11:58:35','2026-08-24 19:58:14','2026-08-26 11:58:14'),(44,'Network Slow','Wifi speed is Slow','Medium','Medium','Assigned',8,3,'2026-08-24 12:00:04','2026-08-24 12:00:36','2026-08-24 20:00:05','2026-08-26 12:00:05'),(45,'Email Not Sent','Hr email address is wrong','Critical','High','Assigned',8,4,'2026-08-24 14:27:25','2026-08-24 14:28:40','2026-08-24 15:27:25','2026-08-24 18:27:25'),(46,'Unable to access Portal','Cannot access Login portal','Medium','Medium','Assigned',8,5,'2026-08-25 19:19:43','2026-08-25 19:24:31','2026-08-26 03:19:43','2026-08-27 19:19:43');
/*!40000 ALTER TABLE `tickets` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `email` varchar(150) NOT NULL,
  `password` varchar(255) NOT NULL,
  `role_id` int NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`),
  KEY `role_id` (`role_id`),
  CONSTRAINT `users_ibfk_1` FOREIGN KEY (`role_id`) REFERENCES `roles` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'user 1','user@email.com','$2b$12$8XHYwUzHN4GHjGuUydvGae4lTYNxWwKhqJqiK.nwtkcn7MtyYKoxi',1,1),(2,'user3','user3@email.com','$2b$12$wUH6/Gf6rmHqPXJhsnu/ReyWozRuyIr.RQpOnqn2zjjHA0iARZFmW',1,1),(3,'user4','user4@email.com','$2b$12$pJtUnOzZi2XHHyeakZ75hOzWqtFC4sO/gl1EZrZhAz1ZSCAMCjkDK',1,1),(4,'System Admin','admin@servicedesk.com','$2b$12$PzWGir4bHKeJ8nrNpqP35OItY6nbylTvoKAoJWBaBCUZ7eTCUmL6.',3,1),(5,'Support Agent','support1@email.com','$2b$12$B5ByK3gzIQSyr0jkO61N3ugjdslDB125W0Ef1/8qvEUbrLXG48dem',2,1),(6,'Lokesh','lokesh@email.com','$2b$12$oMJqJ97vodwK8anNbj6BJujGBasdTuB2WNmN.NOU.XPWjz855D4Zm',2,1),(7,'aryan oli','aryan@email.com','$2b$12$4WvD2IdXOsQ7wjLKoxdoOOeIeZM8d/BOoGdPv4G3igwW/SIZsg5UO',1,1),(8,'Employee 1','employee1@email.com','$2b$12$syva6xtXDE2ju17C5XalfuYOWyRF1u284.r1kvM2gbvVH.p27Bcqi',1,1),(9,'Aryan','oliaryan@123.com','$2b$12$S70R18z3pfFcoVOZ97i6SOT62QJ3R8JaudWhX1dCtDkEkPcMyhxBi',2,1);
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2026-08-31 15:49:48
