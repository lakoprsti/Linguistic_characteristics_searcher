import mysql.connector
import itertools
from config import USER, HOST, PASSWORD

# exception
class LanguageNotFoundError(Exception):
    pass


# sql connector by Hannah
def connect_to_db(phonlang):
    cnx = mysql.connector.connect(
        host = HOST,
        user = USER,
        password = PASSWORD,
        database = phonlang
    )
    return cnx


def get_languages(language):
    try:
        db_name = 'phonlang'
        db_connection = connect_to_db(db_name)
        cur = db_connection.cursor(dictionary=True)
        print(f"Connected to {db_name}")

        query = f"""SELECT ph.primary_key, ph.phoneme, ph.cons, ph.son, ph.syll, ph.lab, ph.round, ph.coronal, ph.ant,
                ph.dist, ph.dorsal, ph.high, ph.low, ph.back, ph.tense, ph.phrngl, ph.atr, ph.voice, ph.sg, ph.cg,
                ph.cont, ph.strid, ph.lat, ph.delrel, ph.nasal
        FROM phonemechart ph
        JOIN langphons lp
        ON ph.primary_key = lp.phoneme
        JOIN languages lan
        ON lp.language = lan.primary_key
        WHERE lan.primary_key = "{language}";"""
        cur.execute(query)
        result = cur.fetchall()
        print(result)
        cur.close()
        return result

    except TypeError:
        raise LanguageNotFoundError
    except Exception:
        raise ConnectionError("Failed to read data from DB")

    finally:
        if db_connection:
            db_connection.close()
            print("Db connection closed.")


# phoneme comparison by Juli
def find_other_phonemes(common_features, feat_table):
    """Returns the smallest possible group with the specified set of features."""
    if not isinstance(common_features, dict) or not isinstance(feat_table, list):
        raise TypeError
    new_phon_list = []
    for j in range(len(feat_table)):
        if common_features == (dict(common_features.items() & feat_table[j].items())):
            phon = "{}".format(feat_table[j]["primary_key"])
            new_phon_list.append(phon)
    return new_phon_list


def smallest_common(common_feats, phonemes_in_group, feats_table):
    """Finds the smallest group of features that can describe the selected phonemes without overlapping any other."""
    if not isinstance(common_feats, dict) or not isinstance(phonemes_in_group, list) \
            or not isinstance(feats_table, list):
        raise TypeError
    smallest_common_group = []
    smallest_feature_group = {}
    while smallest_common_group != phonemes_in_group:
        for i in range(len(common_feats)):
            if i >= 2:
                for combination in list(map(dict, itertools.combinations(common_feats.items(), i))):
                    smallest_common_group.clear()
                    for k in range(len(feats_table)):
                        count = k
                        if combination == (dict(combination.items() & feats_table[k].items())):
                            phoneme = "{}".format(feats_table[k]["primary_key"])
                            smallest_common_group.append(phoneme)
                        if count == (len(feats_table)-1) and smallest_common_group == phonemes_in_group:
                            smallest_feature_group.update(combination)
                            print(smallest_feature_group)
                            return smallest_feature_group


def compare_phonemes(language, *phonemes):
    """Compares phonemes passed in the function in the given language.
    IMPORTANT! Takes primary_key from SQL database, NOT IPA!!!
    If the phonemes do not form a natural group, the next smallest possible group is given.
    If a phoneme doesn't exist in the specified language it will give the largest possible group
    with the phonemes that exist."""
    table = get_languages(language)
    if len(table) == 0:
        raise LanguageNotFoundError
    phonemes_list = [item for item in phonemes]
    if len(phonemes_list) == 1:
        try:
            features = [phoneme for phoneme in table if phonemes_list[0] == phoneme["primary_key"]]
        except KeyError or IndexError:
            print("Phoneme not found. Please try again.")
        common = dict(features[0].items())
        print(common)
        del common["primary_key"]
        del common["phoneme"]
    else:
        try:
            all_features = []
            for phoneme in table:
                for item in phonemes_list:
                    if item == phoneme["primary_key"]:
                        try:
                            all_features.append(phoneme)
                        except KeyError or IndexError:
                            print("Phoneme not found. Please try again.")
            common = dict(all_features[0].items() & all_features[1].items())
            if len(all_features) > 2:
                for i in range(len(all_features)):
                    common = dict(common.items() & all_features[i].items())
        except ValueError or IndexError:
            print("Invalid input. Please try again.")
    common = {key: value for key, value in common.items() if value is not None}
    all_phonemes = find_other_phonemes(common, table)
    smallest_common_10 = smallest_common(common, all_phonemes, table)
    smallest_common_features = {key: bool(value) for key, value in smallest_common_10.items()}
    return smallest_common_features, all_phonemes