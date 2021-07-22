SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

CREATE TABLE IF NOT EXISTS 'team' (
  `TEAM_ID` CHAR(20) NOT NULL COMMENT '',
  PRIMARY KEY (`TEAM_ID`)  COMMENT '')
ENGINE = InnoDB;


CREATE TABLE IF NOT EXISTS `task` (
  `TASK_ID` CHAR(20) NOT NULL COMMENT '',
  `SKILL` CHAR(20) NOT NULL COMMENT '',
  PRIMARY KEY (`TASK_ID`)  COMMENT '')
ENGINE = InnoDB;


CREATE TABLE IF NOT EXISTS `team_skill` (
  `TEAM_ID` CHAR(20) NOT NULL COMMENT '',
  `SKILL` CHAR(20) NOT NULL COMMENT '',
  CONSTRAINT 'FK_TEAM_ID'
    FOREIGN KEY ('TEAM_ID')
    REFERENCES 'team' ('TEAM_ID')
    ON DELETE CASCADE
    ON UPDATE CASCADE)   
ENGINE = InnoDB;

CREATE INDEX `FK_TEAM_ID_IDx` ON `team_skill` (`TEAM_ID` ASC)  COMMENT '';


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
