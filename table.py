from pathlib import Path


files = [x for x in sorted(list(Path('.').iterdir())) if not x.name.endswith('.py') and not x.name.endswith('~')]
#print(files)
print('VERSION\tUNCOMPRESSED\tBROTLI\tGZIP')
for idx, i in enumerate(range(0, len(files), 3)):
    #print(i)
    sizes = [files[i + j].stat().st_size for j in range(3)]
    print('\t'.join((str(idx),) + tuple(str(x) for x in sizes)))
    #for j in range(3):
    #    file = files[i + j]
    #    #print('\t', j, file)
    #    print(f"{file.stat().st_size}", )
    #print(thing)
