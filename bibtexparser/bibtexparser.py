'''
Parses BibTeX files, and finds missing fields
'''

from typing import Optional

def parse(bibtex: str) -> dict:
    '''
    Parses the contents of a BibTex file.

    Args:
        bibtex (str): BibTeX text to be parsed

    Returns:
        dict: dictionary containing the references
    '''
    d = dict()
    openRef = False
    lines = bibtex.split('\n')
    for l in lines:
        if len(l) == 0:
            continue
        if not openRef:
            if l[0] == '@':
                spl = l[1:].split('{')
                refdict = {'bibclass': spl[0]}
                bibref = spl[1].strip(',')
                openRef = True
        else:
            if l == '}':
                openRef = False
                d.update({bibref: refdict})
            else:
                spl = l.split('=')
                if len(spl) < 2:
                    continue
                if spl[1][-1] == ',':
                    cont = spl[1][:-1]
                else:
                    cont = spl[1]
                refdict.update({spl[0].strip(): cont.strip()})
    return d


def missingfield(dbib: dict, field: str, bibclass: Optional[str] = None) -> None:
    '''
        Looks for missing fields in the dictionary containing the bibliography.

        Args:
            dbib (dict): Dictionary created by :parse():.
            field (str): Field to check if it is missing.
            bibclass (str, optional): Class of BibTex entries to look, for example article. Defaults to None
        '''

    for key, ref in dbib.items():
        check = True
        if bibclass is not None:
            check = (bibclass == ref['bibclass'])
        if check:
            if field not in ref.keys():
                print(key, '\n')
