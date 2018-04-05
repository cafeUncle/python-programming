super_villains = {'fiddler': 'Isaac Bowin',
                  'Captain Cold': 'Leonard Sanrt',
                  'Weather Wizard': 'Mark Mardon',
                  'Mirror Master': 'Sam Scudder',
                  'Pied Piper': 'Thomas Peterson'}

if __name__ == 'main':
    print(super_villains)
    print(super_villains['Captain Cold'])

    del super_villains['Captain Cold']

    print(super_villains)
    # print(super_villains['Captain Cold'])

    super_villains['mew'] = 'new '

    print(super_villains)
    print(super_villains.get('mew'))
    print(super_villains.get('Captain Cold'))

    print(len(super_villains))
    print(super_villains.keys())
    print(super_villains.values())