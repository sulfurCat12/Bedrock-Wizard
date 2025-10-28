import json, uuid, os

name = ''
desc = ''
BPorRP = 0

RP_UUID = uuid.uuid4()

def manifest_RP():
  manifest = {
    "format_version": 2,
    "header": {
        "description": desc,
        "name": name,
        "uuid": str(RP_UUID),
        "version": [1, 0, 0],
        "min_engine_version": [ 1, 21, 110 ]
    },
    "modules": [
        {
            "description": desc,
            "type": "resources",
            "uuid": str(uuid.uuid4()),
            "version": [1, 0, 0]
        }
    ]
  }

  if BPorRP == 1:
    manifest_json = json.dumps(manifest, indent=2)
    with open(f'packs/{name}/manifest.json', 'w') as f:
      f.write(manifest_json)
  elif BPorRP == 3:
    os.makedirs(f'packs/{name}/RP', exist_ok=True)
    manifest_json = json.dumps(manifest, indent=2)
    with open(f'packs/{name}/RP/manifest.json', 'w') as f:
      f.write(manifest_json)

def manifest_BP():
  manifest = {
    "format_version": 2,
    "header": {
        "description": desc,
        "name": name,
        "uuid": str(uuid.uuid4()),
        "version": [1, 0, 0]
    },
    "modules": [
        {
            "description": desc,
            "type": "data",
            "uuid": str(uuid.uuid4()),
            "version": [1, 0, 0]
        },
        {
            "description": desc,
            "type": "client_data",
            "uuid": str(uuid.uuid4()),
            "version": [1, 0, 0]
        }
    ],
    "dependencies": [
        {
            "uuid": str(RP_UUID),
            "version": [1, 0, 0]
        }
    ]
  }

  if BPorRP == 2:
    manifest_json = json.dumps(manifest, indent=2)
    with open(f'packs/{name}/manifest.json', 'w') as f:
      f.write(manifest_json)
  elif BPorRP == 3:
    os.makedirs(f'packs/{name}/BP', exist_ok=True)
    manifest_json = json.dumps(manifest, indent=2)
    with open(f'packs/{name}/BP/manifest.json', 'w') as f:
      f.write(manifest_json)

def init():
  global name, desc, BPorRP
  print("MC Pack Template Generator\n")

  name = str(input('> Name: '))
  desc = str(input('> Description: '))

  BPorRP = int(input('> What type of pack do you want to generate? (1/2/3)\n1. Resource Pack\n2. Behaviour Pack\n3. Addon (RP + BP)\n'))

  os.makedirs(f'packs/{name}', exist_ok=True)

  if BPorRP == 1:
    manifest_RP()
    print(f'Resource Pack Template successfully generated at packs/{name}')
  elif BPorRP == 2:
    manifest_BP()
    print(f'Behaviour Pack Template successfully generated at packs/{name}')
  elif BPorRP == 3:
    manifest_RP()
    manifest_BP()
    print(f'Addon Pack Template successfully generated at packs/{name}')
  else:
    print('Error; Please enter a valid type')

init()
