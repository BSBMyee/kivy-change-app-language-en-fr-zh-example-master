.PHONY: po mo

po:
    #gettext
	xgettext -Lpython --keyword=tr:1 --output=messages.pot main.py lang.kv
	msgmerge --update --no-fuzzy-matching --backup=off po/en.po messages.pot
	msgmerge --update --no-fuzzy-matching --backup=off po/fr.po messages.pot
	msgmerge --update --no-fuzzy-matching --backup=off po/zh_hant.po messages.pot

	mkdir -p data/locales/en/LC_MESSAGES
	mkdir -p data/locales/fr/LC_MESSAGES
	mkdir -p data/locales/zh_hant/LC_MESSAGES

    # Creates .mo files from the .po files
	msgfmt -c -o data/locales/en/LC_MESSAGES/langapp.mo po/en.po
	msgfmt -c -o data/locales/fr/LC_MESSAGES/langapp.mo po/fr.po
	msgfmt -c -o data/locales/zh_hant/LC_MESSAGES/langapp.mo po/zh_hant.po

	echo "I'm a PC"



# This doesn't get used on Windows thru Cygwin, but it might on Linux or Mac

mo:
	mkdir -p data/locales/en/LC_MESSAGES
	mkdir -p data/locales/fr/LC_MESSAGES
	mkdir -p data/locales/zh_hant/LC_MESSAGES
	msgfmt -c -o data/locales/en/LC_MESSAGES/langapp.mo po/en.po
	msgfmt -c -o data/locales/fr/LC_MESSAGES/langapp.mo po/fr.po
	msgfmt -c -o data/locales/zh_hant/LC_MESSAGES/langapp.mo po/zh_hant.po

	echo "I'm a mac"