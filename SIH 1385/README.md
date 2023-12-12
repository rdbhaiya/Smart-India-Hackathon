
# SIH-1385 (Developing a software that can translate resource material and other texts from English to other Indian regional languages.)
NOTE: You have to change your directories based on your system path.
1385:
=
Organization Name: Ministry of Commerce and Industries
,PS Code: SIH1385
,Team Name: SANSKRITI_06
,Team Leader Name: Rupam Das
,Institute Code (AISHE): U-0865
,Institute Name: Techno India University
,Theme Name: Smart Education

Idea Description: The idea is to translate resource materials namely - old book pages, english manuscipts, research papers, documents, historical accounts etc. to a desired language so that people who are not familiar with English, can also get a look at these materials and understand them. The idea is to also make the application look more like of a dictionary than like a translator. The translated materials would be available for users where they can also download them for other uses.

Abstract/Summary: For the implementation, we use the python 'PyPDF2' module for extracting all of the text available inside the document/pdf/word file/image. We store this text as in the string format inside a variable. Then we use Google API - 'googletrans' to translate the full text from English into a desired language. Then we use 'Document' method from the python 'docx' module to convert back the translated text into a document. Regarding reading/extracting texts from an image, we use the python 'pytesseract' module and 'PIL' module and then the same procedure follows.

============================================
YOUTUBE LINK: https://www.youtube.com/watch?v=TJlwgvsJD64
============================================
