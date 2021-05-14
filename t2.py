import logging
import json

def main(req):
    logging.info('Python HTTP trigger function processed a request.')

    nset = None
    if not nset:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            nset = req_body.get('set')

    if nset:
        data = {'set': nset, 'powerSet': powerset(nset)}
        out = json.dumps(data)
        return out


def powerset(nset):
        out = [[]]
        
        for element in nset:
            out += [i + [element] for i in out]
        
        return out
