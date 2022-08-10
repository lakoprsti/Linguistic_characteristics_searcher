from unittest import TestCase
import functions


class TestGetLanguages(TestCase):
    def test_get_languages_english(self):
        expected = [{'primary_key': 'a1', 'phoneme': 'ɒ', 'cons': 0, 'son': 1, 'syll': 1, 'lab': 1, 'round': 1,
                     'coronal': 0, 'ant': None, 'dist': None, 'dorsal': 1, 'high': 0, 'low': 1, 'back': 1,
                     'tense': None, 'phrngl': 1, 'atr': 0, 'voice': 1, 'sg': 0, 'cg': 0, 'cont': 1, 'strid': 0,
                     'lat': 0, 'delrel': 0, 'nasal': 0},
                    {'primary_key': 'a2', 'phoneme': 'ɑ', 'cons': 0, 'son': 1, 'syll': 1, 'lab': 1, 'round': 0,
                     'coronal': 0, 'ant': None, 'dist': None, 'dorsal': 1, 'high': 0, 'low': 1, 'back': 1,
                     'tense': None, 'phrngl': 1, 'atr': 0, 'voice': 1, 'sg': 0, 'cg': 0, 'cont': 1, 'strid': 0,
                     'lat': 0, 'delrel': 0, 'nasal': 0},
                    {'primary_key': 'a4', 'phoneme': 'a', 'cons': 0, 'son': 1,'syll': 1, 'lab': 1, 'round': 0,
                     'coronal': 0, 'ant': None, 'dist': None, 'dorsal': 1, 'high': 0, 'low': 1, 'back': 0,
                     'tense': None, 'phrngl': 1, 'atr': 0, 'voice': 1, 'sg': 0, 'cg': 0, 'cont': 1, 'strid': 0,
                     'lat': 0, 'delrel': 0, 'nasal': 0},
                    {'primary_key': 'a5', 'phoneme': 'æ', 'cons': 0, 'son': 1,'syll': 1, 'lab': 1, 'round': 0,
                     'coronal': 0, 'ant': None, 'dist': None, 'dorsal': 1, 'high': 0, 'low': 1, 'back': 0,
                     'tense': None, 'phrngl': 1, 'atr': 1, 'voice': 1, 'sg': 0, 'cg': 0, 'cont': 1, 'strid': 0,
                     'lat': 0, 'delrel': 0, 'nasal': 0},
                    {'primary_key': 'o1', 'phoneme': 'ʌ', 'cons': 0, 'son': 1, 'syll': 1, 'lab': 1, 'round': 0,
                     'coronal': 0, 'ant': None, 'dist': None, 'dorsal': 1, 'high': 0, 'low': 0, 'back': 1, 'tense': 0,
                     'phrngl': 1, 'atr': 0, 'voice': 1, 'sg': 0, 'cg': 0, 'cont': 1, 'strid': 0, 'lat': 0, 'delrel': 0,
                     'nasal': 0},
                    {'primary_key': 'o2', 'phoneme': 'ɔ', 'cons': 0, 'son': 1, 'syll': 1, 'lab': 1,'round': 1,
                     'coronal': 0, 'ant': None, 'dist': None, 'dorsal': 1, 'high': 0, 'low': 0, 'back': 1, 'tense': 0,
                     'phrngl': 1, 'atr': 0, 'voice': 1, 'sg': 0, 'cg': 0, 'cont': 1, 'strid': 0, 'lat': 0, 'delrel': 0,
                     'nasal': 0},
                    {'primary_key': 'o3', 'phoneme': 'o', 'cons': 0, 'son': 1, 'syll': 1, 'lab': 1,'round': 1,
                     'coronal': 0, 'ant': None, 'dist': None, 'dorsal': 1, 'high': 0, 'low': 0, 'back': 1, 'tense': 1,
                     'phrngl': 1, 'atr': 1, 'voice': 1, 'sg': 0, 'cg': 0, 'cont': 1, 'strid': 0, 'lat': 0, 'delrel': 0,
                     'nasal': 0},
                    {'primary_key': 'e1', 'phoneme': 'ə', 'cons': 0, 'son': 1, 'syll': 1, 'lab': 1, 'round': 0,
                     'coronal': 0, 'ant': None, 'dist': None, 'dorsal': 1, 'high': 0, 'low': 0, 'back': 0, 'tense': 0,
                     'phrngl': 1, 'atr': None, 'voice': 1, 'sg': 0, 'cg': 0, 'cont': 1, 'strid': 0, 'lat': 0,
                     'delrel': 0, 'nasal': 0},
                    {'primary_key': 'e2', 'phoneme': 'e', 'cons': 0, 'son': 1, 'syll': 1, 'lab': 1, 'round': 0,
                     'coronal': 0, 'ant': None, 'dist': None, 'dorsal': 1, 'high': 0, 'low': 0, 'back': 0, 'tense': 1,
                     'phrngl': 1, 'atr': 1, 'voice': 1, 'sg': 0, 'cg': 0, 'cont': 1, 'strid': 0, 'lat': 0, 'delrel': 0,
                     'nasal': 0},
                    {'primary_key': 'e5', 'phoneme': 'ɛ', 'cons': 0, 'son': 1, 'syll': 1, 'lab': 1,'round': 0,
                     'coronal': 0, 'ant': None, 'dist': None, 'dorsal': 1, 'high': 0, 'low': 0, 'back': 0, 'tense': 0,
                     'phrngl': 1, 'atr': 0, 'voice': 1, 'sg': 0, 'cg': 0, 'cont': 1, 'strid': 0, 'lat': 0, 'delrel': 0,
                     'nasal': 0},
                    {'primary_key': 'e7', 'phoneme': 'ɜ', 'cons': 0, 'son': 1, 'syll': 1, 'lab': 1, 'round': 0,
                     'coronal': 0, 'ant': None, 'dist': None, 'dorsal': 1, 'high': 0, 'low': 0, 'back': 0, 'tense': 0,
                     'phrngl': 1, 'atr': 0, 'voice': 1, 'sg': 0, 'cg': 0, 'cont': 1, 'strid': 0, 'lat': 0, 'delrel': 0,
                     'nasal': 0},
                    {'primary_key': 'u2', 'phoneme': 'u', 'cons': 0, 'son': 1, 'syll': 1, 'lab': 1, 'round': 1,
                     'coronal': 0, 'ant': None, 'dist': None, 'dorsal': 1, 'high': 1, 'low': 0, 'back': 1, 'tense': 1,
                     'phrngl': 1, 'atr': 1, 'voice': 1, 'sg': 0, 'cg': 0, 'cont': 1, 'strid': 0, 'lat': 0, 'delrel': 0,
                     'nasal': 0},
                    {'primary_key': 'u3', 'phoneme': 'ʊ', 'cons': 0, 'son': 1, 'syll': 1, 'lab': 1,'round': 1,
                     'coronal': 0, 'ant': None, 'dist': None, 'dorsal': 1, 'high': 1, 'low': 0, 'back': 1, 'tense': 0,
                     'phrngl': 1, 'atr': 0, 'voice': 1, 'sg': 0, 'cg': 0, 'cont': 1, 'strid': 0, 'lat': 0, 'delrel': 0,
                     'nasal': 0},
                    {'primary_key': 'i2', 'phoneme': 'i', 'cons': 0, 'son': 1, 'syll': 1, 'lab': 1,'round': 0,
                     'coronal': 0, 'ant': None, 'dist': None, 'dorsal': 1, 'high': 1, 'low': 0, 'back': 0, 'tense': 1,
                     'phrngl': 1, 'atr': 1, 'voice': 1, 'sg': 0, 'cg': 0, 'cont': 1, 'strid': 0, 'lat': 0, 'delrel': 0,
                     'nasal': 0},
                    {'primary_key': 'i4', 'phoneme': 'ɪ', 'cons': 0, 'son': 1, 'syll': 1, 'lab': 1,'round': 0,
                     'coronal': 0, 'ant': None, 'dist': None, 'dorsal': 1, 'high': 1, 'low': 0, 'back': 0, 'tense': 0,
                     'phrngl': 1, 'atr': 0, 'voice': 1, 'sg': 0, 'cg': 0, 'cont': 1, 'strid': 0, 'lat': 0, 'delrel': 0,
                     'nasal': 0},
                    {'primary_key': 't', 'phoneme': 't', 'cons': 1, 'son': 0, 'syll': 0, 'lab': 0, 'round': None,
                     'coronal': 1, 'ant': 1, 'dist': 0, 'dorsal': 0, 'high': None, 'low': None, 'back': None,
                     'tense': None, 'phrngl': 0, 'atr': None, 'voice': 0, 'sg': 0, 'cg': 0, 'cont': 0, 'strid': 0,
                     'lat': 0, 'delrel': 0, 'nasal': 0},
                    {'primary_key': 'd', 'phoneme': 'd', 'cons': 1, 'son': 0, 'syll': 0, 'lab': 0, 'round': None,
                     'coronal': 1, 'ant': 1, 'dist': 0, 'dorsal': 0, 'high': None, 'low': None, 'back': None,
                     'tense': None, 'phrngl': 0, 'atr': None, 'voice': 1, 'sg': 0, 'cg': 0, 'cont': 0, 'strid': 0,
                     'lat': 0, 'delrel': 0, 'nasal': 0},
                    {'primary_key': 's', 'phoneme': 's', 'cons': 1, 'son': 0,'syll': 0, 'lab': 0, 'round': None,
                     'coronal': 1, 'ant': 1, 'dist': 0, 'dorsal': 0, 'high': None, 'low': None, 'back': None,
                     'tense': None, 'phrngl': 0, 'atr': None, 'voice': 0, 'sg': 0, 'cg': 0, 'cont': 1, 'strid': 1,
                     'lat': 0, 'delrel': 0, 'nasal': 0},
                    {'primary_key': 'z', 'phoneme': 'z', 'cons': 1, 'son': 0,'syll': 0, 'lab': 0, 'round': None,
                     'coronal': 1, 'ant': 1, 'dist': 0, 'dorsal': 0, 'high': None, 'low': None, 'back': None,
                     'tense': None, 'phrngl': 0, 'atr': None, 'voice': 1, 'sg': 0, 'cg': 0, 'cont': 1, 'strid': 1,
                     'lat': 0, 'delrel': 0, 'nasal': 0},
                    {'primary_key': 'thvl', 'phoneme': 'θ', 'cons': 1, 'son': 0, 'syll': 0, 'lab': 0, 'round': None,
                     'coronal': 1, 'ant': 1, 'dist': 0, 'dorsal': 0, 'high': None, 'low': None, 'back': None,
                     'tense': None, 'phrngl': 0, 'atr': None, 'voice': 0, 'sg': 0, 'cg': 0, 'cont': 1, 'strid': 0,
                     'lat': 0, 'delrel': 0, 'nasal': 0},
                    {'primary_key': 'thv', 'phoneme': 'ð', 'cons': 1, 'son': 0, 'syll': 0, 'lab': 0, 'round': None,
                     'coronal': 1, 'ant': 1, 'dist': 0, 'dorsal': 0, 'high': None, 'low': None, 'back': None,
                     'tense': None, 'phrngl': 0, 'atr': None, 'voice': 1, 'sg': 0, 'cg': 0, 'cont': 1, 'strid': 0,
                     'lat': 0, 'delrel': 0, 'nasal': 0},
                    {'primary_key': 'h', 'phoneme': 'h', 'cons': 0, 'son': 0, 'syll': 0, 'lab': 0, 'round': None,
                     'coronal': 0, 'ant': None, 'dist': None, 'dorsal': 0, 'high': None, 'low': None, 'back': None,
                     'tense': None, 'phrngl': 0, 'atr': None, 'voice': 0, 'sg': 1, 'cg': 0, 'cont': 1, 'strid': 0,
                     'lat': 0, 'delrel': 0, 'nasal': 0},
                    {'primary_key': 'sh', 'phoneme': 'ʃ', 'cons': 1, 'son': 0, 'syll': 0, 'lab': 0, 'round': None,
                     'coronal': 1, 'ant': 0, 'dist': 0, 'dorsal': 0, 'high': None, 'low': None, 'back': None,
                     'tense': None, 'phrngl': 0, 'atr': None, 'voice': 0, 'sg': 0, 'cg': 0, 'cont': 1, 'strid': 0,
                     'lat': 0, 'delrel': 0, 'nasal': 0},
                    {'primary_key': 'zh', 'phoneme': 'ʒ', 'cons': 1, 'son': 0,'syll': 0, 'lab': 0, 'round': None,
                     'coronal': 1, 'ant': 0, 'dist': 0, 'dorsal': 0, 'high': None, 'low': None, 'back': None,
                     'tense': None, 'phrngl': 0, 'atr': None, 'voice': 1, 'sg': 0, 'cg': 0, 'cont': 1, 'strid': 0,
                     'lat': 0, 'delrel': 0, 'nasal': 0},
                    {'primary_key': 'p', 'phoneme': 'p', 'cons': 1, 'son': 0,'syll': 0, 'lab': 1, 'round': 0,
                     'coronal': 0, 'ant': None, 'dist': None, 'dorsal': 0, 'high': None, 'low': None, 'back': None,
                     'tense': None, 'phrngl': 0, 'atr': None, 'voice': 0, 'sg': 0, 'cg': 0, 'cont': 0, 'strid': 0,
                     'lat': 0, 'delrel': 0, 'nasal': 0},
                    {'primary_key': 'b', 'phoneme': 'b', 'cons': 1, 'son': 0,'syll': 0, 'lab': 1, 'round': 0,
                     'coronal': 0, 'ant': None, 'dist': None, 'dorsal': 0, 'high': None, 'low': None, 'back': None,
                     'tense': None, 'phrngl': 0, 'atr': None, 'voice': 1, 'sg': 0, 'cg': 0, 'cont': 0, 'strid': 0,
                     'lat': 0, 'delrel': 0, 'nasal': 0},
                    {'primary_key': 'f', 'phoneme': 'f', 'cons': 1, 'son': 0, 'syll': 0, 'lab': 1, 'round': 0,
                     'coronal': 0, 'ant': None, 'dist': None, 'dorsal': 0, 'high': None, 'low': None, 'back': None,
                     'tense': None, 'phrngl': 0, 'atr': None, 'voice': 0, 'sg': 0, 'cg': 0, 'cont': 1, 'strid': 1,
                     'lat': 0, 'delrel': 0, 'nasal': 0},
                    {'primary_key': 'v', 'phoneme': 'v', 'cons': 1, 'son': 0,'syll': 0, 'lab': 1, 'round': 0,
                     'coronal': 0, 'ant': None, 'dist': None, 'dorsal': 0, 'high': None, 'low': None, 'back': None,
                     'tense': None, 'phrngl': 0, 'atr': None, 'voice': 1, 'sg': 0, 'cg': 0, 'cont': 1, 'strid': 1,
                     'lat': 0, 'delrel': 0, 'nasal': 0},
                    {'primary_key': 'k', 'phoneme': 'k', 'cons': 1, 'son': 0, 'syll': 0, 'lab': 0, 'round': None,
                     'coronal': 0, 'ant': None, 'dist': None, 'dorsal': 1, 'high': 1, 'low': 0, 'back': 1, 'tense': 0,
                     'phrngl': 0, 'atr': None, 'voice': 0, 'sg': 0, 'cg': 0, 'cont': 0, 'strid': 0, 'lat': 0,
                     'delrel': 0, 'nasal': 0},
                    {'primary_key': 'g', 'phoneme': 'g', 'cons': 1, 'son': 0, 'syll': 0,'lab': 0, 'round': None,
                     'coronal': 0, 'ant': None, 'dist': None, 'dorsal': 1, 'high': 1, 'low': 0, 'back': 1, 'tense': 0,
                     'phrngl': 0, 'atr': None, 'voice': 1, 'sg': 0, 'cg': 0, 'cont': 0, 'strid': 0, 'lat': 0,
                     'delrel': 0, 'nasal': 0},
                    {'primary_key': 'tsh', 'phoneme': 't͡ʃ', 'cons': 1, 'son': 0, 'syll': 0, 'lab': 0, 'round': None,
                     'coronal': 1, 'ant': 0, 'dist': 1, 'dorsal': 1, 'high': 1, 'low': 0, 'back': 0, 'tense': 0,
                     'phrngl': 0, 'atr': None, 'voice': 0, 'sg': 0, 'cg': 0, 'cont': None, 'strid': 1, 'lat': 0,
                     'delrel': 1, 'nasal': 0},
                    {'primary_key': 'dzh', 'phoneme': 'd͡ʒ', 'cons': 1, 'son': 0, 'syll': 0, 'lab': 0, 'round': None,
                     'coronal': 1, 'ant': 0, 'dist': 1, 'dorsal': 1, 'high': 1, 'low': 0, 'back': 0, 'tense': 0,
                     'phrngl': 0, 'atr': None, 'voice': 1, 'sg': 0, 'cg': 0, 'cont': None, 'strid': 1, 'lat': 0,
                     'delrel': 1, 'nasal': 0},
                    {'primary_key': 'm', 'phoneme': 'm', 'cons': 1, 'son': 1, 'syll': 0, 'lab': 0, 'round': 0,
                     'coronal': 0, 'ant': None, 'dist': None, 'dorsal': 0, 'high': None, 'low': None, 'back': None,
                     'tense': None, 'phrngl': 0, 'atr': None, 'voice': 1, 'sg': 0, 'cg': 0, 'cont': 0, 'strid': 0,
                     'lat': 0, 'delrel': 0, 'nasal': 1},
                    {'primary_key': 'n', 'phoneme': 'n', 'cons': 1, 'son': 1, 'syll': 0, 'lab': 0, 'round': None,
                     'coronal': 1, 'ant': 1, 'dist': 0, 'dorsal': 0, 'high': None, 'low': None, 'back': None,
                     'tense': None, 'phrngl': 0, 'atr': None, 'voice': 1, 'sg': 0, 'cg': 0, 'cont': 0, 'strid': 0,
                     'lat': 0, 'delrel': 0, 'nasal': 1},
                    {'primary_key': 'n2', 'phoneme': 'ŋ', 'cons': 1, 'son': 1, 'syll': 0, 'lab': 0, 'round': None,
                     'coronal': 0, 'ant': None, 'dist': None, 'dorsal': 1, 'high': 1, 'low': 0, 'back': 1, 'tense': 0,
                     'phrngl': 0, 'atr': None, 'voice': 1, 'sg': 0, 'cg': 0, 'cont': 0, 'strid': 0, 'lat': 0,
                     'delrel': 0, 'nasal': 1},
                    {'primary_key': 'l', 'phoneme': 'l', 'cons': 1, 'son': 1, 'syll': 0, 'lab': 0, 'round': None,
                     'coronal': 1, 'ant': 1, 'dist': 0, 'dorsal': 0, 'high': None, 'low': None, 'back': None,
                     'tense': None, 'phrngl': 0, 'atr': None, 'voice': 1, 'sg': 0, 'cg': 0, 'cont': 1, 'strid': 0,
                     'lat': 1, 'delrel': 0, 'nasal': 0},
                    {'primary_key': 'r', 'phoneme': 'r', 'cons': 1, 'son': 1,'syll': 0, 'lab': 0, 'round': None,
                     'coronal': 1, 'ant': 1, 'dist': 0, 'dorsal': 0, 'high': None, 'low': None, 'back': None,
                     'tense': None, 'phrngl': 0, 'atr': None, 'voice': 1, 'sg': 0, 'cg': 0, 'cont': 1, 'strid': 0,
                     'lat': 0, 'delrel': 0, 'nasal': 0},
                    {'primary_key': 'j', 'phoneme': 'j', 'cons': 0, 'son': 1, 'syll': 0, 'lab': 0, 'round': 0,
                     'coronal': 0, 'ant': None, 'dist': None, 'dorsal': 1, 'high': 1, 'low': 0, 'back': 0, 'tense': 0,
                     'phrngl': 0, 'atr': None, 'voice': 1, 'sg': 0, 'cg': 0, 'cont': 1, 'strid': 0, 'lat': 0,
                     'delrel': 0, 'nasal': 0},
                    {'primary_key': 'w', 'phoneme': 'w', 'cons': 0, 'son': 1, 'syll': 0, 'lab': 0, 'round': 1,
                     'coronal': 0, 'ant': None, 'dist': None, 'dorsal': 1, 'high': 1, 'low': 0, 'back': 1, 'tense': 0,
                     'phrngl': 0, 'atr': None, 'voice': 1, 'sg': 0, 'cg': 0, 'cont': 1, 'strid': 0, 'lat': 0,
                     'delrel': 0, 'nasal': 0}]
        language = "en"
        result = functions.get_languages(language)
        self.assertEqual(expected, result)

    def test_get_languages_error(self):
        with self.assertRaises(functions.LanguageNotFoundError):
            functions.find_other_phonemes("gr")


class TestFindOtherPhonemes(TestCase):

    def test_find_other_phonemes(self):
        expected = ["s", "z", "f", "v"]
        language = "en"
        comm_feat = {'nasal': 0, 'dorsal': 0, 'tense': None, 'sg': 0, 'high': None, 'cont': 1, 'syll': 0,
                    'phrngl': 0, 'lat': 0, 'delrel': 0, 'son': 0, 'back': None, 'atr': None, 'low': None, 'cg': 0,
                    'strid': 1, 'cons': 1}
        table = functions.get_languages(language)
        result = functions.find_other_phonemes(comm_feat, table)
        self.assertEqual(expected, result)

    def test_find_other_phonemes_2(self):
        expected = ["s", "z"]
        language = "en"
        comm_feat = {'son': 0, 'cg': 0, 'nasal': 0, 'lat': 0, 'high': None, 'back': None, 'atr': None, 'dorsal': 0,
                    'syll': 0, 'lab': 0, 'low': None, 'strid': 1, 'round': None, 'tense': None, 'coronal': 1,
                    'ant': 1,'phrngl': 0, 'delrel': 0, 'dist': 0, 'cons': 1, 'sg': 0, 'cont': 1}
        table = functions.get_languages(language)
        result = functions.find_other_phonemes(comm_feat, table)
        self.assertEqual(expected, result)

    def test_find_other_phonemes_spanish(self):
        expected = ["p", "b", "f"]
        language = "sp"
        comm_feat = {'high': None, 'dorsal': 0, 'phrngl': 0, 'dist': None, 'low': None, 'syll': 0, 'lab': 1,
                     'delrel': 0, 'round': 0, 'ant': None, 'tense': None, 'cg': 0, 'coronal': 0, 'cons': 1, 'sg': 0,
                     'atr': None, 'nasal': 0, 'son': 0, 'lat': 0, 'back': None}
        table = functions.get_languages(language)
        result = functions.find_other_phonemes(comm_feat, table)
        self.assertEqual(expected, result)

    def test_find_other_phonemes_english(self):
        expected = ["p", "b", "f", "v"]
        language = "en"
        comm_feat = {'nasal': 0, 'son': 0, 'sg': 0, 'round': 0, 'syll': 0, 'coronal': 0, 'ant': None, 'cons': 1,
                     'cg': 0, 'lab': 1, 'tense': None, 'dorsal': 0, 'high': None, 'phrngl': 0, 'low': None,
                     'back': None, 'dist': None, 'lat': 0, 'delrel': 0, 'atr': None}
        table = functions.get_languages(language)
        result = functions.find_other_phonemes(comm_feat, table)
        self.assertEqual(expected, result)

    def test_find_other_phonemes_one_phoneme(self):
        expected = ["s"]
        language = "en"
        comm_feat = {'cons': 1, 'son': 0, 'syll': 0, 'lab': 0, 'round': None, 'coronal': 1, 'ant': 1, 'dist': 0,
                     'dorsal': 0, 'high': None, 'low': None, 'back': None, 'tense': None, 'phrngl': 0, 'atr': None,
                     'voice': 0, 'sg': 0, 'cg': 0, 'cont': 1, 'strid': 1, 'lat': 0, 'delrel': 0, 'nasal': 0}
        table = functions.get_languages(language)
        result = functions.find_other_phonemes(comm_feat, table)
        self.assertEqual(expected, result)

    def test_find_other_phonemes_error_1(self):
        language = "en"
        comm_feat = [{'cons': 1, 'son': 0, 'syll': 0, 'lab': 0, 'round': None, 'coronal': 1, 'ant': 1, 'dist': 0,
                     'dorsal': 0, 'high': None, 'low': None, 'back': None, 'tense': None, 'phrngl': 0, 'atr': None,
                     'voice': 0, 'sg': 0, 'cg': 0, 'cont': 1, 'strid': 1, 'lat': 0, 'delrel': 0, 'nasal': 0}]
        table = functions.get_languages(language)
        with self.assertRaises(TypeError):
            functions.find_other_phonemes(comm_feat, table)

    def test_find_other_phonemes_error_2(self):
        comm_feat = {'cons': 1, 'son': 0, 'syll': 0, 'lab': 0, 'round': None, 'coronal': 1, 'ant': 1, 'dist': 0,
                     'dorsal': 0, 'high': None, 'low': None, 'back': None, 'tense': None, 'phrngl': 0, 'atr': None,
                     'voice': 0, 'sg': 0, 'cg': 0, 'cont': 1, 'strid': 1, 'lat': 0, 'delrel': 0, 'nasal': 0}
        table = "table"
        with self.assertRaises(TypeError):
            functions.find_other_phonemes(comm_feat, table)


class TestSmallestCommon(TestCase):

    def test_smallest_common(self):
        all_expected = [{'dorsal': 0, 'strid': 1}, {'strid': 1, 'cont': 1}, {'cont': True, 'strid': True},
                       {'delrel': False, 'strid': True}, {'strid': True, 'dorsal': False},
                       {'strid': True, 'delrel': False}]
        language = "en"
        comm_feat = {'nasal': 0, 'dorsal': 0, 'tense': None, 'sg': 0, 'high': None, 'cont': 1, 'syll': 0,
                    'phrngl': 0, 'lat': 0, 'delrel': 0, 'son': 0, 'back': None, 'atr': None, 'low': None, 'cg': 0,
                    'strid': 1, 'cons': 1}
        phonemes_group = ["s", "z", "f", "v"]
        table = functions.get_languages(language)
        result = functions.smallest_common(comm_feat, phonemes_group, table)
        in_list = False
        print(result)
        if result in all_expected:
            in_list = True
        self.assertTrue(in_list)

    def test_smallest_common_one_phoneme(self):
        expected = {'ant': True, 'voice': False, 'strid': True}
        language = "en"
        comm_feat = {'cons': 1, 'son': 0, 'syll': 0, 'lab': 0, 'round': None, 'coronal': 1, 'ant': 1, 'dist': 0,
                     'dorsal': 0, 'high': None, 'low': None, 'back': None, 'tense': None, 'phrngl': 0, 'atr': None,
                     'voice': 0, 'sg': 0, 'cg': 0, 'cont': 1, 'strid': 1, 'lat': 0, 'delrel': 0, 'nasal': 0}
        phonemes_group = ["s"]
        table = functions.get_languages(language)
        result = functions.smallest_common(comm_feat, phonemes_group, table)
        self.assertEqual(expected, result)

    def test_smallest_common_error_1(self):
        language = "en"
        comm_feat = [{'cons': 1, 'son': 0, 'syll': 0, 'lab': 0, 'round': None, 'coronal': 1, 'ant': 1, 'dist': 0,
                     'dorsal': 0, 'high': None, 'low': None, 'back': None, 'tense': None, 'phrngl': 0, 'atr': None,
                     'voice': 0, 'sg': 0, 'cg': 0, 'cont': 1, 'strid': 1, 'lat': 0, 'delrel': 0, 'nasal': 0}]
        phoneme_group = ["s"]
        table = functions.get_languages(language)
        with self.assertRaises(TypeError):
            functions.smallest_common(comm_feat, phoneme_group, table)

    def test_smallest_common_error_2(self):
        language = "en"
        comm_feat = [{'cons': 1, 'son': 0, 'syll': 0, 'lab': 0, 'round': None, 'coronal': 1, 'ant': 1, 'dist': 0,
                     'dorsal': 0, 'high': None, 'low': None, 'back': None, 'tense': None, 'phrngl': 0, 'atr': None,
                     'voice': 0, 'sg': 0, 'cg': 0, 'cont': 1, 'strid': 1, 'lat': 0, 'delrel': 0, 'nasal': 0}]
        phoneme_group = "s"
        table = functions.get_languages(language)
        with self.assertRaises(TypeError):
            functions.smallest_common(comm_feat, phoneme_group, table)

    def test_smallest_common_error_3(self):
        comm_feat = [{'cons': 1, 'son': 0, 'syll': 0, 'lab': 0, 'round': None, 'coronal': 1, 'ant': 1, 'dist': 0,
                     'dorsal': 0, 'high': None, 'low': None, 'back': None, 'tense': None, 'phrngl': 0, 'atr': None,
                     'voice': 0, 'sg': 0, 'cg': 0, 'cont': 1, 'strid': 1, 'lat': 0, 'delrel': 0, 'nasal': 0}]
        phoneme_group = ["s"]
        table = []
        with self.assertRaises(TypeError):
            functions.smallest_common(comm_feat, phoneme_group, table)


class TestComparePhonemes(TestCase):

    def test_compare_phonemes_features(self):
        all_expected = [({'dorsal': False, 'strid': True}, ['s', 'z', 'f', 'v']),
                    ({'strid': True, 'cont': True}, ['s', 'z', 'f', 'v']),
                    ({'cont': True, 'strid': True}, ['s', 'z', 'f', 'v']),
                    ({'delrel': False, 'strid': True}, ['s', 'z', 'f', 'v']),
                    ({'strid': True, 'dorsal': False}, ['s', 'z', 'f', 'v']),
                    ({'strid': True, 'delrel': False}, ['s', 'z', 'f', 'v'])]
        language = "en"
        result = functions.compare_phonemes(language, "s", "z", "f", "v")
        in_list = False
        print(result)
        if result in all_expected:
            in_list = True
        self.assertTrue(in_list)

    def test_compare_phonemes_features_less(self):
        all_expected = [({'dorsal': False, 'strid': True}, ['s', 'z', 'f', 'v']),
                    ({'strid': True, 'cont': True}, ['s', 'z', 'f', 'v']),
                    ({'cont': True, 'strid': True}, ['s', 'z', 'f', 'v']),
                    ({'delrel': False, 'strid': True}, ['s', 'z', 'f', 'v']),
                    ({'strid': True, 'dorsal': False}, ['s', 'z', 'f', 'v']),
                    ({'strid': True, 'delrel': False}, ['s', 'z', 'f', 'v'])]
        language = "en"
        result = functions.compare_phonemes(language, "s", "z", "f")
        in_list = False
        print(result)
        if result in all_expected:
            in_list = True
        self.assertTrue(in_list)

    def test_compare_phonemes_features_one_phoneme(self):
        expected = ({'ant': True, 'voice': False, 'strid': True}, ['s'])
        language = "en"
        result = functions.compare_phonemes(language, "s")
        self.assertEqual(expected, result)

    def test_compare_phonemes_error_1(self):
        with self.assertRaises(functions.LanguageNotFoundError):
            functions.compare_phonemes("gr", "a1")

    def test_compare_phonemes_error_2(self):
        with self.assertRaises(IndexError):
            functions.compare_phonemes("en", "a")


