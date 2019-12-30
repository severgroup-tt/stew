Stew
====

A library for parsing files containing localization strings.

Stew file format
----------------

.. code-block::

    [[section title]]

    [translation_key]
        en = English translation
        ru = Russian translation

Where ``[[section title]]`` is just an identifier for readability and structure
purposes only. It is not used by the library in any way.

``[translation_key]`` is a key that you should use in your localized files. Stew
does not impose any limitations on the format of the key, however, the
platform for which you are generating your strings, may. For example,
Android will turn your translation keys into static variables, so you can't have
white spaces or dashes in them. So keep that in mind.

``en = English translation``: a translation for a particular language, English
in this case.

Plurals
+++++++
To have multiple plural forms, use the following notation:

.. code-block::

    ru = %s thing
    ru[1] = %s things

Please, consult the documentation for your platform for the indices corresponding
to the required plural form.

