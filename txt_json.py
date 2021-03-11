#fname = "D://Documentos/Gig/python/Canción-Rota.txt"
import re
import json

def meta_extraction(line):

    '''Función de extracción de metadatos'''

    line = line.strip()
    if (line != '' and line != None):
        line = line.split(':')
        data = line[0].strip().lower()
        atrib_s = line[1].strip().split(" ")
        atrib = ''
        for i in atrib_s:
            atrib = atrib + i.capitalize() + ' '
        if atrib.find('-') == -1:
            return [data, atrib.strip()]
        else:
            atrib_s = atrib.split('-')
            if atrib_s[0] != '' and atrib_s[1] != '':
                atrib = ''
                for i in atrib_s:
                    atrib = atrib + i.capitalize() + '-'
                return [data, atrib[:len(atrib)-1].strip()]
            else:
                return [data, atrib.strip()]
    else:
        return [None, None]


def song_extraction(line):

    ''' Función de extracción de datos de la canción'''

    line = line.strip()
    if (line != '' and line != None):
        if line.startswith('['):
            pos_ini = line.find('[')
            pos_fin = line.find(']')
            tipo = line[pos_ini+1:pos_fin]
            return [tipo, 'tipo']
        elif line.startswith('<'):
            pos_ini = line.find('<')
            pos_fin = line.find('>')
            acordes = line[pos_ini+1:pos_fin]
            return [acordes, 'acorde']
        elif line.startswith('{'):
            pos_ini = line.find('{')
            pos_fin = line.find('}')
            letra = line[pos_ini+1:pos_fin]
            return [letra, 'letra']
        else:
            print('Error de asignación en el formato')
    else:
        return [None, None]

def def_sub_datos(dato):

    '''Función de separación de acordes, espaciados y letras'''

    if dato[1] == 'letra':
        sub = dato[0]
        return [sub, None]
    elif dato[1] == 'acorde':
        contador = 0
        notas = ''
        espacio = ''
        n = ''
        ini = False
        for i in range(len(dato[0])):
            if dato[0][i] == ' ' :
                contador += 1
            else:
                if contador != 0 or ini == False:
                    espacio = espacio + ';' + str(contador)
                    ini = True
                contador = 0
        notes = re.findall('[a-z,A-Z,/,#,0-9]+', dato[0])
        for n in notes:
            notas = notas + ';' + n
        return [espacio[1:], notas[1:]]



if __name__ == '__main__':

    fname = "Canción-Rota.txt"
    fh = open(fname, encoding='utf-8')

    js= dict()
    metadata = dict()
    cancion = list()
    estrofa = dict()
    tipo = ''
    content = list()
    verso = dict()
    notas = ''
    espacio = ''
    letra = ''

    ini = True
    count = 1
    spynotas = []
    tipo_ant = ''


    for line in fh:
        if count <= 8:
            dato = meta_extraction(line)
            if dato[0] != None:
                metadata[dato[0]] = dato[1]
                count += 1
            if count == 8:
                js['metadata'] = metadata
        else:
            dato = song_extraction(line)
            if dato[0] != None:
                if dato[1] == 'tipo':
                    tipo = dato[0]
                    if tipo != tipo_ant and ini != True:
                        estrofa = {
                            'tipo' : tipo_ant,
                            'contenido' : content
                        }
                        cancion.append(estrofa)
                        content = []
                        verso = {}
                    ini = False
                    tipo_ant = tipo

                elif dato[1] == 'acorde':
                    spynotas = def_sub_datos(dato)
                    notas = spynotas[1]
                    espacio = spynotas[0]
                elif dato[1] == 'letra':
                    letras = def_sub_datos(dato)
                    letra = letras[0]
                    verso = {
                        'notas' : notas,
                        'espacio' : espacio,
                        'letra' : letra
                    }
                    content.append(verso)
                else:
                    print('Ha sucedido un error de clasificación de la canción')


    estrofa = {
        'tipo' : tipo_ant,
        'contenido' : content
    }
    cancion.append(estrofa)
    js['canción'] = cancion
    print(js)

    with open('song.json', 'w') as file:
        json.dump(js, file, indent=4, ensure_ascii=False)
