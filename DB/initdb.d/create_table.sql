CREATE TABLE equipments_info
(
    `siteId`  VARCHAR(25),
    `perfId`  SMALLINT,
    `eqpCode` VARCHAR(100),
    `eqpName` VARCHAR(100),
    `eqpType` VARCHAR(100),
    `data_time`  datetime  NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (siteId, perfId)
);
CREATE TABLE power_info
(
    `siteId`      VARCHAR(25),
    `pnName`      VARCHAR(25),
    `eqpName`     VARCHAR(25),
    `perfId`      VARCHAR(25),
    `ymdms`       VARCHAR(25),
    `volTage`     VARCHAR(25),
    `amPere`      VARCHAR(25),
    `arPower`     VARCHAR(25),
    `atvPower`    VARCHAR(25),
    `ratPower`    VARCHAR(25),
    `pwFactor`    VARCHAR(25),
    `accruePower` VARCHAR(25),
    `voltagerS`   VARCHAR(25),
    `voltagesT`   VARCHAR(25),
    `voltagetR`   VARCHAR(25),
    `temperature` VARCHAR(25),
    `data_time`  datetime  NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (siteId, perfId, ymdms)
);

