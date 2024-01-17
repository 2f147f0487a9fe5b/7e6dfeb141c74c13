import requests
import re
import patches

patch_exp = "(?<=\?v=)(\d+)"

class PatchError(Exception):
    pass

def read_patches() -> dict:
    output = {var: value for var, value in vars(patches).items() if not var.startswith('__')}
    return output

def get_local_version(filename: str = None) -> int:
    try:
        with open(filename, 'r') as file:
            file = file.read()        
        version = re.search(patch_exp , file).group()
        return version
    except FileNotFoundError:
        return 0
    
def request_current_version(url: str = None) -> int:
    with requests.get(url) as file:
        filecontent = file.content.decode()
    version = re.search(patch_exp , filecontent).group()
    return version

def request_file(url: str, version: int) -> str:
    with requests.get(f"{url}?v={version}") as file:
        filecontent = file.content.decode()
    return filecontent

class Patcher:
    @staticmethod
    def autopatch(base_url: str = "https://hordes.io", filename: str = "client.js") -> None:
        patch = read_patches()
        fetched_patches = patch.keys()
        if len(patch) > 0:
            print(f"Fetched patches: {','.join(fetched_patches)}")
        else:
            print(f"No patches fetched")

        local_version = get_local_version(filename)

        current_version = request_current_version(base_url)

        if int(str(local_version)[:4]) == int(str(current_version)[:4]):
            raise PatchError("File already contains last version. hint: delete file if you want to recreate it.")

        filecontent = request_file(f'{base_url}/{filename}', current_version)

        for key, value in patch.items():
            print(f"Applying {key}: 0/{len(value)}")
            for i, iv in enumerate(value):
                filecontent = re.sub(iv['expression'], iv['value'], filecontent)
                print(f"Applying {key}: {i+1}/{len(value)}")
            print(f"Applied {key}.")
        
        filename = f'{"_".join(fetched_patches)}_{filename}'
        with open(filename, 'w') as file:
            file.write(filecontent)

        print(f"Successfully finished patching {filename}")

if __name__ == "__main__":
    Patcher.autopatch()
    input("Press enter to exit...")