USE phonlang;

-- select all phonemes of a language
DELIMITER //
CREATE PROCEDURE sel_language
(
	IN lang VARCHAR(5)
)
BEGIN
	DROP TEMPORARY TABLE IF EXISTS temp_tab;
	CREATE TEMPORARY TABLE temp_tab(
	  primary_key VARCHAR(4) NOT NULL PRIMARY KEY,
	  phoneme     VARCHAR(5) NOT NULL,
	  cons        BOOLEAN  NOT NULL,
	  son         BOOLEAN  NOT NULL,
	  syll        BOOLEAN  NOT NULL,
	  lab         BOOLEAN  NOT NULL,
	  round       BOOLEAN,
	  coronal     BOOLEAN NOT NULL,
	  ant         BOOLEAN, 
	  dist        BOOLEAN,
	  dorsal      BOOLEAN NOT NULL,
	  high        BOOLEAN,
	  low         BOOLEAN, 
	  back        BOOLEAN, 
	  tense       BOOLEAN, 
	  phrngl      BOOLEAN NOT NULL,
	  atr         BOOLEAN,
	  voice       BOOLEAN NOT NULL,
	  sg          BOOLEAN NOT NULL,
	  cg          BOOLEAN NOT NULL,
	  cont        BOOLEAN,
	  strid       BOOLEAN NOT NULL,
	  lat         BOOLEAN NOT NULL,
	  delrel      BOOLEAN NOT NULL,
	  nasal       BOOLEAN NOT NULL      
	);
    INSERT INTO temp_tab 
		SELECT ph.primary_key, ph.phoneme, ph.cons, ph.son, ph.syll, ph.lab, ph.round, ph.coronal, ph.ant, ph.dist, ph.dorsal,
			   ph.high, ph.low, ph.back, ph.tense, ph.phrngl, ph.atr, ph.voice, ph.sg, ph.cg, ph.cont, ph.strid, ph.lat, ph.delrel,
               ph.nasal
		FROM phonemechart ph
		JOIN langphons lp
		ON ph.primary_key = lp.phoneme
		JOIN languages lan
		ON lp.language = lan.primary_key
		WHERE lan.primary_key = lang;
    
END//
DELIMITER ;

/*
query on its own (example english)
SELECT ph.primary_key, ph.phoneme, ph.cons, ph.son, ph.syll, ph.lab, ph.round, ph.coronal, ph.ant, ph.dist, ph.dorsal,
	   ph.high, ph.low, ph.back, ph.tense, ph.phrngl, ph.atr, ph.voice, ph.sg, ph.cg, ph.cont, ph.strid, ph.lat, ph.delrel,
       ph.nasal
FROM phonemechart ph
JOIN langphons lp
ON ph.primary_key = lp.phoneme
JOIN languages lan
ON lp.language = lan.primary_key
WHERE lan.primary_key = "en";
*/
        
-- example usage
CALL sel_language("en");
SELECT * from temp_tab;
