import json, uuid, os

def manifest():
  print("MC Pack Template Generator\n")
  name = input("> Name: ")
  desc = input("> Description: ")
  
  manifest = {
    "format_version": 2,
    "header": {
        "description": desc,
        "name": name,
        "uuid": str(uuid.uuid4()),
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

  os.mkdir(f'packs/{name}')
  
  manifest_json = json.dumps(manifest, indent=2)
  with open(f'packs/{name}/manifest.json', 'w') as f:
    f.write(manifest_json)

manifest()
