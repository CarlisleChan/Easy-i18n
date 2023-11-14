import os
import argparse
import openai
from dotenv import load_dotenv

load_dotenv()

openai.base_url = os.getenv("OPENAI_BASE_URL")
openai.api_key = os.getenv("OPENAI_API_KEY")

SUPPORTED_LANGUAGES = [
    {'code': 'sq', 'name': 'Albanian', 'android': 'values', 'ios': 'sq.lproj'},
    {'code': 'ar', 'name': 'Arabic', 'android': 'values-ar', 'ios': 'ar.lproj'},
    {'code': 'am', 'name': 'Amharic', 'android': 'values-am', 'ios': 'am.lproj'},
    {'code': 'az', 'name': 'Azerbaijani', 'android': 'values-az', 'ios': 'az.lproj'},
    {'code': 'ga', 'name': 'Irish', 'android': 'values-ga', 'ios': 'ga.lproj'},
    {'code': 'et', 'name': 'Estonian', 'android': 'values-et', 'ios': 'et.lproj'},
    {'code': 'eu', 'name': 'Basque', 'android': 'values-eu', 'ios': 'eu.lproj'},
    {'code': 'be', 'name': 'Belarusian', 'android': 'values-be', 'ios': 'be.lproj'},
    {'code': 'bg', 'name': 'Bulgarian', 'android': 'values-bg', 'ios': 'bg.lproj'},
    {'code': 'is', 'name': 'Icelandic', 'android': 'values-is', 'ios': 'is.lproj'},
    {'code': 'pl', 'name': 'Polish', 'android': 'values-pl', 'ios': 'pl.lproj'},
    {'code': 'bs', 'name': 'Bosnian', 'android': 'values-bs', 'ios': 'bs.lproj'},
    {'code': 'fa', 'name': 'Persian', 'android': 'values-fa', 'ios': 'fa.lproj'},
    {'code': 'af', 'name': 'Afrikaans', 'android': 'values-af', 'ios': 'af.lproj'},
    {'code': 'da', 'name': 'Danish', 'android': 'values-da', 'ios': 'da.lproj'},
    {'code': 'de', 'name': 'German', 'android': 'values-de', 'ios': 'de.lproj'},
    {'code': 'ru', 'name': 'Russian', 'android': 'values-ru', 'ios': 'ru.lproj'},
    {'code': 'fr', 'name': 'French', 'android': 'values-fr', 'ios': 'fr.lproj'},
    {'code': 'fil', 'name': 'Filipino', 'android': 'values-tl', 'ios': 'fil.lproj'},
    {'code': 'fi', 'name': 'Finnish', 'android': 'values-fi', 'ios': 'fi.lproj'},
    {'code': 'fy', 'name': 'Frisian', 'android': 'values-fy', 'ios': 'fy.lproj'},
    {'code': 'km', 'name': 'Khmer', 'android': 'values-km', 'ios': 'km.lproj'},
    {'code': 'ka', 'name': 'Georgian', 'android': 'values-ka', 'ios': 'ka.lproj'},
    {'code': 'gu', 'name': 'Gujarati', 'android': 'values-gu', 'ios': 'gu.lproj'},
    {'code': 'kk', 'name': 'Kazakh', 'android': 'values-kk', 'ios': 'kk.lproj'},
    {'code': 'ht', 'name': 'Haitian Creole', 'android': 'values-ht', 'ios': 'ht.lproj'},
    {'code': 'ko', 'name': 'Korean', 'android': 'values-ko', 'ios': 'ko.lproj'},
    {'code': 'ha', 'name': 'Hausa', 'android': 'values-ha', 'ios': 'ha.lproj'},
    {'code': 'nl', 'name': 'Dutch', 'android': 'values-nl', 'ios': 'nl.lproj'},
    {'code': 'ky', 'name': 'Kyrgyz', 'android': 'values-ky', 'ios': 'ky.lproj'},
    {'code': 'gl', 'name': 'Galician', 'android': 'values-gl', 'ios': 'gl.lproj'},
    {'code': 'ca', 'name': 'Catalan', 'android': 'values-ca', 'ios': 'ca.lproj'},
    {'code': 'cs', 'name': 'Czech', 'android': 'values-cs', 'ios': 'cs.lproj'},
    {'code': 'kn', 'name': 'Kannada', 'android': 'values-kn', 'ios': 'kn.lproj'},
    {'code': 'co', 'name': 'Corsican', 'android': 'values-co', 'ios': 'co.lproj'},
    {'code': 'hr', 'name': 'Croatian', 'android': 'values-hr', 'ios': 'hr.lproj'},
    {'code': 'ku', 'name': 'Kurdish', 'android': 'values-ku', 'ios': 'ku.lproj'},
    {'code': 'la', 'name': 'Latin', 'android': 'values-la', 'ios': 'la.lproj'},
    {'code': 'lv', 'name': 'Latvian', 'android': 'values-lv', 'ios': 'lv.lproj'},
    {'code': 'lo', 'name': 'Lao', 'android': 'values-lo', 'ios': 'lo.lproj'},
    {'code': 'lt', 'name': 'Lithuanian', 'android': 'values-lt', 'ios': 'lt.lproj'},
    {'code': 'lb', 'name': 'Luxembourgish', 'android': 'values-lb', 'ios': 'lb.lproj'},
    {'code': 'ro', 'name': 'Romanian', 'android': 'values-ro', 'ios': 'ro.lproj'},
    {'code': 'mg', 'name': 'Malagasy', 'android': 'values-mg', 'ios': 'mg.lproj'},
    {'code': 'mt', 'name': 'Maltese', 'android': 'values-mt', 'ios': 'mt.lproj'},
    {'code': 'mr', 'name': 'Marathi', 'android': 'values-mr', 'ios': 'mr.lproj'},
    {'code': 'ml', 'name': 'Malayalam', 'android': 'values-ml', 'ios': 'ml.lproj'},
    {'code': 'ms', 'name': 'Malay', 'android': 'values-ms', 'ios': 'ms.lproj'},
    {'code': 'mk', 'name': 'Macedonian', 'android': 'values-mk', 'ios': 'mk.lproj'},
    {'code': 'mi', 'name': 'Maori', 'android': 'values-mi', 'ios': 'mi.lproj'},
    {'code': 'mn', 'name': 'Mongolian', 'android': 'values-mn', 'ios': 'mn.lproj'},
    {'code': 'bn', 'name': 'Bangla', 'android': 'values-bn', 'ios': 'bn.lproj'},
    {'code': 'my', 'name': 'Burmese', 'android': 'values-my', 'ios': 'my.lproj'},
    {'code': 'hmn', 'name': 'Hmong', 'android': 'values-hmn', 'ios': 'hmn.lproj'},
    {'code': 'xh', 'name': 'Xhosa', 'android': 'values-xh', 'ios': 'xh.lproj'},
    {'code': 'zu', 'name': 'Zulu', 'android': 'values-zu', 'ios': 'zu.lproj'},
    {'code': 'ne', 'name': 'Nepali', 'android': 'values-ne', 'ios': 'ne.lproj'},
    {'code': 'no', 'name': 'Norwegian', 'android': 'values-no', 'ios': 'no.lproj'},
    {'code': 'pa', 'name': 'Punjabi', 'android': 'values-pa', 'ios': 'pa.lproj'},
    {'code': 'pt', 'name': 'Portuguese', 'android': 'values-pt', 'ios': 'pt.lproj'},
    {'code': 'ps', 'name': 'Pashto', 'android': 'values-ps', 'ios': 'ps.lproj'},
    {'code': 'ny', 'name': 'Chichewa', 'android': 'values-ny', 'ios': 'ny.lproj'},
    {'code': 'ja', 'name': 'Japanese', 'android': 'values-ja', 'ios': 'ja.lproj'},
    {'code': 'sv', 'name': 'Swedish', 'android': 'values-sv', 'ios': 'sv.lproj'},
    {'code': 'sm', 'name': 'Samoan', 'android': 'values-sm', 'ios': 'sm.lproj'},
    {'code': 'sr', 'name': 'Serbian', 'android': 'values-sr', 'ios': 'sr.lproj'},
    {'code': 'st', 'name': 'Sotho', 'android': 'values-st', 'ios': 'st.lproj'},
    {'code': 'si', 'name': 'Sinhala', 'android': 'values-si', 'ios': 'si.lproj'},
    {'code': 'eo', 'name': 'Esperanto', 'android': 'values-eo', 'ios': 'eo.lproj'},
    {'code': 'sk', 'name': 'Slovak', 'android': 'values-sk', 'ios': 'sk.lproj'},
    {'code': 'sl', 'name': 'Slovenian', 'android': 'values-sl', 'ios': 'sl.lproj'},
    {'code': 'sw', 'name': 'Swahili', 'android': 'values-sw', 'ios': 'sw.lproj'},
    {'code': 'gd', 'name': 'Scottish Gaelic', 'android': 'values-gd', 'ios': 'gd.lproj'},
    {'code': 'ceb', 'name': 'Cebuano', 'android': 'values-ceb', 'ios': 'ceb.lproj'},
    {'code': 'so', 'name': 'Somali', 'android': 'values-so', 'ios': 'so.lproj'},
    {'code': 'tg', 'name': 'Tajik', 'android': 'values-tg', 'ios': 'tg.lproj'},
    {'code': 'te', 'name': 'Telugu', 'android': 'values-te', 'ios': 'te.lproj'},
    {'code': 'ta', 'name': 'Tamil', 'android': 'values-ta', 'ios': 'ta.lproj'},
    {'code': 'th', 'name': 'Thai', 'android': 'values-th', 'ios': 'th.lproj'},
    {'code': 'tr', 'name': 'Turkish', 'android': 'values-tr', 'ios': 'tr.lproj'},
    {'code': 'cy', 'name': 'Welsh', 'android': 'values-cy', 'ios': 'cy.lproj'},
    {'code': 'ur', 'name': 'Urdu', 'android': 'values-ur', 'ios': 'ur.lproj'},
    {'code': 'uk', 'name': 'Ukrainian', 'android': 'values-uk', 'ios': 'uk.lproj'},
    {'code': 'uz', 'name': 'Uzbek', 'android': 'values-uz', 'ios': 'uz.lproj'},
    {'code': 'es', 'name': 'Spanish', 'android': 'values-es', 'ios': 'es.lproj'},
    {'code': 'iw', 'name': 'Hebrew', 'android': 'values-iw', 'ios': 'he.lproj'},
    {'code': 'el', 'name': 'Greek', 'android': 'values-el', 'ios': 'el.lproj'},
    {'code': 'haw', 'name': 'Hawaiian', 'android': 'values-haw', 'ios': 'haw.lproj'},
    {'code': 'sd', 'name': 'Sindhi', 'android': 'values-sd', 'ios': 'sd.lproj'},
    {'code': 'hu', 'name': 'Hungarian', 'android': 'values-hu', 'ios': 'hu.lproj'},
    {'code': 'sn', 'name': 'Shona', 'android': 'values-sn', 'ios': 'sn.lproj'},
    {'code': 'hy', 'name': 'Armenian', 'android': 'values-hy', 'ios': 'hy.lproj'},
    {'code': 'ig', 'name': 'Igbo', 'android': 'values-ig', 'ios': 'ig.lproj'},
    {'code': 'it', 'name': 'Italian', 'android': 'values-it', 'ios': 'it.lproj'},
    {'code': 'yi', 'name': 'Yiddish', 'android': 'values-yi', 'ios': 'yi.lproj'},
    {'code': 'hi', 'name': 'Hindi', 'android': 'values-hi', 'ios': 'hi.lproj'},
    {'code': 'su', 'name': 'Sundanese', 'android': 'values-su', 'ios': 'su.lproj'},
    {'code': 'in-rID', 'name': 'Indonesian', 'android': 'values-in-rID', 'ios': 'id.lproj'},
    {'code': 'jv', 'name': 'Javanese', 'android': 'values-jv', 'ios': 'jv.lproj'},
    {'code': 'en', 'name': 'English', 'android': 'values', 'ios': 'en.lproj'},
    {'code': 'yo', 'name': 'Yoruba', 'android': 'values-yo', 'ios': 'yo.lproj'},
    {'code': 'vi', 'name': 'Vietnamese', 'android': 'values-vi', 'ios': 'vi.lproj'},
    {'code': 'zh-rTW', 'name': 'Chinese Traditional', 'android': 'values-zh-rTW', 'ios': 'zh-Hant.lproj'},
    {'code': 'zh-rCN', 'name': 'Chinese Simplified', 'android': 'values-zh-rCN', 'ios': 'zh-Hans.lproj'},
    {'code': 'as', 'name': 'Assamese', 'android': 'values-as', 'ios': 'as.lproj'},
    {'code': 'prs', 'name': 'Dari', 'android': 'values-prs', 'ios': 'prs.lproj'},
    {'code': 'fj', 'name': 'Fijian', 'android': 'values-fj', 'ios': 'fj.lproj'},
    {'code': 'mww', 'name': 'Hmong Daw', 'android': 'values-mww', 'ios': 'mww.lproj'},
    {'code': 'iu', 'name': 'Inuktitut', 'android': 'values-iu', 'ios': 'iu.lproj'},
    {'code': 'tlh-Latn', 'name': 'Klingon (Latin)', 'android': 'values-tlh-Latn', 'ios': 'tlh-Latn.lproj'},
    {'code': 'tlh-Piqd', 'name': 'Klingon (pIqaD)', 'android': 'values-tlh-Piqd', 'ios': 'tlh-Piqd.lproj'},
    {'code': 'or', 'name': 'Odia', 'android': 'values-or', 'ios': 'or.lproj'},
    {'code': 'otq', 'name': 'Querétaro Otomi', 'android': 'values-otq', 'ios': 'otq.lproj'},
    {'code': 'ty', 'name': 'Tahitian', 'android': 'values-ty', 'ios': 'ty.lproj'},
    {'code': 'ti', 'name': 'Tigrinya', 'android': 'values-ti', 'ios': 'ti.lproj'},
    {'code': 'to', 'name': 'Tongan', 'android': 'values-to', 'ios': 'to.lproj'},
    {'code': 'yua', 'name': 'Yucatec Maya', 'android': 'values-yua', 'ios': 'yua.lproj'},
    # Add more languages with corresponding Android and iOS configurations as needed
]

def translate_text(source_text, target_lang, platform):
    prompt = f'''
        Translate the content of the {platform} platform's string resource file into {target_lang['name']}. 
        Please provide a concise and to-the-point response, adhering to the format specific to the platform. 
        No need for explanations, just output the result.
    '''
    
    completion = openai.chat.completions.create(
        model=os.getenv("OPENAI_MODEL"),
        messages=[
            {"role": "system", "content": prompt},
            {"role": "user", "content": source_text}
        ]
    )
    return completion.choices[0].message.content

def generate_files(source_path, selected_langs, excluded_langs, platform):
    source_content = open(source_path, 'r', encoding='utf-8').read()

    output_folder = "output"
    total_languages = len([lang for lang in SUPPORTED_LANGUAGES if lang['code'] not in excluded_langs and (not selected_langs or lang['code'] in selected_langs)])
    current_language = 0

    for lang in SUPPORTED_LANGUAGES:
        lang_code, lang_name, android_folder, ios_folder = lang['code'], lang['name'], lang['android'], lang['ios']

        if lang_code in excluded_langs or (selected_langs and lang_code not in selected_langs):
            continue

        translated_content = translate_text(source_content, lang, platform)
        output_folder_platform = os.path.join(output_folder, platform.lower(), android_folder if platform.lower() == "android" else ios_folder)

        os.makedirs(output_folder_platform, exist_ok=True)
        output_file = os.path.join(output_folder_platform, 'strings.xml' if platform.lower() == "android" else 'Localizable.strings')

        with open(output_file, 'w', encoding='utf-8') as output_file_platform:
            output_file_platform.write(translated_content)

        current_language += 1
        print(f"Translation for {lang_name} completed. Output saved to {output_file} ({current_language}/{total_languages})")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate app language files.")
    parser.add_argument("source_path", type=str, help="Source file path for translation.")
    parser.add_argument("--languages", type=str, default="", help="Selected languages (comma-separated).")
    parser.add_argument("--exclude", type=str, default="", help="Excluded languages (comma-separated).")
    parser.add_argument("--platform", type=str, default="android", help="Selected platform ('android' or 'ios'). Default is 'android'.")

    args = parser.parse_args()

    selected_langs = args.languages.split(',') if args.languages else []
    excluded_langs = args.exclude.split(',') if args.exclude else []
    
    generate_files(args.source_path, selected_langs, excluded_langs, args.platform)
